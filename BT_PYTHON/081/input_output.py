def ds_phan_tu_duy_nhat(danhSach):
    dsPtuDuyNhat = [ptu for ptu in danhSach if danhSach.count(ptu) == 1]
    return dsPtuDuyNhat

danhSach = input().split()
dsPtuDuyNhat = ds_phan_tu_duy_nhat(danhSach)
print(*dsPtuDuyNhat)