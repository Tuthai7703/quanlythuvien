def danh_sach_so_le(danhSachSo):
    danhSachSoLe = [so for so in danhSachSo if so % 2 != 0]
    return danhSachSoLe

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(int, danhSach))
        dsSoLe = danh_sach_so_le(danhSachSo)
        print(*dsSoLe)
    except:
        print("Vui long nhap cac phan tu so thu!")