def chuoi_ket_qua(s1, s2):
    if len(s1) <= 5:
        s1 = s1*3
    if len(s2) <= 5:
        s2 = s2*3
    return s1 + s2
s1 = input()
s2 = input()

print(chuoi_ket_qua(s1, s2))