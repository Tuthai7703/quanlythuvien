def chuoi_ket_qua(s):
    if len(s) < 3 or s[-3:] != "ing":
        s += "ing"
    else:
        s = s[:-3] + "ly"
    return s
s = input()
print(chuoi_ket_qua(s))