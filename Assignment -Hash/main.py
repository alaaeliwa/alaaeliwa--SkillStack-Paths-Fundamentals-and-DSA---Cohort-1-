class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity  
        self.size = 0                     
        self.table = [None] * self.capacity  
        self.load_factor_threshold = 0.7

    def _hash(self, key):
        return hash(key) % self.capacity

    def _probe(self, key, i):
        return (self._hash(key) + i ** 2) % self.capacity

    def _rehash(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for item in old_table:
            if item is not None and item != "DELETED":
                self.insert(*item)

    def insert(self, key, value):
        if self.size / self.capacity >= self.load_factor_threshold:
            self._rehash()

        i = 0
        while i < self.capacity:
            idx = self._probe(key, i)
            if self.table[idx] is None or self.table[idx] == "DELETED":
                self.table[idx] = (key, value)
                self.size += 1
                return
            elif self.table[idx][0] == key:
                # Update existing key
                self.table[idx] = (key, value)
                return
            i += 1
        raise Exception("HashTable is full, cannot insert key!")

    def search(self, key):
        i = 0
        while i < self.capacity:
            idx = self._probe(key, i)
            if self.table[idx] is None:
                return None
            elif self.table[idx] != "DELETED" and self.table[idx][0] == key:
                return self.table[idx][1]
            i += 1
        return None

    def delete(self, key):
        i = 0
        while i < self.capacity:
            idx = self._probe(key, i)
            if self.table[idx] is None:
                return False
            elif self.table[idx] != "DELETED" and self.table[idx][0] == key:
                self.table[idx] = "DELETED"
                self.size -= 1
                return True
            i += 1
        return False

    def __str__(self):
        return str([item for item in self.table])


# Example usage:
ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("orange", 30)

print("Search apple:", ht.search("apple"))   # 10
print("Search banana:", ht.search("banana")) # 20

ht.delete("banana")
print("Search banana after deletion:", ht.search("banana")) # None

ht.insert("grape", 40)
ht.insert("melon", 50)
ht.insert("kiwi", 60)
ht.insert("pear", 70)
ht.insert("peach", 80)

print(ht)
