def list_ky_tu_dao_nguoc(s):
    dsKyTu = list(s)
    dsKyTuDaoNguoc = dsKyTu[::-1]
    return dsKyTuDaoNguoc

s = input()
dsKyTuDaoNguoc = list_ky_tu_dao_nguoc(s)
print(*dsKyTuDaoNguoc)