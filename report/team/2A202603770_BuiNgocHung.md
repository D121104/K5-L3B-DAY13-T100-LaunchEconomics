# Báo cáo cá nhân — BuiNgocHung-2A202603770

## 1. Thông tin thành viên

- Họ tên: Bùi Ngọc Hùng
- MSSV: 2A202603770
- Email: 26ai.hungbn@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1 (N3 — Error Analyst 1)

## 2. Phần việc phụ trách

- **CP3 (Nhiệm vụ C):** Đọc 20 ca lỗi trong đề bài và taxonomy 5 loại của Google PAIR; gắn nhãn độc lập toàn bộ 20 ca theo nguyên nhân gốc, khóa nhãn trước khi đối chiếu với N4 và kiểm tra tính đo được của bảng khắc phục 5 ca.
- **CP4 (Nhiệm vụ D):** Tính tỉ lệ mở lại trong 7 ngày thực tế của mẫu chạy thử để đề xuất chỉ số an toàn và ngưỡng dừng an toàn theo mẫu `NẾU – TRONG – THÌ – KHÔNG THÌ`.
- **CP5 (Nhiệm vụ E):** Tính thử 3 chỉ số E1 trên `src/logix_requests.csv`, đề xuất thêm 1 chỉ số dùng và 1 chỉ số an toàn, xây dựng danh sách event có `trace_id` kèm kiểm tra chéo ánh xạ chỉ số ↔ event trong `report/team/chi_so.md`.
- **Rà soát & Duyệt chéo Gate 2a:** Rà nhãn `simulated`, kiểm tra tuân thủ quy tắc 5 (Gate 2a chỉ duyệt kế hoạch pilot), đồng bộ các file hồ sơ trước duyệt chéo và tham gia chấm nhóm bạn.

## 3. Đóng góp cụ thể

- Tự tính và đối chiếu trực tiếp từ `src/logix_requests.csv` (1.200 yêu cầu): chỉ số chính trong đợt chạy thử **82,83%** (`994/1.200`; `noi_dia + hang_nang`: **92,26%**), tỉ lệ bỏ qua gợi ý **27,12%** (`48/177`; `noi_dia + hang_nang`: **21,09%**), tỉ lệ mở lại 7 ngày **4,25%** (`51/1.200`; `noi_dia + hang_nang`: **3,97%**).
- Thiết kế bảng **11 event** đều có `trace_id` (gồm cả `input_validation_failed` khớp Ca 9, `staff_review_decision`/`staff_rework_completed` để thay phút `simulated` bằng phút đo thật, và `audit_sample_checked`/`refund_ledger_write` để phát hiện lỗi ngầm & hoàn trùng) kèm kiểm tra chéo đầy đủ trong `report/team/chi_so.md`.
- Gắn nhãn độc lập và khóa cột **Nhãn người 1** cho cả 20 ca lỗi theo nguyên nhân gốc trong `report/team/bang_loi.md` (4 Do người dùng · 5 Hệ thống · 4 Ngữ cảnh · 4 Giới hạn hệ thống · 3 Ngầm), đạt đồng thuận **20/20 (100%)** với N4.
- Rà soát toàn bộ nhánh của các thành viên và sửa các lỗi đồng bộ trước Gate 2a: bổ sung đủ nhãn `simulated` trong `bang_chi_phi.md` và `ho_so_launch_v0.md`; thay so sánh `0,37×` bằng chi phí cả hệ thống công bằng `5.865 đ = 0,49× (simulated)`; chuẩn hóa vai trò phụ trách sang vai trò LogiX-VN; chốt đề xuất **Go có điều kiện** kèm người phụ trách và ngày kiểm tra; bổ sung phần tính cỡ mẫu D1 và E1 vào `src/lab13.py`.

## 4. Bằng chứng

- PR #3 (`5442b03`) và nhánh `2A202603770_BuiNgocHung` (các commit cập nhật đồng bộ).
- File trực tiếp xây dựng/rà soát: `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/bang_chi_phi.md`, `src/lab13.py`, `TEAM.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:** Hỗ trợ đọc nhanh cấu trúc repo, trích xuất 20 ca lỗi từ file `.docx`, gợi ý cấu trúc bảng event tracking, soát lỗi nhãn `simulated`/từ cấm và kiểm tra tính nhất quán giữa các file hồ sơ.
- **Cách tự kiểm tra:**
  - Chạy script Python đọc trực tiếp `src/logix_requests.csv` và `src/logix_runs.csv` để kiểm chứng từng tử số/mẫu số của E1 (`994/1.200`, `48/177`, `51/1.200`, `39/982`) và tỉ lệ `ok` theo attempt của `quoc_te` (`30,0% → 11,4% → 2,2%`).
  - Tự đối chiếu từng ca trong 20 ca lỗi theo định nghĩa nguyên nhân gốc Google PAIR trước khi khóa nhãn và gửi N4.
  - Chạy lệnh kiểm tra tự động phát hiện dấu `?` trong `pilot_plan.yaml` và quét từ cấm theo quy tắc 5 trên toàn bộ thư mục `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ và đúng hạn toàn bộ phần việc được phân công cho vai N3 (CP3, đề xuất an toàn CP4, E1 + event tracking CP5, và rà soát đồng bộ trước Gate 2a).
- Bài học rút ra lớn nhất: khi đánh giá agent cần phân biệt rạch ròi số `simulated` với số đo thật, tính cả chi phí chuyển/làm lại của nhân viên khi so với baseline, và mọi chỉ số muốn theo dõi trong pilot đều phải ánh xạ được xuống event có `trace_id`.
