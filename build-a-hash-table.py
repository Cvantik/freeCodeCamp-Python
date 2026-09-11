class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, unit: str):
        value = 0
        for u in unit:
            value += ord(u)
        return value
    
    def add (self, key, value):
        hash_value = self.hash(key)
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        self.collection[hash_value][key] = value
    
    def remove(self, key):
        hash_value = self.hash(key)
        try:
            self.collection[hash_value].pop(key)
        except KeyError:
            pass
    
    def lookup(self, key):
        hash_value = self.hash(key)
        try:
            return self.collection[hash_value][key]
        except KeyError:
            return None
        



print(HashTable().hash('golf'))
HashTable().add('dear', 'friend')
HashTable().add('read', 'book')
print(HashTable().lookup('golf'))
print(HashTable().lookup('dear'))

my_table = HashTable()

my_table.add('dear', 'friend')
my_table.add('read', 'book')

print(my_table.lookup('dear'))
print(my_table.lookup('read'))
my_table.remove('read')
print(my_table.lookup('read'))