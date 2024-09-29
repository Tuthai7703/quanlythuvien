def nhan_hai_danh_sach(danhSach1, danhSach2):
    dsKetQua = [so1*so2 for so1, so2 in zip(danhSach1, danhSach2[::-1])]
    return dsKetQua

danhSach1 = input().split()
danhSach2 = input().split()

if len(danhSach1) != len(danhSach2):
    print("Vui long nhap hai danh sach co cung kich thuoc!")
else:
    try:
        danhSach1 = list(map(float, danhSach1))
        danhSach2 = list(map(float, danhSach2))

        dsKetQua = nhan_hai_danh_sach(danhSach1, danhSach2)
        print(*dsKetQua)

    except:
        print("Vui long nhap cac phan tu la so thuc!") 