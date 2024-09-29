def list_va_list_binh_phuong(n):
    dsSoTuNhien = [i for i in range(n)]
    dsBinhPhuong = [i*i for i in range(n)]
    return dsSoTuNhien, dsBinhPhuong

try:
    n = int(input())
    if n < 0:
        print("Vui long nhap so tu nhien!")
    else:
        dsSoTuNhien, dsBinhPhuong = list_va_list_binh_phuong(n)
        print(*dsSoTuNhien)
        print(*dsBinhPhuong)
except:
    print("Dinh dang dau vao khong hop le!")