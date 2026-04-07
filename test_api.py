from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

client = OpenAI(
    # If the environment variable is not set, replace it with your Model Studio API key: api_key="sk-xxx"
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)

messages = [{"role": "user", "content": "Who are you"}]
completion = client.chat.completions.create(
    model="qwen3.6-plus",  # You can replace this with another deep thinking models
    messages=messages,
    extra_body={"enable_thinking": True},
    stream=True
)

# In ra câu trả lời từ LLM dạng streaming
print("LLM Response (Streaming):")
print("-" * 50)
for chunk in completion:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end='', flush=True)
print("\n" + "-" * 50)  

