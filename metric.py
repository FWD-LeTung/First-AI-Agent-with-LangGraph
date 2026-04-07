import time
from langchain_core.messages import AIMessage

class AgentMetrics:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start_timer(self):
        """Bắt đầu đếm thời gian."""
        self.start_time = time.time()

    def stop_timer(self) -> float:
        """Dừng đếm và trả về độ trễ (giây)."""
        self.end_time = time.time()
        return round(self.end_time - self.start_time, 2)

    def extract_tokens(self, message: AIMessage) -> dict:
        """
        Trích xuất số lượng token từ response_metadata của LangChain AIMessage.
        API tương thích của DashScope (Qwen) thường trả về dữ liệu này trong key 'token_usage'.
        """
        metadata = getattr(message, 'response_metadata', {})
        token_usage = metadata.get("token_usage", {})
        
        return {
            "prompt_tokens": token_usage.get("prompt_tokens", 0),
            "completion_tokens": token_usage.get("completion_tokens", 0),
            "total_tokens": token_usage.get("total_tokens", 0)
        }