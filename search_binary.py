def binarysearch2(l, pinit, pend, value):
    if pinit > pend:
        return -1

    m_idx = (pend + pinit) / 2

    if l[m_idx] == value:
        return m_idx

    if value > l[m_idx]:
        return binarysearch2(l, m_idx + 1, pend, value)
    else:
        return binarysearch2(l, pinit, m_idx - 1, value)


l = [2, 5, 7, 10, 12]
# we search for the key in the entire array, so the left index=0 and
# the right index=(size of the array - 1)
print binarysearch2(l, 0, len(l) - 1, 10)  # matches on index 3
print binarysearch2(l, 0, len(l) - 1, 99)  # theres no match and -1 is returned
