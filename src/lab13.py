"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong khoảng (0, 1]')
    if k is None:
        return 1 / p
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong khoảng [0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    if thanh_cong == 0:
        return math.inf
    return so_lan_chay_ky_vong(p, k) / thanh_cong


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()

    if max_lan_chay is not None:
        if max_lan_chay < 1:
            raise ValueError('max_lan_chay phải là số nguyên dương')
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chi_phi_lan_chay_lai = (tien_token + tien_tool)[runs['attempt'] > 1].sum()
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong else math.inf

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=chi_phi_lan_chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=cps,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs) if len(reqs) else 0,
    )


def in_bang(ten, ket_qua):
    print(f'\n{ten}')
    for nhan, so in ket_qua:
        print(f'{nhan:36s} {so:>14,.2f}')


def chay_bao_cao(runs, reqs):
    goc = mo_hinh(runs, reqs)
    in_bang('A2 · Mô hình toàn bộ yêu cầu', goc.items())
    print(f"{'gấp so với hoá đơn / yêu cầu':36s} {goc['cps'] / goc['hoa_don_moi_yc']:>13,.2f}x")

    # A3: kết quả theo loại, gồm tỷ lệ thành công và số attempt trung bình.
    theo_loai = []
    for loai, nhom in reqs.groupby('loai', sort=True):
        ket_qua = mo_hinh(runs, nhom)
        theo_loai.append((loai, len(nhom), ket_qua['thanh_cong'] / len(nhom),
                          nhom['so_lan_chay'].mean(), ket_qua['cps'], ket_qua['cps'] / BASELINE))
    print('\nA3 · Theo loại: loại | requests | success | runs/request | CPS | so với baseline')
    for row in theo_loai:
        print(f'{row[0]:12s} {row[1]:5d} {row[2]:8.1%} {row[3]:13.2f} {row[4]:12,.0f} {row[5]:8.2f}x')

    # A4: phạm vi pilot nội địa + hàng nặng, với chi phí cố định ở hai mức tải.
    pilot_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pilot = mo_hinh(runs, pilot_reqs)
    # 45,000 is total monthly demand; use pilot-scope successes over the full sample.
    ty_le_thanh_cong = pilot['thanh_cong'] / len(reqs)
    print('\nA4 · Chi phí cố định cho noi_dia + hang_nang')
    for khoi_luong in (45000, 22500):
        so_viec_thang = khoi_luong * ty_le_thanh_cong
        co_dinh_moi_viec = 40_000_000 / so_viec_thang
        cps_bien_phi = pilot['cps']
        print(f'{khoi_luong:>6,d} requests/tháng: thành công={so_viec_thang:,.0f}, '
              f'fixed/request={co_dinh_moi_viec:,.0f}, CPS+fixed={cps_bien_phi + co_dinh_moi_viec:,.0f} '
              f'({(cps_bien_phi + co_dinh_moi_viec) / BASELINE:.2f}x baseline)')

    # B1: độ nhạy từng yếu tố so với CPS cơ sở.
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print('\nB1 · Độ nhạy (CPS và thay đổi so với A2)')
    ket_qua_b = {}
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        ket_qua_b[ten] = cps
        print(f'{ten:30s} {cps:10,.0f} {(cps / goc["cps"] - 1):+8.1%}')

    # B2: kịch bản kết hợp; mô hình chi phí cộng tuyến tính.
    b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Token và review cùng gấp đôi: {b2:,.0f} ({b2 / goc["cps"] - 1:+.1%})')
    print('Xếp hạng yếu tố: làm lại, xem lại, lương nhân viên.')

    # B3: tính cả chi phí nhân viên thay thế các yêu cầu chưa thành công.
    print('\nB3 · Chi phí cả hệ thống (trợ lý + nhân viên xử lý phần còn lại)')
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        chi_phi_he_thong = ket_qua['tong'] + khong_thanh_cong * BASELINE
        print(f'{gioi_han} lần: trợ lý={ket_qua["tong"]:,.0f}, chưa thành công={khong_thanh_cong}, '
              f'hệ thống={chi_phi_he_thong:,.0f}, CPS={ket_qua["cps"]:,.0f}')

    # B4: 100% review cho mọi yêu cầu trong phạm vi có ít nhất một attempt OK.
    eligible = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    eligible_ids = set(eligible['request_id'])
    ok_ids = set(runs.loc[(runs['request_id'].isin(eligible_ids)) & (runs['status'] == 'ok'), 'request_id'])
    so_review = len(ok_ids)
    so_lam_lai = int((eligible['ket_qua'] == 'lam_lai').sum())
    trace_chi_phi = mo_hinh(runs, eligible)['token'] + mo_hinh(runs, eligible)['tool']
    thanh_cong = int((eligible['ket_qua'] == 'thanh_cong').sum())
    print('\nB4 · Review 100% trong noi_dia + hang_nang')
    for phut_lam_lai in (9, 15.3):
        tong = trace_chi_phi + so_review * 5 * LUONG_PHUT + so_lam_lai * phut_lam_lai * LUONG_PHUT
        cps = tong / thanh_cong
        print(f'{phut_lam_lai:g} phút làm lại/ca: review={so_review}, làm lại={so_lam_lai}, '
              f'tổng={tong:,.0f}, CPS={cps:,.0f} ({cps / BASELINE:.2f}x baseline)')


