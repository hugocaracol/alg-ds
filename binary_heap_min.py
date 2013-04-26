
class BinaryHeapMin:
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
            # if parent elem > current elem then swap
            if self.heapList[p] > self.heapList[i]:
                self.heapList[p], self.heapList[i] = self.heapList[i], self.heapList[p]
            i = p
            p = self._findParent(i)
        
    def pop(self):
        if self.currentSize == 0:
            return None
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        if self.currentSize > 1:
            self._heapifyDown(1)
        return retval
        
    def _heapifyDown(self, i):
        minChild = self._findMinChild(i)
        while minChild <= self.currentSize:
            if self.heapList[minChild] < self.heapList[i]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild
            minChild = self._findMinChild(i)
            
    def _findMinChild(self, i):
        # if has just one child
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
    
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
    # testing against python's heapq
    import heapq
    from random import randrange
    
    print "BEGIN TESTING..."
    l = [randrange(20) for _ in range(5000)]
    bh = BinaryHeapMin()
    l_heapq = [] + l
    bh.heapify(l)
    heapq.heapify(l_heapq)
    assert bh.getList() == l_heapq
    print "   HEAPIFY [PASSED]"
    
    # POP
    while len(bh.getList()) > 0:
        bh.pop()
        heapq.heappop(l_heapq)
        assert bh.getList() == l_heapq
    print "   POP [PASSED]"
    
    # PUSH
    for i in range(1000):
        n = randrange(2000)
        bh.push(n)
        heapq.heappush(l_heapq, n)
        assert bh.getList() == l_heapq
    print "   PUSH [PASSED]"
    
    # PUSH & POP (random)
    for i in range(1000):
        method = randrange(2)
        if method == 0:
            # PUSH
            n = randrange(2000)
            bh.push(n)
            heapq.heappush(l_heapq, n)
            assert bh.getList() == l_heapq
        else:
            # POP
            if len(l) > 0:
                bh.pop()
                heapq.heappop(l_heapq)
                assert bh.getList() == l_heapq
    print "   PUSH & POP (random) [PASSED]"
    print "END TESTING."
    
test()
