class HashMap:

    def __init__(self, capacity=32):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash_function(self, key):
        key_string = str(key)
        hash_result = 0
        for c in key_string:
            """multiply with prime number (31) to avoid collision"""
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        return hash_result

    def __len__(self):
        return self.size

    def __contains__(self, key):
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def put(self, key, value):
        """Insert or update the key with value."""
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        """Retrieve value for key or -1 if not found."""
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key):
        """Remove key from map. Returns -1 if not found."""
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        return -1

    def keys(self):
        """Return all keys in the map."""
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self):
        """Return all values in the map."""
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self):
        """Return all key-value pairs in the map."""
        return [(k, v) for bucket in self.buckets for k, v in bucket]


if __name__ == "__main__":
    hash_map = HashMap(32)
    hash_map.put('name', 'carney')
    hash_map.put('Age', 50)
    hash_map.put('job', 'prime minister')
    print(hash_map.items())        # [('name', 'carney'), ('Age', 50), ('job', 'prime minister')]
    print("Keys:", hash_map.keys())    # ['name', 'Age', 'job']
    print("Values:", hash_map.values())# ['carney', 50, 'prime minister']
    print("'Age' in map?", 'Age' in hash_map) # True
    print("Get job:", hash_map.get('job'))    # 'prime minister'
    print("Remove name:", hash_map.remove('name')) # None
    print(hash_map.items())        # [('Age', 50), ('job', 'prime minister')]
