def tach_danh_sach(danhSachSo):
    trungBinhCong = sum(danhSachSo) / len(danhSachSo)
    dsNhoHon = [so for so in danhSachSo if so < trungBinhCong]
    dsLonHon = [so for so in danhSachSo if so >= trungBinhCong]
    return trungBinhCong, dsNhoHon, dsLonHon

danhSach = input().split()

try:
    danhSachSo = list(map(float, danhSach))
    trungBinhCong, dsNhoHon, dsLonHon = tach_danh_sach(danhSachSo)
    print(trungBinhCong)
    print(*dsNhoHon)
    print(*dsLonHon)
except:
    print("Vui long nhap cac phan tu la so thuc!")