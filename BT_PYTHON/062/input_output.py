def thay_the_nguyen_am(s):
    nguyenAm = "ueoaiUEOAI"
    tongNguyenAm = 0
    for c in nguyenAm:
        tongNguyenAm += s.count(c)
        s = s.replace(c, '$')
    return tongNguyenAm, s
s = input()
soLuongNguyenAm, chuoiKetQua = thay_the_nguyen_am(s)

print(soLuongNguyenAm)
print(chuoiKetQua)