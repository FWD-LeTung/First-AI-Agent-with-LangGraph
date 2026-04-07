```
==================== BẮT ĐẦU TEST 1 ====================
👤 User: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
  [Log] Trả lời trực tiếp

🤖 TravelBuddy:
Chào bạn! Mình là trợ lý du lịch của TravelBuddy đây 😊 Để mình gợi ý lịch trình và lên phương án chi phí sát thực tế nhất cho bạn, bạn cho mình xin thêm vài thông tin nhé:

📍 Bạn xuất phát từ thành phố nào?  
🏖️ Bạn thích kiểu du lịch nào hơn? (ví dụ: biển nghỉ dưỡng, núi/phượt khám phá, thành phố ẩm thực, hay văn hóa lịch sử?)  
📅 Dự kiến đi bao nhiêu ngày?  
💰 Ngân sách dự kiến cho cả chuyến đi khoảng bao nhiêu?  
👥 Đi mấy người? (1 mình, cặp đôi, gia đình hay nhóm bạn?)

Cứ chia sẻ thoải mái nhé, mình sẽ dựa trên ngân sách thực tế để tra cứu vé máy bay, tính toán chi phí còn lại và tìm khách sạn phù hợp nhất cho bạn luôn! 🌴✈️

[📊 Metrics] Latency: 18.68s | Tokens: 1116 (prompt) + 868 (completion) = 1984 (total)
=====================================================
```

