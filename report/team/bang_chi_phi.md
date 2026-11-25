# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | | |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,28 lần** (4.472 ÷ 275).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại (simulated): 2.264.000 đ, chiếm 51,8%** tổng chi phí.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22x |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69x |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88x |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85x |

- Loại nào không đáng để trợ lý xử lý? **quoc_te** (CPS = 22.515 đ, gấp 1,88x baseline). Cho chạy lại tới 3 lần không giúp vì tỉ lệ thành công chỉ 27,3% — chi phí mỗi lần lỗi vẫn tích lũy mà không cải thiện đủ tỉ lệ thành công.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | 0,38x |
| Một nửa khối lượng (22.500) | 16.875 | 2.370 | 5.784 | 0,48x |

- Chi phí cố định có đổi kết luận không? **Không**. Dù ở khối lượng 22.500/tháng thì CPS+fixed vẫn là 5.784 đ (0,48x baseline), vẫn rẻ hơn nhân viên tự làm (12.000 đ).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)**. Tác động cộng tuyến tính — đúng bằng tổng hai thay đổi riêng lẻ (+5,6% + 40,7% ≈ +46,3%).
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Làm lại (+51,8%)** · 2. **Xem lại (+40,7%)** · 3. **Lương nhân viên (+23,1%)**

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 |
| 2 lần | 4.093.220 | 234 | 6.901.220 | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn nào rẻ nhất cho công ty? **2 lần** (chi phí cả hệ thống thấp nhất: 6.901.220 đ). Không trùng với giới hạn cho CPS thấp nhất — CPS thấp nhất là giới hạn **1 lần** (4.111 đ/việc), nhưng lại đẩy nhiều yêu cầu sang nhân viên (319 ca × 12.000 đ), khiến chi phí hệ thống cao hơn.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`): **11.743 đ (0,98x baseline)** với 9 phút làm lại, hoặc **12.415 đ (1,03x baseline)** với 15,3 phút — gần bằng hoặc vượt chi phí nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? **Pilot phải đo được tỉ lệ xem lại thực tế và thời gian làm lại trung bình** — nếu hai chỉ số này cao hơn giả lập, lợi thế kinh tế sẽ biến mất hoàn toàn.
