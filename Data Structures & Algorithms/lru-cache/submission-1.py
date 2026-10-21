class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if not key in self.d: return -1
        removed_value = self.d.pop(key)
        self.d[key] = removed_value
        return removed_value
        

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            removed_value = self.d.pop(key)
            self.d[key] = value
        elif self.capacity == len(self.d):
            first = next(iter(self.d))
            removed_value = self.d.pop(first)
            self.d[key] = value
        else: self.d[key] = value
        
