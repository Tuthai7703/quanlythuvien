def xoa_trung_lap(s):
    chuoiKetQua = ""
    for kyTu in s:
        if kyTu not in chuoiKetQua:
            chuoiKetQua += kyTu
    return chuoiKetQua
s = input()
print(xoa_trung_lap(s))