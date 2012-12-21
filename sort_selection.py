def sel_sort(l):
    n = len(l)
    for i in range(0, n - 1):
        indMin = i
        for j in range(i + 1, n):
            if l[j] < l[indMin]:
                indMin = j
        if indMin != i:
            l[i], l[indMin] = l[indMin], l[i]


l = [10, 45, 4, 5, 2, 10, 1]
sel_sort(l)
print l  # [1, 2, 4, 5, 10, 10, 45]
