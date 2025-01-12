class HashTable:
    def __init__(self):
        self.max = 10
        self.li = [[] for _ in range(self.max) ]
    
    def get_hashed(self, key):
        index = 0
        for i in str(key):
            index += ord(i)
        return index % self.max
    
    def __setitem__(self, key, val):
        index = self.get_hashed(key)
        for i in self.li[index]:
            if i[0] == key:
                i[1] = val
                return
        self.li[index].append((key, val))
    
    def __getitem__(self, key):
        index = self.get_hashed(key)
        for i in self.li[index]:
            if i[0] == key:
                return i[1]
        return 'Not found'
    
    def __delitem__(self, key):
        index = self.get_hashed(key)
        for i in self.li[index]:
            if i[0] == key:
                self.li[index].remove(i)
                return

    

h = HashTable()
h['Name'] = 'Sooraj'
h['Place'] = 'Pathanamthitta'
h['Age'] = 27
del h['Age']
print(h.li)
