def merge_sort(l, pini, pend, debug=False):
    if pini < pend:
        middle = (pini + pend) / 2

        if debug:
            print '1-invoking merge_sort with (' + str(pini) + ',' + \
                str(middle) + '):' + str(l[pini:middle + 1])
        merge_sort(l, pini, middle, debug)
        if debug:
            print '2-invoking merge_sort with (' + str(middle + 1) + \
                ',' + str(pend) + '):' + str(l[middle + 1:pend + 1])
        merge_sort(l, middle + 1, pend, debug)

        merge_list_sort(l, pini, middle, pend, debug)


def merge_list_sort(l, pini, middle, pend, debug=False):
    if debug:
        print 'invoking merge_list_sort with (' + str(pini) + ',' + \
            str(middle) + ',' + str(pend) + '):' + str(l[pini:pend + 1])
        print 'comparing: ' + str(l[pini:middle + 1]) + ' with ' + \
            str(l[middle + 1:pend + 1])

    new_list = []
    i = 0
    j = pini
    k = middle + 1
    while k <= pend and j <= middle:
        if l[k] < l[j]:
            new_list.append(l[k])
            k += 1
        else:
            new_list.append(l[j])
            j += 1

    while k <= pend:
        new_list.append(l[k])
        k += 1

    while j <= middle:
        new_list.append(l[j])
        j += 1

    if debug:
        print 'sorted: ' + str(new_list)

    #updates the l list with the values from the sorted list
    i = pini
    for item in new_list:
        l[i] = item
        i += 1

l = [6, 1, 3, 1, 8, 7, 24, 99]
print 'unsorted list -> ' + str(l)
merge_sort(l, 0, len(l) - 1, True)
print 'sorted list -> ' + str(l)
