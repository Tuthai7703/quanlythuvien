def in_list(danhSach):
    for soThuTu, giaTri in enumerate(danhSach):
        print(soThuTu, giaTri)

danhSach = input().split()
in_list(danhSach)