def chuoi_con_dao_nguoc(s, a, b):
    chuoiCon = s[a:b + 1]
    chuoiConDaoNguoc = chuoiCon[::-1]
    return chuoiConDaoNguoc

try:
    s = input()
    a, b = map(int, input().split())

    if a < 0 or b < 0:
        print("Vui long nhap a, b la so tu nhien!")
    elif a > b:
        print("Vui long nhap a <= b")
    elif a >= len(s) or b >= len(s):
        print("a, b lon hon do dai cua chuoi!")
    else:
        print(chuoi_con_dao_nguoc(s, a, b))

except:
    print("Dinh dang dau vao khong hop le!")