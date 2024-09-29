def them_phan_tu(danhSach, n):
    ketQua = []
    for thuThu in range(0, len(danhSach), n):
        ketQua.extend(danhSach[thuThu:thuThu+n])
        ketQua.append('Kteam')
    ketQua.pop()
    return ketQua

danhSach = input().split()
if len(danhSach) == 0:
    print("Danh sach rong")
else:
    try:
        n = int(input())
        dsKetQua = them_phan_tu(danhSach, n)
        print(*dsKetQua)
    except:
        print("Dinh dang dau vao khong hop le!")