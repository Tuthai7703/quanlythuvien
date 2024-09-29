def xoa_khoang_trang_thua(s):
    s = s.strip()
    while " " in s:
        s = s.replace(" ", " ")
    return s
def hien_thi_cau(s):
    dsCacCau = s.split('.')
    for cau in dsCacCau:
        cau = xoa_khoang_trang_thua(cau)
        print(cau.title())

s = input()
print(hien_thi_cau(s))