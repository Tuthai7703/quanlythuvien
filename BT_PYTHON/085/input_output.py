def xoa_khoang_trang_thua(s):
    s = s.strip()
    while " " in s:
        s = s.replace(" ", " ")
    return s

def in_danh_sach(dsTen, dsQuocTich):
    dsTen = [xoa_khoang_trang_thua(ten) for ten in dsTen]
    dsQuocTich = [xoa_khoang_trang_thua(quocTich) for quocTich in dsQuocTich]
    for ten, quocTich in zip(dsTen, dsQuocTich):
        print(ten + " - " + quocTich)

dsTen = input().split(',')
dsQuocTich = input().split(',')

if len(dsTen) != len(dsQuocTich):
    print("Vui long nhap hai danh sach cung kich thuoc!")
else:
    in_danh_sach(dsTen, dsQuocTich)
    