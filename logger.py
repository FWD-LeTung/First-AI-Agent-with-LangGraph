import json
import os
from datetime import datetime

LOG_FILE = "agent_metrics.jsonl"

def log_interaction(user_input: str, ai_response: str, metrics: dict):
    """
    Ghi log toàn bộ tương tác và in tóm tắt metric ra màn hình.
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "input": user_input,
        "output": ai_response,
        "metrics": metrics
    }
    
    # Ghi nối tiếp vào file JSONL
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
        
    # In một dòng tóm tắt nhỏ ra terminal để tiện theo dõi
    print(f"\n[📊 Metrics] Latency: {metrics['latency']}s | "
          f"Tokens: {metrics['prompt_tokens']} (prompt) + "
          f"{metrics['completion_tokens']} (completion) = "
          f"{metrics['total_tokens']} (total)")