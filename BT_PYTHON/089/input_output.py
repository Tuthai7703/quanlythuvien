def ds_phan_tu_rieng(danhSach1, danhSach2):
    ptuRiengDS1 = [ptu for ptu in danhSach1 if ptu not in danhSach2]
    ptuRiengDS2 = [ptu for ptu in danhSach2 if ptu not in danhSach1]
    ptuRieng = ptuRiengDS1 + ptuRiengDS2
    return ptuRieng

danhSach1 = input().split()
danhSach2 = input().split()

ptuRieng = ds_phan_tu_rieng(danhSach1, danhSach2)
print(*ptuRieng)