# ---------- Nhiệm vụ D1 · Cỡ mẫu pilot và E1 · Ba chỉ số ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (kiểm định hai phía)."""
    nd = NormalDist()
    za = nd.inv_cdf(1 - alpha / 2)
    zb = nd.inv_cdf(power)
    pb = (p1 + p2) / 2
    num = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
    return math.ceil(num / (p2 - p1) ** 2)


def chay_d1_va_e1(reqs, p1=0.70, alpha=0.05, power=0.80, icc=0.02):
    print('\nD1 · Cỡ mẫu pilot (baseline=0,70; alpha=0,05; power=0,80; ICC=0,02)')
    n_req = co_mau(p1, p1 + 0.05, alpha, power)
    de_75 = 1 + (75 - 1) * icc
    n_staff_75 = math.ceil(n_req * de_75)
    so_nguoi_moi_nhom = math.ceil(n_staff_75 / 75)
    max_20_staff = int(20 / icc)
    max_6_depot = int(6 / icc)
    n_6pp = co_mau(p1, p1 + 0.06, alpha, power)
    # 20*m / (1 + (m - 1)*icc) >= n_6pp  =>  m*(20 - n_6pp*icc) >= n_6pp*(1 - icc)
    m_min_6pp = math.ceil(n_6pp * (1 - icc) / (20 - n_6pp * icc))
    de_6pp = 1 + (m_min_6pp - 1) * icc

    print(f'a) Theo yêu cầu (+5 điểm): {n_req:,d} yêu cầu/nhóm')
    print(f'b) Theo nhân viên (m=75): DE={de_75:.2f}, n={n_staff_75:,d}/nhóm -> {so_nguoi_moi_nhom} người/nhóm (tổng {2 * so_nguoi_moi_nhom} > 40: không đủ)')
    print(f'c) 20 nhân viên/nhóm: n_hiệu_dụng tối đa = {max_20_staff:,d} < {n_req:,d} (không đạt +5 điểm)')
    print(f'd) 6 depot/nhóm: n_hiệu_dụng tối đa = {max_6_depot:,d} (không đạt; chỉ 6 cụm < 20)')
    print(f'e) Mức chênh 6 điểm (n={n_6pp:,d}/nhóm), 20 nhân viên/nhóm: m >= {m_min_6pp} yêu cầu/người (DE={de_6pp:.2f})')

    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        es_5pp = proportion_effectsize(p1 + 0.05, p1)
        pwr_5pp = NormalIndPower().power(es_5pp, nobs1=n_6pp, alpha=alpha, ratio=1.0)
        print(f'   Power thực nếu chọn n={n_6pp} mà chênh thật chỉ 5 điểm: {pwr_5pp:.2f}')
    except ImportError:
        pass

    print('\nE1 · Ba chỉ số tính thử trên dữ liệu chạy thử (không đối chứng)')
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    scope_reqs = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    an_toan_scope = (scope_reqs['mo_lai_trong_7_ngay'] == 1).mean()
    print(f'Chính (24h & không mở lại 7 ngày): {chinh:.2%}')
    print(f'Dùng (bỏ qua gợi ý sua+bo):        {bo_qua:.2%}')
    print(f'An toàn (mở lại trong 7 ngày):     {an_toan:.2%} (phạm vi noi_dia+hang_nang: {an_toan_scope:.2%})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    chay_bao_cao(runs, reqs)
    chay_d1_va_e1(reqs)
