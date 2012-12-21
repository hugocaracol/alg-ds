class Hash:
    """
    A class for experimenting how to create hash tables.

    MyHash uses djb2 hash function for offset calculation
    and separate chaining for collision resolution.
    """
    def __init__(self, n_buckets):
        self.n_buckets = n_buckets
        self.hashTable = [None] * n_buckets
        self.fn_collisions = self.collisions_separate_chaining
        #open addressing
        #self.fn_collisions = self.collisions_linear_probing
        #self.fn_collisions = self.collisions_quadratic_probing

    def _hashthis(self, key):
        hash_djb2 = 5381
        for i in range(len(key)):
            hash_djb2 = ((hash_djb2 << 5) + hash_djb2) + ord(key[i])
        return hash_djb2 % self.n_buckets

    def set(self, key, value):
        offset = self._hashthis(key)
        return self.fn_collisions("SET", offset, key, value)

    def get(self, key):
        offset = self._hashthis(key)
        if self.hashTable[offset] is None:
            return None
        else:
            return self.fn_collisions("GET", offset, key)

    def _print(self):
        print "========= Table - BOF ========="
        for bucket in self.hashTable:
            print bucket
        print "========= Table - EOF ========="

    def collisions_separate_chaining(self, action, offset, key, value=None):
        if action == "SET":
            if self.hashTable[offset] is None:
                self.hashTable[offset] = [(key, value)]
            else:
                for i in range(len(self.hashTable[offset])):
                    if self.hashTable[offset][i][0] == key:
                        #updates the value of existing key
                        self.hashTable[offset][i] = (key, value)
                        return True
                self.hashTable[offset].append((key, value))
            return True
        elif action == "GET":
            for item in self.hashTable[offset]:
                if item[0] == key:
                    return item[1]
            return None
        return False

    def collisions_linear_probing(self, action, offset, key, value=None):
        if action == "SET":
            if self.hashTable[offset] is None:
                self.hashTable[offset] = (key, value)
                return True
            else:
                pos = (offset + 1) % self.n_buckets
                while pos != offset:
                    if self.hashTable[pos] is None:
                        self.hashTable[pos] = (key, value)
                        return True
                    else:
                        pos = (pos + 1) % self.n_buckets
                #couldn't find any available buckets
                return False
        elif action == "GET":
            pos = (offset + 1) % self.n_buckets
            while pos != offset:
                if self.hashTable[pos][0] == key:
                    return self.hashTable[pos][1]
                else:
                    pos = (pos + 1) % self.n_buckets
            return None
        return False

    def collisions_quadratic_probing(self, action, offset, key, value=None):
        if action == "SET":
            if self.hashTable[offset] is None:
                self.hashTable[offset] = (key, value)
                return True
            else:
                n_try = 1
                pos = (offset + n_try * n_try) % self.n_buckets
                while pos != offset:
                    if self.hashTable[pos] is None:
                        self.hashTable[pos] = (key, value)
                        return True
                    else:
                        n_try += 1
                        pos = (pos + n_try * n_try) % self.n_buckets
                #couldn't find any available buckets
                return False
        elif action == "GET":
            n_try = 1
            pos = (offset + n_try * n_try) % self.n_buckets

            while pos != offset:
                if self.hashTable[pos][0] == key:
                    return self.hashTable[pos][1]
                else:
                    n_try += 1
                    pos = (pos + n_try * n_try) % self.n_buckets
            return None


ht = Hash(10)  # 10 buckets
ht.set("name", "Hugo")
ht.set("age", 100)
print ht.get("name")  # Hugo
print ht.get("age")  # 100
