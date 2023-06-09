def binarySearch(arr, x):
    l = 0
    r = len(arr)
  # Loop to implement Binary Search
    while (l <= r):

        # Calculatiing mid
        m = l + ((r - l) // 2)

        res = (x == arr[m])

        # Check if x is present at mid
        if (res == 0):
            return m - 1

        # If x greater, ignore left half
        if (res > 0):
            l = m + 1

        # If x is smaller, ignore right half
        else:
            r = m - 1

    return -1


if __name__ == "__main__":

    arr = ["sekolah", "tinggi", "manajemen", "informatika", "dan", "komputer", "lombok"]
    indeks = arr.index("dan")
    x = "dan"
    result = binarySearch(arr,x)

    if (result == -1):
        print("Element not present")
    else:
        print("['sekolah', 'tinggi', 'manajemen', 'informatika', 'dan', 'komputer', 'lombok']")
        print("Element ditemukan di index",
              indeks)



