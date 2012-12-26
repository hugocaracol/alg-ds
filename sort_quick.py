def quicksort(l, pini, pend, debug=False):

    n = pend - pini + 1
    if n <= 1:
        if debug:
            print 'Sorted ' + str(l[pini:pend + 1])
        return
    if n == 2:
        if l[pini] > l[pend]:
            l[pend], l[pini] = l[pini], l[pend]
        if debug:
            print 'Sorted ' + str(l[pini:pend + 1])
        return
    m = (pend + pini) / 2  # pivot
    # sort 3 elements
    if l[pini] > l[m]:
        l[pini], l[m] = l[m], l[pini]
    if l[m] > l[pend]:
        l[m], l[pend] = l[pend], l[m]
    if l[pini] > l[m]:
        l[pini], l[m] = l[m], l[pini]
    if n == 3:
        if debug:
            print 'Sorted ' + str(l[pini:pend + 1])
        return

    ind_i = pini
    ind_j = pend

    m = partitioning(l, pini, m, pend, debug)
    if debug:
        print 'Call quicksort with Left sub-list: ' + str(l[pini: m])
    quicksort(l, pini, m - 1, debug)
    if debug:
        print 'Call quicksort with Right sub-list: ' + str(l[m + 1:pend + 1])
    quicksort(l, m + 1, pend, debug)


def partitioning(l, pini, m, pend, debug=False):

    if debug:
        print 'Partitioning: ' + str(l[pini:pend + 1]) + \
            ' with pivot l[' + str(m) + ']=' + str(l[m])

    while True:
        i = pini
        while l[i] <= l[m] and i < m:
            i += 1
        j = pend
        while l[m] < l[j] and j > m:
            j -= 1
        if i == m and j == m:
            if debug:
                print 'Finished partitioning ' + str(l[pini:pend + 1])
            return m
        if i != m and j != m:
            l[i], l[j] = l[j], l[i]
        elif i == m:  # 1st half is sorted
            if debug:
                print '1st half (' + str(l[pini:m]) + ') is below pivot. ' + \
                    'Moving pivot to index ' + str(j)
            l[m], l[j] = l[j], l[m]
            m = j
            if debug:
                print 'Updated list ' + str(l)
        elif j == m:  # 2nd half is sorted
            if debug:
                print '2nd half (' + str(l[m + 1:pend + 1]) + ')is above ' + \
                    'pivot. Moving pivot to index ' + str(i)
            l[m], l[i] = l[i], l[m]
            m = i
            if debug:
                print 'Updated list ' + str(l)


l = [7, 2, 8, 3, 6, 4, 1]
print 'unsorted: ' + str(l)
quicksort(l, 0, len(l) - 1, True)
print 'sorted: ' + str(l)
