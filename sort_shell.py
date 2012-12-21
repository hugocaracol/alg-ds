def shell_sort(l):
    n = len(l)
    gap = n / 2
    while gap > 0:
        i = 0
        while gap + i < n:
            temp = l[gap + i]
            j = i
            while temp < l[j] and j >= 0:
                l[j + gap] = l[j]
                j -= gap
            l[j + gap] = temp
            i += 1
        gap /= 2


l = [33, 32, 3, 45, 5, 6, 8, 0, 99, 72, 14]
shell_sort(l)
print l  # [0, 3, 5, 6, 8, 14, 32, 33, 45, 72, 99]
