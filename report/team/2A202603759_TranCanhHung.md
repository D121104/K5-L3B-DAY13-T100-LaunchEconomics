# Báo cáo cá nhân — TranCanhHung-2A202603759

## 1. Thông tin thành viên

- Họ tên: Trần Cảnh Hưng
- MSSV: 2A202603759
- Email: 26ai.hungtc@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ (N4)

## 2. Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi ở CP3 (không trao đổi với N3 trước khi khóa nhãn).
- Giữ và cập nhật hồ sơ launch (`ho_so_launch_v0.md`) từ đầu buổi đến Gate 2a.
- Hoàn thiện `pilot_plan.yaml` (D1–D2, luật dừng, ngày quyết định); kiểm tra YAML đọc được bằng `yaml.safe_load`.
- Phối hợp tổng hợp `bang_loi.md` (bộ nhãn N4, quy tắc phân biệt, bảng khắc phục), rà soát `chi_so.md` và checklist nộp.
- Phụ trách chính `phieu_cham.md` khi nhóm làm hội đồng duyệt chéo.

## 3. Đóng góp cụ thể

- Gắn nhãn độc lập đủ 20 ca theo taxonomy PAIR (Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm); sau khi khóa nhãn, đối chiếu với N3 và ghi tỉ lệ đồng thuận **20/20 = 100%**.
- Viết quy tắc phân biệt các loại dễ lẫn (ca 6, 8, 9, 12, 13, 15, 18) và bảng khắc phục 5 ca (9, 7, 18, 4, 17) có event/ngưỡng và một vai trò phụ trách.
- Điền `pilot_plan.yaml`: chia theo staff 20+20, `n_per_arm = 859`, MDE 6 điểm (DE ≈ 6,96), phạm vi `noi_dia` + `hang_nang`, ≥3 luật dừng, `decision_date = 2027-01-05`; ghi rõ input `simulated`.
- Cập nhật bảy mục `ho_so_launch_v0.md` (chi phí, độ nhạy, so với baseline, chỉ số, lỗi, pilot, rủi ro kinh tế) và khung đề xuất Go / Go có điều kiện / No-go.
- Rà soát đủ file deliverable nhóm trước khi nộp; cập nhật vai trò và thông tin cá nhân trong `TEAM.md`.

## 4. Bằng chứng

| Sản phẩm / bằng chứng | Vai trò của tôi |
| --- | --- |
| `report/team/bang_loi.md` — cột «Nhãn người 2», đồng thuận 20/20, quy tắc phân biệt, bảng khắc phục | Người gắn nhãn 2 |
| `report/team/pilot_plan.yaml` — đầy đủ, không còn `?` ngoài chú thích | Người giữ hồ sơ (phụ trách chính) |
| `report/team/ho_so_launch_v0.md` — 7 mục + khung đề xuất Gate 2a | Người giữ hồ sơ |
| `report/team/chi_so.md` — kiểm tra chéo chỉ số ↔ event trước khi khóa hồ sơ | Người kiểm tra |
| Commit / nhánh: `9917531` trên `03759-hungtc` (merge PR #4) | Cập nhật báo cáo nhóm, nhãn lỗi, pilot, hồ sơ launch |
| GitHub: `danialtranz` | Tài khoản dùng để push / PR |

## 5. Công cụ AI đã dùng

- **Cursor (Composer / Agent):** hỗ trợ soạn và chỉnh `pilot_plan.yaml`, `ho_so_launch_v0.md`, `bang_loi.md`, báo cáo cá nhân; gợi ý cấu trúc luật dừng và cách ghi nhãn `simulated`.
- **Cách tự kiểm tra:**
  - Đối chiếu từng con số trong hồ sơ với `bang_chi_phi.md` / `chi_so.md` (ví dụ CPS 4.472 đ, đồng thuận 20/20, `n_per_arm` 859).
  - Chạy `python -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml', encoding='utf-8'))"` để xác nhận YAML hợp lệ.
  - Đọc lại 20 ca lỗi trong đề trước khi khóa bộ nhãn riêng; không sửa nhãn độc lập sau khi so sánh với N3.
  - Rà checklist trong `SUBMISSION.md` / `report/team/README.md` trước khi coi là đủ nộp.

## 6. Tự đánh giá

- Hoàn thành đúng vai N4: gắn nhãn độc lập, giữ hồ sơ launch, hoàn thiện pilot YAML và tổng hợp deliverable liên quan Gate 2a.
- Điểm mạnh: bám taxonomy PAIR và nhãn `simulated`; pilot có luật dừng cụ thể (ngưỡng, thời hạn, người có quyền dừng) và ngày quyết định rõ.
- Hạn chế: `phieu_cham.md` vẫn chờ buổi duyệt chéo nhóm n+1 mới điền điểm; khung đề xuất cuối trong `ho_so_launch_v0.md` cần cả nhóm chốt Go / Go có điều kiện / No-go trước khi nộp.
- Mức hoàn thành phần việc cá nhân: **đạt** theo phân công trong `phan_cong_cong_viec.md` và bốn vai bắt buộc trong `TEAM.md`.
