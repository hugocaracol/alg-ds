def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        temp = l[i]
        j = i - 1
        while j >= 0 and l[j] > temp:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = temp


l = [1, 32, 3, 45, 5, 6, 8, 0, 99, 72]
insertion_sort(l)
print l  # [0, 1, 3, 5, 6, 8, 32, 45, 72, 99]
