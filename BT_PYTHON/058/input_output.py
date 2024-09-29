def xoa_ki_tu(s):
    chuoiKetQua = ""
    doDaiChuoi = len(s)
    for i in range(doDaiChuoi):
        if i % 2 != doDaiChuoi % 2:
            chuoiKetQua += s[i]
    return chuoiKetQua
s = input()
print(xoa_ki_tu(s))