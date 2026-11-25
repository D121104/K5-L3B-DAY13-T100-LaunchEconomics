# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **82,83%** (994/1.200); trong phạm vi `noi_dia + hang_nang` là **92,26%** (906/982) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` (41) hoặc `bo` (7), chia số yêu cầu được xem lại (`duoc_xem_lai == 1`) | Chỉ số trong đợt chạy thử là **27,12%** (48/177); trong phạm vi `noi_dia + hang_nang` là **21,09%** (27/128) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là **4,25%** (51/1.200); trong phạm vi `noi_dia + hang_nang` là **3,97%** (39/982) |
| Dùng (tự đề xuất) | Tỉ lệ kích hoạt trợ lý trên nhóm can thiệp | Số yêu cầu thuộc nhóm can thiệp có ít nhất 1 event `agent_suggestion_shown`, chia tổng số yêu cầu trong phạm vi pilot của nhóm can thiệp | Không cần tính |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (và số ca hoàn trùng trên sổ cái) | Số đơn lệch số tiền đúng (hoặc có >1 lệnh ghi sổ cái `ok` cùng `request_id`), chia tổng số đơn kiểm tra mẫu (100 đơn/tuần) — nhằm phát hiện lỗi ngầm | Không cần tính |

> **Lưu ý diễn giải:** Mọi số liệu trên là kết quả quan sát **trong đợt chạy thử** (không có nhóm đối chứng), **không** kết luận trợ lý đã nâng chỉ số chính từ mức baseline 70% hay làm giảm lỗi.

## Danh sách event

Tất cả event đều gắn `trace_id` (kèm `request_id`) để nối trực tiếp với trace chạy agent trong giai đoạn pilot.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống tiếp nhận yêu cầu | `request_id`, `loai`, `so_tien_vnd`, `depot`, `staff_id`, `arm` (`treatment`/`control`), `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `input_validation_failed` | Hệ thống tiếp nhận / trợ lý | `request_id`, `error_code` (`sai_ma_van_don`/`thieu_so_tk`/`sai_danh_muc`), `input_type`, `trace_id` | Khi đầu vào của khách không hợp lệ (bắt lỗi do người dùng như ca 1, 9) |
| `agent_run_completed` | Trợ lý hoàn phí | `request_id`, `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status` (`ok`/`loi`), `price_table_version`, `trace_id` | Sau mỗi lần chạy của trợ lý, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện CSKH | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id` | Khi gợi ý của trợ lý hiện trên màn hình nhân viên |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc_te`, `trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý (thay `phut_xem_lai_simulated`) |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `staff_id`, `phut_lam_lai_thuc_te`, `ly_do_lam_lai`, `trace_id` | Khi nhân viên hoàn tất làm lại yêu cầu bị sai (thay `phut_lam_lai_simulated`) |
| `handoff_to_staff` | Trợ lý hoàn phí | `request_id`, `reason` (`thieu_du_lieu`/`vuot_max_lan_chay`/`ngoai_pham_vi`/`loi_he_thong`), `tom_tat`, `trace_id` | Khi trợ lý chuyển ca sang nhân viên xử lý |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien_vnd`, `ket_qua` (`ok`/`fail`/`duplicate_blocked`), `trace_id` | Khi ghi nhận lệnh hoàn tiền vào sổ cái |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `closed_within_24h`, `trace_id` | Khi yêu cầu hoàn phí được đóng |
| `ticket_reopened` | Khách hàng / CSKH | `request_id`, `reopened_at`, `within_7d`, `reopen_reason`, `trace_id` | Khi yêu cầu bị mở lại sau khi đã đóng |
| `audit_sample_checked` | Bộ phận kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_tien` (`true`/`false`), `trace_id` | Khi kiểm tra mẫu định kỳ 100 đơn/tuần |

