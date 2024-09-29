def xoa_khoang_trang_thuong(s):
    s = s.strip()
    while " " in s:
        s = s.replace(" "," ")
    return s

def hien_thi_cau(s):
    dsCacCau = s.split('.')
    for cau in dsCacCau:
        cau = xoa_khoang_trang_thuong(cau)
        print(cau.title())

s = input()
hien_thi_cau(s)