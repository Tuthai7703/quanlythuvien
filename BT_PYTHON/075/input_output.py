def ham_trung_binh(danhSach):
    tongDanhSach = sum(danhSach)
    soPhanTu = len(danhSach)
    trungBinhCong = tongDanhSach/soPhanTu
    return trungBinhCong

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(float, danhSach))
        trungBinhCong = ham_trung_binh(danhSachSo)
        print(trungBinhCong)
    except:
        print("Vui long nhap ket qua la so thuc!")