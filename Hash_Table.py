class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str):
        hash_code = 0
        for char in string:
            hash_code += ord(char)
        return hash_code

    def add(self, key, value):
        hash_code = self.hash(key)
        if hash_code not in self.collection:
            self.collection[hash_code] = {}
        self.collection[hash_code][key] = value

    def remove(self, key):
        hash_code = self.hash(key)
        if hash_code in self.collection and key in self.collection[hash_code]:
            del self.collection[hash_code][key]

    def lookup(self, key):
        hash_code = self.hash(key)
        entry = self.collection.get(hash_code)
        if entry and key in entry:
            return entry[key]
        return None


ht = HashTable()
print(ht.hash('golf')) 
ht.add('golf', 'sport')
ht.add('read', 'book')
ht.add('dear', 'friend')
print(ht.lookup('golf')) 
ht.add('rose', 'flower')
print(ht.collection) 