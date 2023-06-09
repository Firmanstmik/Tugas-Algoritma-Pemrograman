def binary_search(arr, kecil, besar, x):
    #proses dasar
    if besar >= kecil:
        tengah = (besar + kecil) // 2
        if arr[tengah] == x:
            return tengah
        elif arr[tengah] > x:
            return binary_search(arr, kecil, tengah-1, x)
        else:
            return binary_search(arr, tengah+1, besar, x)
    else:
        return -1

 #proses perbandingan
arr = [2,5,8,12,16,23,38,56,72,91,95,99]
x = 72

result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Angka = [2,5,8,12,16,23,38,56,72,91,95,99]")
    print("Element yang dicari (72) berada pada index", str(result))
else:
    print("Element tidak ditemukan")

 
 
