# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: T100 · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công (gấp 16,28× hoá đơn token+tool 275 đ/yêu cầu); xem lại+làm lại là khoản lớn nhất (làm lại 51,8% tổng — simulated) | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | 1) Làm lại +51,8% → 6.787 đ · 2) Xem lại +40,7% → 6.292 đ · 3) Lương NV +23,1% → 5.506 đ (B1) | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | CPS 4.472 đ = 0,37× so với 12.000 đ; A4 (noi_dia+hang_nang)+cố định vẫn 4.599–5.784 đ (0,38–0,48×). `quoc_te` 22.515 đ = 1,88× — không đáng để trợ lý xử lý | Giả lập | Người viết code |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính 82,83% (994/1.200); dùng bỏ qua gợi ý 27,12% (48/177); an toàn mở lại 7 ngày 4,25% (51/1.200); phạm vi noi_dia+hang_nang tốt hơn (chính 92,26%, an toàn 3,97%) | Xong, có bằng chứng | Người gắn nhãn 1 |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 20/20; 5 ca khắc phục đủ 5 loại PAIR (ca 9, 7, 18, 4, 17) có event/ngưỡng và một vai trò phụ trách | Xong, có bằng chứng | Người gắn nhãn 2 |
| 6 · Pilot plan | Chia theo staff 20+20; n/arm=859; DE≈6,96; MDE 6 điểm (đánh đổi power ~0,64 ở 5 điểm); phạm vi noi_dia+hang_nang; ≥3 luật dừng; quyết định 2027-01-05 | Xong, có bằng chứng | Người gắn nhãn 2 (giữ hồ sơ) |
| 7 · Rủi ro kinh tế | Làm lại ×2 → +51,8% (6.787 đ, simulated); xem lại ×2 / 100% → CPS gần hoặc vượt 12.000 đ (B4, simulated); lương +25% → +23,1% | Giả lập | Người kiểm số |

**Đề xuất:** *(chưa chốt — chờ cả nhóm chọn một trong: Go · Go có điều kiện · No-go)*

- [ ] Go
- [ ] Go có điều kiện — điều kiện gợi ý (nếu nhóm chọn hướng này): (1) sửa khoá chống trùng / đối soát sổ cái (ca 7, 20) trước ngày bắt đầu — Kỹ sư trưởng agent; (2) Giám đốc vận hành ký chấp nhận MDE 6 điểm (power ~0,64 ở mức 5 điểm); (3) bật đủ event có `trace_id`, thay phút simulated bằng phút đo thật sau tuần 1 — PM trợ lý hoàn phí; (4) có kế hoạch giảm xem lại theo bậc vì xem lại 100% thì mất lợi thế (B4) — Trưởng nhóm CSKH
- [ ] No-go — việc phải làm để quay lại cổng: …
