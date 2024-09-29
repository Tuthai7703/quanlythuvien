def digit_char_symbol(s):
    digits = ""
    chars = ""
    symbols = ""

    for c in s:
        if c.islower() or c.isupper():
            chars += c
        elif c.isdigit():
            digits += c
        else:
            symbols += c
    chuoiSapXep = digits + chars + symbols

    return len(digits), len(chars), len(symbols), chuoiSapXep
s = input()
slChuSo, slKyTu, slKyHieu, chuoiSapXep = digit_char_symbol(s)

print(slChuSo, slKyTu, slKyHieu, sep="\n")
print(chuoiSapXep)