def kiem_tra_chuoi_con(s1, s2):
    if s2 in s1:
        print(s1.count(s2))
    else:
        print('Chuoi "{}" khong xuat hien trong chuoi "{}"'.format(s2, s1))

s1 = input()
s2 = input()

kiem_tra_chuoi_con(s1, s2)