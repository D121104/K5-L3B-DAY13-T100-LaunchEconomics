# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Bùi Ngọc Hùng (N3, đã khóa) · Người gắn nhãn 2: Trần Cảnh Hưng (N4) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Không có ca lệch nhãn. Hai bộ gắn theo nguyên nhân gốc (PAIR) và trùng 20/20. Các quy tắc phân biệt loại dễ lẫn (dùng chung khi gắn):

- Ca 6, 9: gốc là khách chọn/nhập sai → **Do người dùng**, không gắn Hệ thống dù trợ lý thiếu gợi ý (phần thiếu gợi ý nằm ở cột khắc phục).
- Ca 13: ngoài phạm vi → **Giới hạn hệ thống**, kể cả khi trợ lý xử lý giới hạn kém.
- Ca 8, 15: sai đã lộ (trích dẫn / nhân viên bắt được) → **Hệ thống**, không phải Ngầm.
- Ca 18: số tiền đúng chính sách, giả định “khách hiểu cách tính” không khớp → **Ngữ cảnh**.
- Ca 12: kết quả đúng nhưng chi phí bất thường kéo dài không ai thấy → **Ngầm**.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (hoặc `staff_review_decision` với lý do mã sai); cảnh báo khi > 2% yêu cầu/ngày | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn “đã hoàn” không có `refund_ledger_write` ket_qua=ok cùng `trace_id`; ngưỡng 0 ca | Chỉ báo “đã hoàn” khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo “đang xử lý” và `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` vì số tiền mà audit thấy đúng chính sách, theo tuần | Mẫu tin nhắn luôn ghi cách tính (vd. 30.000 đ × 50% = 15.000 đ) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason=`thieu_du_lieu`, theo loại yêu cầu | Giữ chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked` 100 đơn/tuần so bảng giá hiện hành; ngưỡng lệch 1% | Xoá bộ nhớ đệm khi có bảng giá mới; ghi `price_table_version` vào trace | Kế toán trưởng |
