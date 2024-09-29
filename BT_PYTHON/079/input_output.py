def sap_xep_ds_tang(danhSachSo):
    for i in range(len(danhSachSo)):
        viTriNhoNhat = i
        for j in range(i + 1, len(danhSachSo)):
            if danhSachSo[j] < danhSachSo[viTriNhoNhat]:
                viTriNhoNhat = j
        danhSachSo[i], danhSachSo[viTriNhoNhat] = danhSachSo[viTriNhoNhat], danhSachSo[i]

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(float, danhSach))
        sap_xep_ds_tang(danhSachSo)
        print(*danhSachSo)
    except:
        print("Vui long nhap cac phan tu la so thuc!")