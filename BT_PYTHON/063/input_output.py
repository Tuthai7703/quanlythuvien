def noi_chuoi(s):
    danhSachCacTu = s.split()
    chuoiKetQua = '-'.join(danhSachCacTu)
    return chuoiKetQua
s = input()
print(noi_chuoi(s))