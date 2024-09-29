def phan_tu_lon(danhSachSo):
    giaTri = max(danhSachSo)
    soLuong = danhSachSo.count(giaTri)
    dsViTri = [vt for vt in range(0, len(danhSachSo)) if danhSachSo[vt] == giaTri]
    return giaTri, soLuong, dsViTri

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(float, danhSach))
        giaTri, soLuong, dsViTri = phan_tu_lon(danhSachSo)
        print(giaTri)
        print(soLuong)
        print(*dsViTri)
    except:
        print("Vui long nhap cac phan tu la so thuc!")