# Báo cáo nhóm

Báo cáo ngắn (≤ 2 trang). Số liệu chi tiết nằm trong các file hồ sơ trong `report/team/`; dưới đây tóm tắt các con số chính và quyết định của nhóm.

## 1. Thông tin nhóm

- Tên nhóm: T100
- Lớp: L3B
- Thành viên: xem `TEAM.md` (Đào Đức Duy — N1, Phạm Minh Đức — N2, Bùi Ngọc Hùng — N3, Trần Cảnh Hưng — N4)

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng bộ **hồ sơ launch v0** cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập 1.200 yêu cầu / 1.624 lần chạy) để bảo vệ trước hội đồng **Gate 2a** (duyệt kế hoạch pilot). Quy trình gồm 5 bước tuần tự: định giá chi phí mỗi việc thành công (A), phân tích độ nhạy và giới hạn chạy lại (B), phân loại 20 ca lỗi theo nguyên nhân gốc PAIR và gán cơ chế khắc phục đo được (C), thiết kế pilot có đối chứng đủ cỡ mẫu và luật dừng (D), sau đó đặc tả chỉ số/event, rủi ro kinh tế và tổng hợp hồ sơ 1 trang (E).

## 3. Giải pháp

- **Nhiệm vụ A & B (Mô hình chi phí và độ nhạy):** Triển khai `src/lab13.py` (qua đủ 3 phép thử A1: `1,20 · 1,25 · 1,25`), tính CPS toàn mẫu, tách 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng và chạy 9 kịch bản độ nhạy + B2/B3/B4 → [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi & khắc phục):** N3 và N4 gắn nhãn độc lập 20 ca lỗi không trao đổi, đạt đồng thuận 20/20 (100%), chọn 5 ca đại diện đủ 5 loại PAIR với cách phát hiện đo được và 1 vai trò phụ trách → [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính đủ 5 câu cỡ mẫu D1, chọn chia ngẫu nhiên theo nhân viên 20+20 (phân tầng depot), ghi rõ đánh đổi MDE 6 điểm và thiết lập 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ` → [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, event, rủi ro & hồ sơ launch v0):** Tính thử 3 chỉ số E1, đề xuất thêm 2 chỉ số, định nghĩa 11 event có `trace_id` kèm kiểm tra chéo, liên kết rủi ro kinh tế từ bảng độ nhạy → [chi_so.md](chi_so.md) và tổng hợp 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Kinh tế (có nhãn `simulated`):** CPS toàn mẫu **4.472 đ** (`simulated`), gấp **16,28×** hoá đơn token+tool **274,7 đ/yêu cầu** (đo từ trace); giờ nhân viên chiếm **92,5%** (làm lại 51,8%, xem lại 40,7%). So công bằng cả hệ thống (gồm 222 ca không thành công): **5.865 đ/yêu cầu = 0,49×** mức nhân viên tự làm 12.000 đ (`simulated`).
- **Thu hẹp phạm vi & độ nhạy:** Loại `quoc_te` (**22.515 đ = 1,88×**, thành công 27,3%, `ok` giảm 30,0% → 11,4% → 2,2%) và `doi_tac` (**10.215 đ = 0,85×**). Trong phạm vi `noi_dia + hang_nang`, kể cả cộng chi phí cố định vẫn là **4.599 đ (0,38×)** ở 45.000 yc/tháng hoặc **5.784 đ (0,48×)** ở nửa tải (`simulated`). Giới hạn **2 lần chạy** rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`). Nếu phải xem lại 100% thì CPS lên **11.743–12.415 đ (0,98–1,03×, `simulated`)**, mất lợi thế kinh tế.
- **Chỉ số đợt chạy thử (không đối chứng):** Chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200); trong phạm vi pilot đạt lần lượt **92,26%**, **21,09%** và **3,97%**.
- **Đề xuất cuối ([ho_so_launch_v0.md](ho_so_launch_v0.md)):** **Go có điều kiện** cho pilot `noi_dia + hang_nang` (tối đa 2 lần chạy) với 4 điều kiện có người phụ trách và ngày kiểm tra cụ thể (sửa chống hoàn trùng/sổ cái, ký chấp nhận MDE 6 điểm, thay phút `simulated` bằng phút đo thật sau tuần 1, lộ trình giảm xem lại theo bậc).
- **Kết quả duyệt chéo Gate 2a:** *(nhóm cập nhật sau phiên duyệt chéo 17:00 và đính kèm phiếu chấm tại [phieu_cham.md](phieu_cham.md)).*

## 5. Khó khăn và cách xử lý

- **Cỡ mẫu cụm bị giới hạn bởi số nhân viên (40 người):** Chia theo nhân viên 20+20 chỉ đạt `n_hiệu dụng` tối đa 1.000 < 1.251 (không đủ thấy mức chênh +5 điểm). Nhóm xử lý bằng cách giữ chia ngẫu nhiên theo nhân viên 20+20 để đảm bảo ≥ 20 cụm và tránh tràn tác động, chấp nhận MDE 6 điểm (`n = 859`, `m ≥ 299`, `DE = 6,96`) và nêu minh bạch đánh đổi power ~0,64 ở mức 5 điểm.
- **Đồng bộ nhãn `simulated` và cách so sánh công bằng:** Khi rà soát chéo giữa các file, nhóm phát hiện thiếu nhãn `simulated` ở một số bảng độ nhạy và so sánh nhầm 0,37× chưa cộng phần chuyển nhân viên; nhóm đã chuẩn hóa toàn bộ nhãn `simulated`, dùng số cả hệ thống 0,49× và đồng bộ event `input_validation_failed` giữa `bang_loi.md` và `chi_so.md`.

## 6. Tổng hợp đóng góp

Chi tiết vai trò, phần việc và bằng chứng commit của từng thành viên nằm trong [TEAM.md](../../TEAM.md) và các file báo cáo cá nhân `report/team/<MSSV>_<HoTen>.md`.

## 7. Hạn chế và hướng cải thiện

- Các chỉ số chi phí hiện dựa trên phút xem lại/làm lại giả lập (`_simulated`); cần thay thế bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed` ngay sau tuần 1 của pilot.
- Đợt chạy thử 2 tuần không có nhóm đối chứng nên không khẳng định tác động nhân quả; thiết kế pilot 20+20 nhân viên ngẫu nhiên phân tầng theo depot sẽ giải quyết điểm này.

## 8. Tài liệu tham khảo

- Tài liệu và dữ liệu giả lập Lab 13 (`docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`).
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (arXiv:2504.13359).
- Google PAIR, *People + AI Guidebook* — chương "Errors + Graceful Failure".
