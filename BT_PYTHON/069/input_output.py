def tong_trung_binh_cac_so(s):
    dsCacTu = s.split()

    tong = 0
    dem = 0

    for tu in dsCacTu:
        if tu.isdigit():
            tong += int(tu)
            dem += 1
    if dem == 0:
        return 0, 0
    trungBinh = tong / dem
    return tong, trungBinh

s = input()
tong, trungBinh = tong_trung_binh_cac_so(s)
print(tong)
print(trungBinh)