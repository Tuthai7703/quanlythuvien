def nhan_ban_danh_sach(danhSach, n):
    soPhanTu = len(danhSach)
    soLanNhanBan = n // soPhanTu + 1
    dsNhanBan = danhSach*soLanNhanBan
    dsNPhanTu = dsNhanBan[:n]
    return dsNPhanTu

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        n = int(input())
        dsKetQua = nhan_ban_danh_sach(danhSach, n)
        print(*dsKetQua)

    except:
        print("Dinh dang dau vao khong hop le!")