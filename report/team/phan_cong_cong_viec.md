# Phân công công việc cho 4 thành viên

Điền tên thật vào N1–N4 sau khi thống nhất nhóm. Vai trò dưới đây bổ sung cho bốn vai bắt buộc trong `TEAM.md`; cập nhật cả `TEAM.md` để ghi nhận người viết code, người kiểm số, người gắn nhãn 1 và người gắn nhãn 2 kiêm giữ hồ sơ. Đổi người viết code sau giờ giải lao theo yêu cầu của lab.

## Vai trò và trách nhiệm chính

| Thành viên | Vai trò | Công việc chính |
| --- | --- | --- |
| N1 | Developer | Viết và chạy `src/lab13.py`; triển khai A1–A4 và B1–B4. Sau giờ giải lao bàn giao code cho N2 để ít nhất hai người tự tay tính/kiểm tra được mô hình chi phí. |
| N2 | Data Analyst / Người kiểm số | Kiểm tra dữ liệu và kết quả A, B; tính tay độc lập ít nhất một con số; phụ trách phân tích cỡ mẫu D1 và kiểm tra phương án pilot. |
| N3 | Error Analyst 1 / Người gắn nhãn 1 | Đọc đề và tiêu chí phân loại; gắn nhãn độc lập 20 ca lỗi ở CP3; phụ trách chỉ số an toàn và event tracking ở CP5. |
| N4 | Error Analyst 2 / Người gắn nhãn 2 kiêm giữ hồ sơ | Gắn nhãn độc lập 20 ca lỗi ở CP3; cập nhật hồ sơ launch từ đầu buổi; tổng hợp báo cáo, pilot YAML và phiếu chấm. |

## Phân công theo giai đoạn

| Giai đoạn | N1 | N2 | N3 | N4 |
| --- | --- | --- | --- | --- |
| Setup | Tạo môi trường Python, chạy thử script | Kiểm tra CSV, số dòng và schema | Đọc đề CP3, chuẩn bị quy tắc nhãn | Điền thông tin nhóm trong `TEAM.md`, mở hồ sơ launch |
| A: Chi phí | Code A1–A3; hỗ trợ A4 | Kiểm tra công thức/kết quả A1–A4, ghi bảng chi phí | Đọc trước 20 ca lỗi, ghi câu hỏi cần phân biệt | Điền dần `bang_chi_phi.md` và hồ sơ launch |
| B: Độ nhạy | Code và chạy kịch bản B1–B4 | Xếp hạng yếu tố, kiểm tra số và kết luận B3/B4 | Chuẩn bị taxonomy lỗi, không gắn nhãn trước khi tới CP3 | Cập nhật bảng chi phí và các rủi ro kinh tế ban đầu |
| C: Lỗi | Hoàn thiện/kiểm tra kết quả B còn lại | Kiểm tra đồng thuận sau khi hai bộ nhãn đã khóa | Gắn nhãn độc lập toàn bộ 20 ca; ghi bằng chứng | Gắn nhãn độc lập toàn bộ 20 ca; ghi bộ nhãn riêng |
| C: Đối chiếu | Hỗ trợ tính đồng thuận | Tính tỷ lệ trùng, cùng nhóm thống nhất ca khác nhau | Giải thích các nhãn của N3 sau khi khóa nhãn | Giải thích các nhãn của N4 sau khi khóa nhãn; ghi quy tắc phân biệt |
| D: Pilot | Kiểm tra tính nhất quán giữa giả định và code | Tính cỡ mẫu D1, đánh giá phân nhóm và thiết kế pilot | Đề xuất chỉ số/ngưỡng dừng an toàn | Hoàn thiện `pilot_plan.yaml`, kiểm tra YAML và placeholder |
| E: Chỉ số và hồ sơ | Hỗ trợ số liệu/chỉ số chính | Phân tích rủi ro kinh tế từ bảng độ nhạy | Định nghĩa event tracking và chỉ số an toàn | Tổng hợp `chi_so.md`, hoàn thiện `ho_so_launch_v0.md` |
| Gate 2a | Bảo vệ phần mô hình chi phí | Giải thích cỡ mẫu và số liệu | Duyệt chéo hồ sơ nhóm được phân công | Ghi `phieu_cham.md`, tổng hợp góp ý và checklist nộp |
| Nộp bài | Chạy lại `lab13.py`, kiểm tra thay đổi code | Đối chiếu số cuối, kiểm tra file deliverable | Rà nhãn `simulated` và nội dung chỉ số | Kiểm tra đủ file, YAML, `TEAM.md`, báo cáo cá nhân; phối hợp commit/push |

## Quy tắc phối hợp

- N3 và N4 phải tự gắn nhãn cả 20 ca lỗi một cách độc lập, không trao đổi và không xem bộ nhãn của nhau trước khi hoàn thành. Không sửa bộ nhãn độc lập sau khi đã so sánh.
- N1 và N2 cùng chịu trách nhiệm xác nhận số A/B; N2 phải tự kiểm tra độc lập, không chỉ chép kết quả từ chương trình.
- Sau giờ giải lao, N2 tiếp quản code để đổi người viết code như yêu cầu trong `TEAM.md`; N1 bàn giao cách chạy và logic thay đổi.
- Mỗi sản phẩm có một người phụ trách chính nhưng người phụ trách không thay thế việc cả nhóm hiểu và bảo vệ được kết quả.
- Số liệu lấy từ cột `_simulated` phải ghi nhãn `simulated`; không khẳng định thử nghiệm giả lập đã chứng minh tác động nhân quả.

## Theo dõi đầu ra

| Sản phẩm | Người phụ trách chính | Người kiểm tra |
| --- | --- | --- |
| `src/lab13.py` | N1, sau giải lao N2 | N2, N1 |
| `report/team/bang_chi_phi.md` | N2 | N1 |
| `report/team/bang_loi.md` | N3 và N4 | N1, N2 kiểm tra tính đầy đủ sau khi khóa nhãn |
| `report/team/pilot_plan.yaml` | N4 | N2 |
| `report/team/chi_so.md` | N3 và N2 | N4 |
| `report/team/ho_so_launch_v0.md` | N4 | Cả nhóm |
| `report/team/phieu_cham.md` | N4 | Thành viên được giao duyệt chéo |
| `TEAM.md`, `group_report.md`, báo cáo cá nhân | Mỗi người cập nhật phần mình; N4 kiểm tra đủ file | Cả nhóm |
