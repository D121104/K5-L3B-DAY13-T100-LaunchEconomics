# Phân tích repository Lab 13

## Tóm tắt

Đây là repository phục vụ một bài lab nhóm về kinh tế của trợ lý AI và thiết kế pilot cho công ty giả định LogiX-VN. Đây **không phải** ứng dụng hoàn phí có thể triển khai: không có dịch vụ web, API/model thật hay luồng vận hành production. Dữ liệu và giá trong bài là giả lập; mục tiêu là hoàn thiện một mô hình chi phí, đánh giá lỗi và đề xuất kế hoạch pilot có khả năng đưa ra quyết định.

## Cấu trúc và vai trò các thành phần

| Thành phần | Vai trò |
| --- | --- |
| `README.md` | Giới thiệu lab, bối cảnh, mục tiêu, lịch và cách bắt đầu. |
| `RULES.md` | Quy định dùng AI, liêm chính, dữ liệu, secret và nộp muộn. |
| `CHECKPOINTS.md` | Chỉ dẫn 5 nhiệm vụ A–E, sản phẩm và tiêu chí tự kiểm tra. |
| `RUBRIC.md`, `SUBMISSION.md`, `TEAM.md` | Chấm điểm, checklist nộp và thông tin/đóng góp thành viên. |
| `src/lab13.py` | Khung bài làm Python. Các hàm cốt lõi còn `NotImplementedError`; học viên phải hoàn thiện. |
| `src/lab13_starter.py` | Bản khởi đầu để đối chiếu, được yêu cầu giữ nguyên. |
| `src/logix_runs.csv` | Trace ở cấp lần chạy: token, tool, trạng thái, attempt và các ID liên kết. |
| `src/logix_requests.csv` | Kết quả và các thuộc tính ở cấp yêu cầu, gồm nhóm loại, review, thời gian giả lập và chỉ số kết quả. |
| `docs/` | Công thức, hướng dẫn chi tiết và tài liệu bài học gốc. |
| `report/team/` | Các biểu mẫu đầu ra cho chi phí, lỗi, pilot, chỉ số, hồ sơ launch và đánh giá chéo. Hầu hết là khung để nhóm điền, không phải kết quả đã hoàn thành. |

## Luồng làm bài

1. Cài Python 3.10+ và dependencies trong `src/requirements.txt`; chạy lệnh từ thư mục `src/` vì script đọc CSV bằng đường dẫn tương đối.
2. CP1/A: hoàn thiện ba công thức retry, kiểm tra ba assertion đã cho, xây mô hình chi phí từ mọi trace, phân tích theo loại yêu cầu và tính kịch bản có chi phí cố định.
3. CP2/B: chạy các kịch bản độ nhạy, gồm giá token/tool, thời gian nhân viên, review/rework và giới hạn retry; ghi kết quả vào `report/team/bang_chi_phi.md`.
4. CP3/C: hai thành viên gắn nhãn độc lập 20 trường hợp lỗi trong tài liệu đề bài; thống nhất cách phân loại và biện pháp giảm thiểu trong `bang_loi.md`.
5. CP4/D: tính cỡ mẫu, chọn đơn vị phân nhóm/đối chứng, xác định khả năng nhận diện tác động và điền `pilot_plan.yaml` cùng các luật dừng định lượng.
6. CP5/E: định nghĩa chỉ số/event, ghi rủi ro kinh tế, tổng hợp hồ sơ một trang, duyệt chéo; hoàn tất báo cáo nhóm/cá nhân và nộp theo `SUBMISSION.md`.

## Mô hình dữ liệu và phép tính

CSV có 1.624 lần chạy agent và 1.200 yêu cầu. Có 6 depot, 20 nhân viên; phân bố loại yêu cầu gồm 824 nội địa, 158 hàng nặng, 150 quốc tế và 68 đối tác. Kết quả có 978 `thanh_cong`, 74 `lam_lai`, 148 `chuyen_nhan_vien`. Trace có 1.052 lượt `ok`, 572 lượt `loi`. Đây là thống kê mô tả trên bộ dữ liệu giả lập, không phải bằng chứng hiệu quả ngoài thực tế.

