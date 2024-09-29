def kiem_tra_ds_giam(danhSachSo):
    for soThuTu in range(len(danhSachSo) -1):
        if danhSachSo[soThuTu] < danhSachSo[soThuTu + 1]:
            return False
    return True

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(float, danhSach))
        ketQua = kiem_tra_ds_giam(danhSachSo)
        print(ketQua)
    except:
        print("Vui long nhap cac phan tu la so thuc!")
        