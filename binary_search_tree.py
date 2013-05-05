class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _isRoot(self, node):
        return self.root == node

    def treeIsEmpty(self):
        return self.root is None

    def put(self, k, val):
        if not self.treeIsEmpty():
            self._put(k, val, self.root)
        else:
            self.root = Node(k, val)

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.left)
            else:
                currentNode.left = Node(key, val, currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.right)
            else:
                currentNode.right = Node(key, val, currentNode)
        else:
            # updates val
            currentNode.val = val

    def __setitem__(self, k, val):
        self.put(k, val)

    def get(self, k):
        if self.treeIsEmpty():
            return None
        node = self._get(k, self.root)
        if node is not None:
            return node.val
        else:
            return None

    def _get(self, key, currentNode):
        if currentNode is None:
            return None
        else:
            if key < currentNode.key:
                return self._get(key, currentNode.left)
            elif key > currentNode.key:
                return self._get(key, currentNode.right)
            else:
                return currentNode

    def __getitem__(self, k):
        return self.get(k)

    def delete(self, k):
        # returns True if deleted, False otherwise
        if self.treeIsEmpty():
            return False
        result = self._delete(k, self.root)
        return result

    def _delete(self, k, currentNode):
        if k < currentNode.key:
            if currentNode.left is not None:
                return self._delete(k, currentNode.left)
            else:
                return False
        elif k > currentNode.key:
            if currentNode.right is not None:
                return self._delete(k, currentNode.right)
            else:
                return False
        else:
            # deletion
            if currentNode.isLeaf():
                # leaf
                if currentNode == self.root:
                    self.root = None
                else:
                    if k < currentNode.parent.key:
                        currentNode.parent.left = None
                    else:
                        currentNode.parent.right = None
                    currentNode.parent = None
            elif currentNode.hasLeftChild() and not currentNode.hasRightChild():
                # left child
                if self._isRoot(currentNode):
                    self.root = currentNode.left
                    currentNode.left.parent = None
                else:
                    if k < currentNode.parent.key:
                        currentNode.left.parent = currentNode.parent
                        currentNode.parent.left = currentNode.left
                    else:
                        currentNode.left.parent = currentNode.parent
                        currentNode.parent.right = currentNode.left
                        
            elif not currentNode.hasLeftChild() and currentNode.hasRightChild():
                # right child
                if self._isRoot(currentNode):
                    currentNode.right.parent = None
                    self.root = currentNode.right
                else:
                    if k < currentNode.parent.key:
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.left = currentNode.right
                    else:
                        currentNode.right.parent = currentNode.parent
                        currentNode.parent.right = currentNode.right
            else:
                # both children
                # search for the min node of the right branch
                # (we could also search for the max node of the left branch)
                minNode = currentNode.right.findMinChild()
                currentNode.updateContent(minNode)
                if minNode.hasRightChild():
                    if minNode == currentNode.right:
                        minNode.right.parent = currentNode
                        currentNode.right = minNode.right
                    else:
                        minNode.right.parent = minNode.parent
                        minNode.parent.left = minNode.right
                else:
                    # min node is leaf
                    if minNode == currentNode.right:
                        currentNode.right = None
                    else:
                        minNode.parent.left = None
        return True

    def __delitem__(self, k):
        self.delete(k)

    def checkTree(self):
        listKeys = []
        if self.root is not None:
            self._checkTree(self.root, listKeys)

        if listKeys != sorted(listKeys):
            print listKeys
            for k in listKeys:
                print str(k) + " = " + str(self.get(k))
                print "root: " + str(self.root.key)
                parent = self._get(k, self.root).parent
        return listKeys == sorted(list(set(listKeys)))

    def _checkTree(self, node, listKeys):
        if node.left is not None:
            self._checkTree(node.left, listKeys)
        if node.key in listKeys:
            print "key ja existe"
        listKeys.append(node.key)
        if node.right is not None:
            self._checkTree(node.right, listKeys)
        
    def traverse(self, node = None, child = ""):
        # inorder
        if node is None:
            return
        self.traverse(node.left, " left of " + str(node.key))
        print str(node.key) + child
        self.traverse(node.right, " right of " + str(node.key))


class Node:
    def __init__(self, key, val, parent = None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None
    
    def hasLeftChild(self):
        return self.left is not None

    def hasRightChild(self):
        return self.right is not None

    def isLeaf(self):
        return self.left is None and self.right is None

    def findMinChild(self, node = None):
        if node is None:
            node = self
        if node.left is None:
            return self
        else:
            return self.findMinChild(node.left)

    def updateContent(self, node):
        self.key = node.key
        self.val = node.val
        
def test():
    
    from random import randrange
    
    print "BEGIN TEST..."
    bst = BinarySearchTree()
    assert bst.checkTree()
    print "   CREATE [PASSED]"
    bst.delete(randrange(5000))
    print "   DELETE (empty tree) [PASSED]"
    
    # random put
    list_tree_k = []
    list_tree_v = []
    dict_tree = {}
    for _ in range(5000):
        k  = randrange(1000)
        # ASCII: 48-122
        v  = "".join([chr(randrange(48,122)) for _ in range(20)])
        list_tree_k.append(k)
        list_tree_v.append(v)
        dict_tree[k] = v
        bst.put(k, v)
    assert bst.checkTree()
    print "   PUT (" + str(len(list_tree_k)) + ") [PASSED]"
    
    for i in range(randrange(len(list_tree_k))):
        bst.delete(list_tree_k[i])
        if list_tree_k[i] in dict_tree:
            del dict_tree[list_tree_k[i]]
        assert bst.checkTree()
        if bst.treeIsEmpty():
            break
    bst = BinarySearchTree()
    bst.put(9999,'4765385476983bnb4')
    bst.delete(0)
    bst.delete(9999)
    bst.delete(0)
    print "   DELETE [PASSED]"

    # random put
    list_tree_k = []
    dict_tree = {}
    for _ in range(1000):
        k  = randrange(1000)
        # ASCII: 48-122
        v  = "".join([chr(randrange(48,122)) for _ in range(50)])
        list_tree_k.append(k)
        dict_tree[k] = v
        bst.put(k, v)

    # getting values
    for i in range(1000):
        assert bst.get(list_tree_k[i]) == dict_tree[list_tree_k[i]]
    print "   GET [PASSED]"
    print "END TEST."


#for i in range(50):
#    print "Test #" + str(i+1)
#    test()