```
==================== BẮT ĐẦU TEST 2 ====================
👤 User: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
  [Log] Gọi tool: search_flights ({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})
  [Log] Trả lời trực tiếp

🤖 TravelBuddy:
Chào bạn! Mình vừa tra cứu giúp bạn các chuyến bay từ Hà Nội đi Đà Nẵng đây. Bạn tham khảo nhé:

- **Chuyến bay:** 
  • VietJet Air | 08:30 -> 09:50 | 890.000₫ (Economy) 💡 *Lựa chọn tiết kiệm nhất*
  • Bamboo Airways | 11:00 -> 12:20 | 1.200.000₫ (Economy)
  • Vietnam Airlines | 06:00 -> 07:20 | 1.450.000₫ (Economy)
  • Vietnam Airlines | 14:00 -> 15:20 | 2.800.000₫ (Business)

- **Khách sạn:** Mình sẽ tìm ngay các chỗ nghỉ phù hợp ngay sau khi bạn cho biết thêm thông tin.
- **Tổng chi phí ước tính:** Đang chờ bạn chốt ngân sách tổng & số đêm lưu trú để mình tính dư/thiếu chính xác.
- **Gợi ý thêm:** Để mình tư vấn trọn gói (vé + khách sạn + bảng chi tiêu chi tiết), bạn nhắn mình thêm 3 thông tin nhỏ nhé:
  1️⃣ Bạn dự định đi bao nhiêu đêm?
  2️⃣ Ngân sách tổng cho chuyến này tầm bao nhiêu?
  3️⃣ Bạn thích khách sạn ở khu vực nào? (Ví dụ: gần biển Mỹ Khê để sáng tắm biển, khu trung tâm sông Hàn để tiện ăn chơi, hay khu yên tĩnh như Sơn Trà?)

Có thông tin này là mình tính toán ngân sách dư ra cho bạn và gợi ý khách sạn "đáng đồng tiền" liền nhé! 😊✈️

[📊 Metrics] Latency: 70.54s | Tokens: 1324 (prompt) + 1959 (completion) = 3283 (total)
=====================================================
```
```

==================== BẮT ĐẦU TEST 3 ====================
👤 User: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
  [Log] Gọi tool: search_flights ({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})
  [Log] Gọi tool: calculate_budget ({'expenses': 'vé_máy_bay: 1100000', 'total_budget': 5000000})
  [Log] Gọi tool: search_hotels ({'city': 'Phú Quốc', 'max_price_per_night': 1950000})
  [Log] Trả lời trực tiếp

🤖 TravelBuddy:
Chào bạn! Mình đã rà soát xong cho chuyến Hà Nội → Phú Quốc 2 đêm với ngân sách 5 triệu. Đây là phương án mình gợi ý nhé:

- **Chuyến bay**: VietJet Air | 16:00 → 18:15 | **1.100.000₫**. Đây là lựa chọn rẻ nhất, giúp bạn tiết kiệm để dành ngân sách cho khách sạn và vui chơi ở đảo ngọc. Nếu thích bay sáng, Vietnam Airlines lúc 10:00 giá 1.350.000₫ cũng là option tốt.

- **Khách sạn** (2 đêm):
  - 🌟 **9Station Hostel** (2⭐, Dương Đông): 200.000₫/đêm → 2 đêm = **400.000₫**. Rating 4.5 rất ngon, hợp túi tiền, còn dư nhiều để ăn chơi.
  - 🌟 **Lahana Resort** (3⭐, Dương Đông): 800.000₫/đêm → 2 đêm = **1.600.000₫**. Balance tốt giữa giá và chất lượng, gần trung tâm Dương Đông tiện di chuyển.
  - 🌟 **Sol by Meliá** (4⭐, Bãi Trường): 1.500.000₫/đêm → 2 đêm = **3.000.000₫**. Resort xịn ngay bãi biển đẹp, nếu muốn nghỉ dưỡng sang chảnh hơn.

- **Tổng chi phí ước tính** (chọn VietJet + 9Station Hostel):
  - Vé máy bay: 1.100.000₫
  - Khách sạn 2 đêm: 400.000₫
  - **Còn lại**: ~3.500.000₫ cho ăn uống, di chuyển, tour khám đảo. Quá thoải mái luôn! 🎉

- **Gợi ý thêm**:
  - Phú Quốc 2 đêm thì bạn nên book 1 tour 3 đảo (Hòn Mây Rút, Hòn Dăm Ngang, Hòn Gầm Ghì) để ngắm san hô và lặn biển. Giá tour thường khoảng 400.000 - 600.000₫/người.
  - Nhớ mang kem chống nắng, kính râm và áo phao nếu có kế hoạch tắm biển nhiều nhé.
  - Đặt vé sớm để giá tốt hơn, nhất là nếu đi cuối tuần!

Bạn thích phương án khách sạn nào? Hoặc cần mình tính lại chi tiết hơn cho option khác không? 😊

[📊 Metrics] Latency: 48.53s | Tokens: 1651 (prompt) + 828 (completion) = 2479 (total)
=====================================================
```
```
==================== BẮT ĐẦU TEST 4 ====================
👤 User: Tôi muốn đặt khách sạn
  [Log] Trả lời trực tiếp

🤖 TravelBuddy:
Chào bạn! Mình sẵn sàng hỗ trợ bạn tìm khách sạn ưng ý nhất nè. 🏨✨

Để mình gợi ý chuẩn xác và sát với túi tiền nhất, bạn cho mình biết thêm vài thông tin nhé:
- 📍 Bạn định đặt khách sạn ở **thành phố/tỉnh nào**?
- 💰 Ngân sách dự kiến cho **mỗi đêm** khoảng bao nhiêu? (Nếu chưa có con số cụ thể thì cứ nói khoảng giá mong muốn, mình sẽ linh động chọn)
- 👥 Bạn đi mấy người và cần mấy phòng?
- 📍 Có ưu tiên khu vực nào không? (ví dụ: gần biển, trung tâm thành phố, gần chợ/điểm vui chơi, hay yên tĩnh nghỉ ngơi...)

Cứ nhắn mình, mình sẽ lọc ngay những khách sạn có đánh giá tốt và giá hợp lý nhất trong tầm bạn chọn nha! 😊

[📊 Metrics] Latency: 16.38s | Tokens: 1105 (prompt) + 723 (completion) = 1828 (total)
=====================================================
```
```
==================== BẮT ĐẦU TEST 5 ====================
👤 User: Giải giúp tôi bài tập lập trình Python về linked list
  [Log] Trả lời trực tiếp

🤖 TravelBuddy:
Chào bạn, mình là trợ lý du lịch của TravelBuddy nên chuyên môn của mình chỉ hỗ trợ các vấn đề liên quan đến du lịch như tìm vé máy bay, đặt khách sạn, lên lịch trình hay tính toán ngân sách đi chơi thôi nhé. Mình không thể hỗ trợ giải bài tập lập trình Python được. 

Nếu bạn đang lên kế hoạch cho một chuyến đi thực tế, cần tìm vé bay giá tốt, khách sạn phù hợp ngân sách, hay muốn tư vấn điểm đến tại Việt Nam, cứ nhắn mình nhé. Mình sẵn sàng đồng hành cùng bạn! 😊✈️🌴

[📊 Metrics] Latency: 11.96s | Tokens: 1111 (prompt) + 608 (completion) = 1719 (total)
=====================================================
```
