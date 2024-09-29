def tu_dai_nhat(s):
    tuDaiNhat = ""
    dsCacTu = s.split()
    for tu in dsCacTu:
        if(len(tu) > len(tuDaiNhat)) or (len(tu) == len(tuDaiNhat) and tu < tuDaiNhat):
            tuDaiNhat = tu
    return tuDaiNhat
s = input()
print(tu_dai_nhat(s))
