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

**Điều kiện trước và trong pilot:**

1. Trước ngày bắt đầu pilot (chốt quyết định 2027-01-05), Kỹ sư trưởng agent hoàn tất khoá chống hoàn trùng, đối soát `refund_ledger_write` và kiểm tra rollback; ngưỡng lỗi hoàn trùng là 0 ca.
2. Trước khi phân nhóm, Giám đốc vận hành ký chấp nhận thiết kế 20 nhân viên mỗi nhánh, MDE 6 điểm và power khoảng 0,64 nếu tác động thật chỉ là 5 điểm; nếu yêu cầu phát hiện 5 điểm thì phải thiết kế lại cỡ mẫu trước khi chạy.
3. PM trợ lý hoàn phí bật đủ event có `trace_id` và thay phút `simulated` bằng thời gian đo thực tế từ tuần đầu. Bắt đầu ở `noi_dia`; chỉ mở `hang_nang` theo rollout nếu CPS không quá 8.000 đ trong 2 tuần liên tiếp và không kích hoạt luật dừng an toàn.
4. Trưởng nhóm CSKH theo dõi tỷ lệ xem lại/bỏ qua hằng tuần và triển khai giảm xem lại theo bậc; nếu tỷ lệ bỏ qua gợi ý vượt 40% trong 1 tuần thì phỏng vấn 5 nhân viên trong 3 ngày, không chuyển bước rollout khi chưa xử lý nguyên nhân.
5. Giám đốc vận hành dừng pilot nếu tỷ lệ mở lại của nhóm trợ lý cao hơn đối chứng ít nhất 2 điểm phần trăm hoặc vượt 6%, hay có ca hoàn trùng theo luật dừng trong `pilot_plan.yaml`; không mở rộng khi chưa điều tra và khắc phục.

**Đề xuất: Go có điều kiện** — chạy pilot theo rollout đã định trong phạm vi `noi_dia` + `hang_nang`; không mở rộng nếu chưa đạt các điều kiện trên.