Các mức giá được hard-code trong `lab13.py`: 26 đồng/1.000 token đầu vào, 130 đồng/1.000 token đầu ra, 15 đồng/lần gọi tool, 2.000 đồng/phút nhân viên và baseline 12.000 đồng/yêu cầu. Tài liệu dữ liệu nêu thêm chi phí cố định giả định 40 triệu đồng/tháng.

Nguyên tắc cốt lõi của mô hình: cộng token/tool trên **mọi lần chạy**, kể cả lần lỗi; cộng review và rework từ hai cột `_simulated`; chia tổng biến phí cho số yêu cầu `thanh_cong`. Các giá trị từ cột `_simulated` phải được gắn nhãn `simulated`. Khi so sánh với baseline, cần cẩn trọng với yêu cầu chuyển nhân viên: mẫu số “thành công” loại chúng ra nhưng chi phí vận hành tổng thể có thể cần tính cả lao động xử lý thay. Công thức và định nghĩa chi tiết nằm trong [du_lieu_va_cong_thuc.md](du_lieu_va_cong_thuc.md).

## Điểm cần lưu ý khi phát triển và đánh giá

- `lab13.py` hiện là bài tập chưa hoàn thiện. Chạy nguyên trạng sẽ dừng ở `NotImplementedError`; không nên xem đó là lỗi phụ thuộc thư viện.
- Các đường dẫn CSV là tương đối với thư mục làm việc. Chạy script từ repo root có thể không tìm thấy file; dùng `cd src` theo hướng dẫn.
- Đọc `logix_requests.csv` với `keep_default_na=False`, nếu không giá trị rỗng của `quyet_dinh_xem_lai` bị pandas đổi thành `NaN` và có thể làm sai logic so sánh.
- `runs` là cấp attempt, `reqs` là cấp request; phải tổng hợp đúng cấp và liên kết bằng ID khi lọc theo loại hoặc giới hạn số lần chạy. Không được đếm mỗi attempt như một yêu cầu độc lập.
- Cỡ mẫu theo yêu cầu không đồng nghĩa cỡ mẫu hiệu dụng khi phân nhóm theo nhân viên/depot. Tương quan trong cụm (ICC) làm giảm lượng thông tin; chỉ có 6 depot nên phân nhóm theo depot có thể thiếu cụm dù tổng request lớn.
- Bộ dữ liệu thử nghiệm không tự chứng minh tác động nhân quả. Cần nhóm đối chứng, phân bổ phù hợp và luật dừng định trước. Nên viết kết quả là số quan sát trong đợt chạy thử, không khẳng định trợ lý đã làm tăng chỉ số.
- Hồ sơ phải nêu phạm vi sử dụng hợp lý theo kinh tế, cả con số bất lợi, chủ sở hữu quyết định và điều kiện dừng; Gate 2a chỉ duyệt kế hoạch pilot.
- Quy tắc lab cấm dùng AI để bịa số, nhãn lỗi hoặc kết quả duyệt chéo. AI có thể hỗ trợ giải thích/code/soát lỗi, nhưng mọi kết quả phải tính hoặc kiểm chứng độc lập và nhóm phải giải thích được.

## Kiểm tra nhanh trước khi nộp

- `cd src && python3 lab13.py` chạy đến cuối và in ba phép thử A1 đạt.
- Không chỉnh sửa hai CSV hoặc `lab13_starter.py`; thay đổi bài làm ở `lab13.py`.
- `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn placeholder `?` và có tối thiểu ba luật dừng đủ điều kiện/ngưỡng, thời hạn, hành động và người có quyền dừng.
- Báo cáo có đủ file, đúng tên; mọi con số dựa trên cột `_simulated` có nhãn `simulated`; từng mục có chủ sở hữu là một vai trò.
- Không commit `.venv/`, `.env`, API key hoặc mật khẩu; không dùng từ “production” trong hồ sơ.
- Tham chiếu checklist đầy đủ và deadline trong [SUBMISSION.md](../SUBMISSION.md), tiêu chí chấm trong [RUBRIC.md](../RUBRIC.md).
