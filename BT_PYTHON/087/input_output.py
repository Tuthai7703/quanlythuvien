def hona_doi_danh_sach(danhSach1, danhSach2):
    nuaDoDaiDS1 = len(danhSach1) // 2
    nuaDoDaiDS2 = len(danhSach2) // 2

    nuaDanhSach1 = danhSach1[nuaDoDaiDS1:]
    nuaDanhSach2 = danhSach2[nuaDoDaiDS2:]
    danhSach1 = danhSach1[:nuaDoDaiDS1] + nuaDanhSach2
    danhSach2 = danhSach2[:nuaDoDaiDS2] + nuaDanhSach1
    return danhSach1, danhSach2

danhSach1 = input().split()
danhSach2 = input().split()

dsHoanDoi1, dsHoanDoi2 = hona_doi_danh_sach(danhSach1, danhSach2)

print(*dsHoanDoi1)
print(*dsHoanDoi2)