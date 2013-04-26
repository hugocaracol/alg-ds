class BinaryHeapMax:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def push(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self._heapifyUp(self.currentSize)

    def _findParent(self, i):
        # return 0 if element at i has no parent
        return i // 2

    def _heapifyUp(self, i):
        p = self._findParent(i)
        while p > 0:
            # if parent elem < current elem then swap
            if self.heapList[p] < self.heapList[i]:
                self.heapList[p], self.heapList[i] = self.heapList[i], self.heapList[p]
            i = p
            p = self._findParent(i)
    
    def pop(self):
        if self.currentSize == 0:
            return None
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        if self.currentSize > 1:
            self._heapifyDown(1)
        return retVal
    
    def _heapifyDown(self, i):
        maxChild = self._findMaxChild(i)
        while maxChild <= self.currentSize:
            if self.heapList[maxChild] < self.heapList[i]:
                return
            self.heapList[i], self.heapList[maxChild] = self.heapList[maxChild], self.heapList[i]
            i = maxChild
            maxChild = self._findMaxChild(i)
    
    def _findMaxChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] > self.heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def getList(self):
        return self.heapList[1:]

    def heapify(self, l):
        i = len(l) // 2
        self.currentSize = len(l)
        self.heapList = [0] + l[:]
        while(i > 0):
            self._heapifyDown(i)
            i -= 1


def test():
    
    import heapq
    from random import randrange
    
    print "BEGIN TESTING..."
    l = [randrange(1000) for _ in range(700)]
    l_heapq = [i*-1 for i in l]
    # HEAPIFY
    bh = BinaryHeapMax()
    bh.heapify(l)
    heapq.heapify(l_heapq)
    assert bh.getList() ==  [i*-1 for i in l_heapq]
    print "   HEAPIFY [PASSED]"
    
    # POP
    while len(bh.getList()) > 0:
        bh.pop()
        heapq.heappop(l_heapq)
        assert bh.getList() == [i*-1 for i in l_heapq]
    print "   POP [PASSED]"
    
    # PUSH
    for i in range(1000):
        n = randrange(2000)
        bh.push(n)
        heapq.heappush(l_heapq, n*-1)
        assert bh.getList() == [i*-1 for i in l_heapq]
    print "   PUSH [PASSED]"
    
    # PUSH & POP (random)
    for i in range(1000):
        method = randrange(2)
        if method == 0:
            # PUSH
            n = randrange(2000)
            bh.push(n)
            heapq.heappush(l_heapq, n*-1)
            assert bh.getList() == [i*-1 for i in l_heapq]
        else:
            # POP
            if len(bh.getList()) > 0:
                bh.pop()
                heapq.heappop(l_heapq)
                assert bh.getList() == [i*-1 for i in l_heapq]
    print "   PUSH & POP (random) [PASSED]"
    print "END TESTING."
    
    
test()
