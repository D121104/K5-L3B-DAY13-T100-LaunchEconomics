# Báo cáo cá nhân — Phạm Minh Đức · 2A202603758

## 1. Thông tin thành viên

- Họ tên: Phạm Minh Đức
- MSSV: 2A202603758
- Email: 26ai.ducpm@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (N2, nhận code sau giải lao)

## 2. Phần việc phụ trách

- **N2 — Người kiểm số:** kiểm tra dữ liệu đầu vào, đối chiếu độc lập kết quả `src/lab13.py` cho toàn bộ nhiệm vụ A1–A4 và B1–B4; điền đầy đủ bảng trong `report/team/bang_chi_phi.md`; xác nhận số liệu chi phí phục vụ phân tích rủi ro kinh tế (E2) và xác định phạm vi pilot.

## 3. Đóng góp cụ thể

- Tạo nhánh riêng `PhamMinhDuc_2A202603758`, pull code mới nhất từ `main`.
- Chạy và kiểm tra `src/lab13.py`: xác nhận ba phép thử A1 đạt (1,20 · 1,25 · 1,25).
- Điền bảng **A2**: tổng chi phí 4.373.585 đ, CPS = 4.472 đ, gấp 16,28× hoá đơn token/yêu cầu; xác định khoản làm lại chiếm 51,8% tổng chi phí (simulated).
- Điền bảng **A3**: tách 4 loại yêu cầu, chỉ ra `quoc_te` không đáng để trợ lý xử lý (CPS = 22.515 đ, 1,88× baseline), phân tích lý do chạy lại không giúp ích.
- Điền bảng **A4**: chi phí cố định ở hai mức tải (45.000 và 22.500 req/tháng), kết luận vẫn rẻ hơn baseline cả hai trường hợp.
- Điền bảng **B1**: 9 kịch bản độ nhạy, xác định thứ tự ảnh hưởng: làm lại (+51,8%) > xem lại (+40,7%) > lương nhân viên (+23,1%).
- Điền **B2**: xác nhận tính cộng tuyến tính của mô hình chi phí (token gấp đôi + xem lại gấp đôi = +46,3%).
- Điền **B3**: so sánh 3 giới hạn chạy lại — giới hạn 2 lần rẻ nhất cho cả hệ thống (6.901.220 đ), giới hạn 1 lần có CPS thấp nhất nhưng đẩy nhiều ca sang nhân viên.
- Điền **B4**: xem lại 100% đẩy CPS lên 11.743–12.415 đ, gần bằng baseline — pilot phải đo thời gian làm lại thực tế.

## 4. Bằng chứng

- Nhánh `PhamMinhDuc_2A202603758`, commit `cc51afa` — `report/team/bang_chi_phi.md` (40 dòng thay đổi, điền đầy đủ A1–A4 và B1–B4).
- Chạy độc lập `src/lab13.py` với venv Python để lấy số liệu đối chiếu trực tiếp từ CSV.

## 5. Công cụ AI đã dùng

- **Claude Code (Claude Sonnet 4.6):** hỗ trợ cài đặt venv, chạy `lab13.py` và điền `bang_chi_phi.md` từ output thực tế. Tự kiểm tra: đối chiếu từng con số với output terminal của `python lab13.py`, xác nhận A1 đạt 3/3 phép thử trước khi điền bảng; kiểm tra B2 bằng tay (5,6% + 40,7% ≈ 46,3%) để xác nhận tính cộng tuyến tính.

## 6. Tự đánh giá

Hoàn thành đúng vai người kiểm số: điền đầy đủ và chính xác bảng A1–A4 và B1–B4 với số liệu từ trace thực tế. Phân tích B3 chỉ ra rằng "giới hạn chạy rẻ nhất cho CPS" và "rẻ nhất cho cả hệ thống" là hai mục tiêu khác nhau — điểm quan trọng cho quyết định thiết kế pilot. Điểm cần cải thiện: nên tham gia phân tích CP3 (gắn nhãn lỗi) để hiểu sâu hơn nguyên nhân lỗi ảnh hưởng đến chi phí.
