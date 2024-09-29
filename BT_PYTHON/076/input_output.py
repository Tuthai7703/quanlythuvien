def so_nho_nhat(danhSachSo):
    soNhoNhat = danhSachSo[0]
    for so in danhSachSo:
        if so < soNhoNhat:
            soNhoNhat = so
    return soNhoNhat

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(float, danhSach))
        soNhoNhat = so_nho_nhat(danhSachSo)
        print(soNhoNhat)
    except:
        print("Dinh dang dau vao khong hop le!")