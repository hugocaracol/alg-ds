def shaker_sort(l):
    n = len(l)
    swap_count = 1
    while swap_count > 0:
        swap_count = 0
        # forward
        for i in range(n - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swap_count += 1
        # backwards
        for i in range(n - 1, 0, -1):
            if l[i] < l[i - 1]:
                l[i], l[i - 1] = l[i - 1], l[i]
                swap_count += 1
        n -= 1

l = [1, 32, 3, 45, 5, 6, 8, 0]
shaker_sort(l)
print l  # [0, 1, 3, 5, 6, 8, 32, 45]
