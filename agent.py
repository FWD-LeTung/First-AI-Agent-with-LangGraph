from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage

from metric import AgentMetrics
from logger import log_interaction
from tools import search_flights, search_hotels, calculate_budget
from dotenv import load_dotenv
import os

load_dotenv()

# Đọc System Prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

# Khai báo State
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 3. Khởi tạo LLM và Tools
tools_list = [search_flights, search_hotels, calculate_budget]

# Cấu hình Qwen
llm = ChatOpenAI(
    model="qwen3.6-plus",
    api_key=os.getenv("OPENAI_API_KEY"), # Lấy API Key từ file .env
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
llm_with_tools = llm.bind_tools(tools_list)

# 4. Agent Node
def agent_node(state: AgentState):
    messages = state["messages"]
    if not messages or not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
        
    response = llm_with_tools.invoke(messages)
    
    # LOGGING
    if response.tool_calls:
        for tc in response.tool_calls:
            print(f"  [Log] Gọi tool: {tc['name']} ({tc['args']})")
    else:
        print(f"  [Log] Trả lời trực tiếp")
        
    return {"messages": [response]}

# 5. Xây dựng Graph
builder = StateGraph(AgentState)
# 2 node chính agent và tools
builder.add_node("agent", agent_node)
tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

# TODO
builder.add_edge(START, "agent")

builder.add_conditional_edges("agent", tools_condition)

builder.add_edge("tools", "agent")

# memory 
memory = MemorySaver()
# build Graph
graph = builder.compile(checkpointer=memory)

# 6. Chat loop
if __name__ == "__main__":
    print("="*60)
    print("TravelBuddy - Trợ lý Du lịch Thông minh")
    print(" Gõ 'quit' để thoát")
    print("="*60)
    
    config = {"configurable": {"thread_id": "1"}} 
    tracker = AgentMetrics() # Khởi tạo bộ đo lường

    while True:
        user_input = input("\nBạn: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            break
            
        print("\nTravelBuddy đang suy nghĩ...")
        tracker.start_timer()

        result = graph.invoke(
            {"messages": [("human", user_input)]}, 
            config=config
        )
        latency = tracker.stop_timer()
        final_message = result["messages"][-1]
        tokens = tracker.extract_tokens(final_message)
        
        metrics_data = {
            "latency": latency,
            **tokens
        }
        print(f"\nTravelBuddy: {final_message.content}")
        
        #Ghi log lại
        log_interaction(user_input, final_message.content, metrics_data)