**Kiểm tra chéo (ánh xạ chỉ số ↔ event):**

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** ghép `refund_request_created` (`created_at`, `arm`) với `ticket_closed` (`closed_at - created_at <= 24h`) và kiểm tra không có `ticket_reopened` với `within_7d == true` trong vòng 7 ngày theo `request_id`/`trace_id`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** từ `staff_review_decision`, đếm số ca có `quyet_dinh` là `sua` hoặc `bo` chia tổng số ca phát sinh `staff_review_decision`.
- **Chỉ số dùng (tự đề xuất) — Tỉ lệ kích hoạt trợ lý trên nhóm can thiệp:** đếm số `request_id` duy nhất có `agent_suggestion_shown` chia tổng số `request_id` có `arm == "treatment"` và `loai` thuộc phạm vi pilot từ `refund_request_created`.
- **Chỉ số an toàn — Tỉ lệ lỗi lọt đến khách (mở lại trong 7 ngày):** đếm số `request_id` có `ticket_reopened` (`within_7d == true`) chia tổng số `request_id` từ `refund_request_created` theo từng `arm`.
- **Chỉ số an toàn (tự đề xuất) — Tỉ lệ đơn hoàn sai tiền & hoàn trùng:** từ `audit_sample_checked`, đếm số ca `lech_tien == true` chia tổng số ca được kiểm tra mẫu hằng tuần; đồng thời đối soát `refund_ledger_write` (số `request_id` có >1 bản ghi `ket_qua == "ok"`, ngưỡng dừng = 0 ca).
- **Theo dõi chi phí thực tế trong pilot (thay thế số `simulated`):** kết hợp `agent_run_completed` (`tokens_in`, `tokens_out`, `tool_calls`), `staff_review_decision` (`phut_xem_lai_thuc_te`) và `staff_rework_completed` (`phut_lam_lai_thuc_te`).
- **Phát hiện lỗi đầu vào từ người dùng (khớp ca 9 trong `bang_loi.md`):** đếm `input_validation_failed` theo ngày chia tổng `refund_request_created` (cảnh báo khi > 2%).

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy trong `report/team/bang_chi_phi.md`. Con số phụ thuộc cột `_simulated` gắn nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | CPS lên 6.787 đ (+51,8%) — `simulated` (B1) | Tỉ lệ làm lại theo tuần (event `staff_rework_completed`) tăng rõ so với đợt chạy thử | Thu hẹp pilot về `noi_dia`; rà 20 trace làm lại/tuần | PM trợ lý hoàn phí |
| Tỉ lệ xem lại tăng gấp đôi / phải xem lại 100% kéo dài | Xem lại ×2 → CPS 6.292 đ (+40,7%) `simulated`; xem lại 100% `noi_dia`+`hang_nang` → 11.743–12.415 đ ≈ 0,98–1,03× baseline 12.000 đ (B4, `simulated`) | % yêu cầu được xem lại còn > 50% cuối bước rollout 0,25; hoặc `staff_review_decision` tỉ lệ `sua`+`bo` không giảm | Giảm xem lại theo bậc khi tỉ lệ sửa+bỏ < 15%; không mở rộng bước rollout | Trưởng nhóm CSKH |
| Chi phí biến đổi cao khi rollout / fixed cost phân bổ lớn ở tải thấp | Ngưỡng CPS biến đổi > 8.000 đ trong 2 tuần; fixed 40 triệu/tháng được báo riêng vì 4/10/20 người treatment tương ứng khoảng 15.300/8.200/5.800 đ tổng mỗi việc (`simulated`) | CPS biến đổi hằng tuần; số việc thành công/tháng; tỉ lệ đạt rollout 4 → 10 → 20 | Nếu CPS biến đổi vượt ngưỡng, thu hẹp `noi_dia`, giới hạn 2 lần chạy; nếu sản lượng thấp, không mở rộng và đánh giá riêng chi phí cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% | CPS lên 5.506 đ (+23,1%) — một phần `simulated` (B1) | Chi phí phút nhân viên thực tế > 2.000 đ/phút trong 2 tuần | Giới hạn tối đa 2 lần chạy; ưu tiên `noi_dia` | PM trợ lý hoàn phí |
