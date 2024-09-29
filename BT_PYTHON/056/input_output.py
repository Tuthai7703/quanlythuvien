def chuoi_dan_xen(s1, s2):
    s2DaoNguoc = s2[::-1]
    maxDoDaiChuoi = max(len(s1), len(s2))
    chuoiDanXen = ""

    for i in range(maxDoDaiChuoi):
        if (i < len(s1)):
            chuoiDanXen += s1[i]
        if (i < len(s2)):
            chuoiDanXen += s2DaoNguoc[i]
    return chuoiDanXen

s1 = input()
s2 = input()

print(chuoi_dan_xen(s1, s2))