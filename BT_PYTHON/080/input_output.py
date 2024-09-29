import math

def kt_so_nguyen_to(n):
    if n < 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ds_so_nguyen_to(danhSachso):
    dsSoNguyenTo = [so for so in danhSachso if kt_so_nguyen_to(so)]
    return dsSoNguyenTo

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        danhSachSo = list(map(int, danhSach))
        dsSoNguyenTo = ds_so_nguyen_to(danhSachSo)
        print(*dsSoNguyenTo)
    except:
        print("Vui long nhap phan tu la so nguyen!")