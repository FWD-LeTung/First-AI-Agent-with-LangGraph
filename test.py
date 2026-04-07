import time
from agent import graph  # Import graph đã compile từ agent.py
from metric import AgentMetrics
from logger import log_interaction

# Danh sách 5 kịch bản từ tài liệu Lab 4
TEST_CASES = [
    "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
    "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng",
    "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!",
    "Tôi muốn đặt khách sạn",
    "Giải giúp tôi bài tập lập trình Python về linked list"
]

def run_automated_tests():
    print("="*70)
    print("🚀 BẮT ĐẦU CHẠY TỰ ĐỘNG 5 KỊCH BẢN TEST")
    print("="*70)

    tracker = AgentMetrics()

    for i, prompt in enumerate(TEST_CASES, 1):
        print(f"\n{'='*20} BẮT ĐẦU TEST {i} {'='*20}")
        print(f"👤 User: {prompt}")
        
        # Cấp thread_id độc lập cho mỗi test để reset trí nhớ
        config = {"configurable": {"thread_id": f"auto_test_case_{i}"}}
        
        tracker.start_timer()
        
        try:
            # Gọi Agent xử lý
            result = graph.invoke(
                {"messages": [("human", prompt)]}, 
                config=config
            )
            latency = tracker.stop_timer()
            
            # Lấy kết quả cuối cùng
            final_message = result["messages"][-1]
            ai_response = final_message.content
            
            # Trích xuất metric
            tokens = tracker.extract_tokens(final_message)
            metrics_data = {"latency": latency, **tokens}
            
            print(f"\n🤖 TravelBuddy:\n{ai_response}")
            
            # Ghi log (đánh dấu [TEST i] để dễ nhìn trong file)
            log_interaction(f"[TEST {i}] {prompt}", ai_response, metrics_data)
            
        except Exception as e:
            print(f"\n❌ Lỗi khi chạy Test {i}: {e}")
        
        # Tạm nghỉ 2 giây giữa các test để tránh bị API rate limit
        time.sleep(2)
        print(f"{'='*53}")

if __name__ == "__main__":
    run_automated_tests()
    print("\n✅ Đã hoàn thành 5 test cases! Kiểm tra file agent_metrics.jsonl để xem log chi tiết.")