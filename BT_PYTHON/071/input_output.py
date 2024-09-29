def dem_tu(s):
    dem = 0
    dsCacTu = s.split()

    for tu in dsCacTu:
        coKyTu = False
        coChuSo = False

        for kyTu in tu:
            if kyTu.isalpha():
                coKyTu = True
            if kyTu.isdigit():
                coChuSo = True

        if coKyTu and coChuSo:
            dem += 1
    return dem
s = input()
print(dem_tu(s))