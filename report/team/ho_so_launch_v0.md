# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: T100 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công (`simulated`), gấp 16,28× hoá đơn token+tool 274,7 đ/yêu cầu (đo từ trace); làm lại chiếm 51,8% và xem lại 40,7% (`simulated`) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1) Làm lại +51,8% → 6.787 đ · 2) Xem lại +40,7% → 6.292 đ · 3) Lương NV +23,1% → 5.506 đ (B1, `simulated`) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ (gồm 222 ca chuyển/làm lại, `simulated`); phạm vi `noi_dia`+`hang_nang` + cố định 40 tr/tháng = 4.599 đ (0,38×) ở 45.000 yc/tháng và 5.784 đ (0,48×) ở 22.500 yc/tháng (`simulated`); loại `quoc_te` (22.515 đ = 1,88×) và `doi_tac` (10.215 đ = 0,85×) | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (không đối chứng): chính 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 7 ngày 4,25% (51/1.200). Phạm vi `noi_dia`+`hang_nang`: chính 92,26%, mở lại 3,97%. Đủ 11 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 20/20 (100%); bảng khắc phục 5 ca đủ 5 loại PAIR (ca 9, 7, 18, 4, 17) có cách phát hiện đo được và 1 vai trò phụ trách | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên 20+20 (phân tầng depot); n/nhánh = 859, DE = 6,96, MDE 6 điểm (đánh đổi: power ~0,64 ở mức 5 điểm); phạm vi `noi_dia`+`hang_nang`; 3 luật dừng đủ 4 vế; ngày quyết định 2027-01-05 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ (+51,8%, `simulated`); xem lại 100% `noi_dia`+`hang_nang` → 11.743–12.415 đ (0,98–1,03×, mất lợi thế, B4, `simulated`); lương +25% → 5.506 đ (+23,1%, `simulated`); khối lượng giảm nửa làm cố định tăng lên 2.370 đ/việc | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** *(cho kế hoạch pilot phạm vi `noi_dia` + `hang_nang`, giới hạn tối đa 2 lần chạy — chi phí hệ thống thấp nhất 6.901.220 đ, `simulated`)*

- **Điều kiện 1 (An toàn sổ cái & chống hoàn trùng):** Hoàn tất khoá chống trùng (`idempotency_key`) và đối soát tự động sổ cái 0 ca lệch (ca 7, 20); xóa cache bảng giá cũ kèm `price_table_version` (ca 17) — **Người phụ trách:** Kỹ sư trưởng agent — **Ngày kiểm tra:** `2026-11-30` (trước khi bật rollout 0,10).
- **Điều kiện 2 (Chấp nhận đánh đổi cỡ mẫu & luật dừng):** Ký chấp nhận đánh đổi MDE 6 điểm (power ~0,64 nếu tác động thật chỉ 5 điểm) và phê duyệt 3 luật dừng viết trước cùng cơ chế tắt trong 30 phút — **Người phụ trách:** Giám đốc vận hành LogiX-VN — **Ngày kiểm tra:** `2026-11-30`.
- **Điều kiện 3 (Đo dữ liệu thật thay `simulated`):** Bật đủ 11 event có `trace_id` (đặc biệt `staff_review_decision`, `staff_rework_completed`, `audit_sample_checked`) và thay toàn bộ phút `simulated` bằng phút đo thực tế để tính lại CPS — **Người phụ trách:** PM trợ lý hoàn phí — **Ngày kiểm tra:** `2026-12-08` (cuối tuần 1).
- **Điều kiện 4 (Lộ trình giảm tỉ lệ xem lại):** Áp dụng giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo < 15%` để tránh kịch bản xem lại 100% làm CPS tiệm cận/vượt 12.000 đ (B4) — **Người phụ trách:** Trưởng nhóm CSKH — **Ngày kiểm tra:** `2026-12-15` (cuối bước rollout 0,25).
