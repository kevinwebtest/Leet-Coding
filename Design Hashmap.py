class MyHashMap:

    def __init__(self):
        self.hmap = []

    def put(self, key: int, value: int) -> None:
        for k, v in self.hmap:
            if k == key:
                self.hmap.remove([k,v])
                self.hmap.append([key,value])
                return
        self.hmap.append([key,value])

    def get(self, key: int) -> int:
        for k, v in self.hmap:
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        for k, v in self.hmap:
            if key == k:
                self.hmap.remove([k,v])


        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)