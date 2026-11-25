# Team

## Thông tin nhóm

- Tên nhóm: T100
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-T100-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/D121104/K5-L3B-DAY13-T100-LaunchEconomics` · nhánh `main` · *(cập nhật hash commit cuối trước khi nộp)*

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Đào Đức Duy | 2A202603900 | 26ai.duydd4@vinuni.edu.vn | D121104 | Người viết code (N1) |
| 2 | Phạm Minh Đức | 2A202603758 | 26ai.ducpm@vinuni.edu.vn | ducpham13 | Người kiểm số (N2, nhận code sau giải lao) |
| 3 | Bùi Ngọc Hùng | 2A202603770 | 26ai.hungbn@vinuni.edu.vn | Ngochung1772k4 | Người gắn nhãn 1 (N3) |
| 4 | Trần Cảnh Hưng | 2A202603759 | 26ai.hungtc@vinuni.edu.vn | danialtranz | Người gắn nhãn 2, kiêm giữ hồ sơ (N4) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/2A202603770_BuiNgocHung.md`.

## DaoDucDuy-2A202603900

### Phần việc phụ trách

- Người viết code (N1): cài đặt môi trường, triển khai nhiệm vụ A1–A4 và B1–B4 trong `src/lab13.py`; thiết lập phân công và thông tin nhóm.

### Đóng góp cụ thể

- Viết 3 hàm A1 đạt 3/3 phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`), xây dựng `mo_hinh()` và báo cáo A2–A4, B1–B4 trong `src/lab13.py`.
- Phân định vai trò trong nhóm và cập nhật bảng thành viên trong `TEAM.md`.

### Bằng chứng

- PR #1 (`c83d17a`), PR #5 (`d2d0559`), `src/lab13.py`, `TEAM.md`.

## PhamMinhDuc-2A202603758

### Phần việc phụ trách

- Người kiểm số (N2): kiểm tra dữ liệu, đối chiếu công thức/kết quả A1–A4 và B1–B4; phụ trách cỡ mẫu D1 và tiếp nhận code sau giờ giải lao.

### Đóng góp cụ thể

- Đối chiếu độc lập kết quả chạy `src/lab13.py` và điền đầy đủ bảng A1–A4, B1–B4, xếp hạng độ nhạy và phân tích B3–B4 trong `report/team/bang_chi_phi.md`.
- Xác nhận số liệu chi phí phục vụ phân tích rủi ro kinh tế (E2) và phạm vi pilot.

### Bằng chứng

- PR #2 (`cc51afa`), `report/team/bang_chi_phi.md`.

## BuiNgocHung-2A202603770

### Phần việc phụ trách

- Người gắn nhãn 1 (N3): đọc đề và quy tắc taxonomy PAIR; gắn nhãn độc lập 20 ca lỗi (CP3); phụ trách chỉ số an toàn, event tracking (CP5), đề xuất ngưỡng dừng an toàn (CP4), rà soát nhãn `simulated` và đồng bộ hồ sơ; tham gia duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Gắn nhãn độc lập và khóa bộ nhãn 20 ca lỗi (Nhãn người 1) theo nguyên nhân gốc trong `report/team/bang_loi.md` (đạt đồng thuận 20/20 với N4).
- Tính kiểm chứng 3 chỉ số E1 trên `src/logix_requests.csv` (toàn mẫu và phạm vi `noi_dia + hang_nang`), đề xuất thêm 2 chỉ số (dùng & an toàn), xây dựng bảng 11 event có `trace_id` kèm kiểm tra chéo trong `report/team/chi_so.md`.
- Đề xuất ngưỡng dừng an toàn dựa trên nền mở lại 4,25% (3,97% trong phạm vi) cho `pilot_plan.yaml`; rà soát nhãn `simulated`, hoàn thiện D1 trong `src/lab13.py`, đồng bộ `bang_chi_phi.md`, `ho_so_launch_v0.md` và viết báo cáo cá nhân `report/team/2A202603770_BuiNgocHung.md`.

### Bằng chứng

- PR #3 (`5442b03`), nhánh `2A202603770_BuiNgocHung`, `report/team/chi_so.md`, `report/team/bang_loi.md`, `report/team/2A202603770_BuiNgocHung.md`.

## TranCanhHung-2A202603759

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ (N4): gắn nhãn độc lập 20 ca lỗi (CP3); hoàn thiện bảng khắc phục 5 ca, `pilot_plan.yaml`, tổng hợp `ho_so_launch_v0.md` và ghi `phieu_cham.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, đối chiếu đạt đồng thuận 20/20 và hoàn thiện bảng khắc phục 5 ca (đủ 5 loại PAIR) trong `report/team/bang_loi.md`.
- Bổ sung mục E2 (rủi ro kinh tế) vào `report/team/chi_so.md`, hoàn thiện `report/team/pilot_plan.yaml` (không còn dấu `?`, đủ 3 luật dừng 4 vế) và tổng hợp `report/team/ho_so_launch_v0.md`.

### Bằng chứng

- PR #4 (`9917531`), `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/chi_so.md`.
