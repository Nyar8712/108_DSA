from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * self.capacity
        
    def add(self, key: str):
        hash_code = MD5.new()
        hash_code.update(key.encode("utf-8"))
        tran_h = int(hash_code.hexdigest(), 16)
        
        index = tran_h % self.capacity
        cur = self.data[index]
        while cur:
            if cur.val == tran_h:
                return
            cur = cur.next
        cur_next = ListNode(tran_h)
        cur_next.next = self.data[index]
        self.data[index] = cur_next
        
    def remove(self, key: str):
        hash_code = MD5.new()
        hash_code.update(key.encode("utf-8"))
        tran_h = int(hash_code.hexdigest(), 16)
        
        index = tran_h % self.capacity
        cur = self.data[index]
        if cur and cur.val == tran_h:
            self.data[index] = cur.next
            return
        pre = None
        while cur:
            if cur.val == tran_h:
                pre.next = cur.next
                return
            pre = cur
            cur = cur.next
            
    def contains(self, key: str):
        hash_code = MD5.new()
        hash_code.update(key.encode("utf-8"))
        tran_h = int(hash_code.hexdigest(), 16)
        
        index = tran_h % self.capacity
        cur = self.data[index]
        while cur:
            if cur.val == tran_h:
                return True
            cur = cur.next
        return False
      
# Hash_Table = MyHashSet()
# Hash_Table.add("dog")
# Hash_Table.add("pig")
# outcome = Hash_Table.contains("pig")
# print(outcome)
# outcome = Hash_Table.contains("dog")
# print(outcome)
# outcome = Hash_Table.contains("cat")
# print(outcome)
# Hash_Table.add("bird")
# outcome = Hash_Table.contains("bird")
# print(outcome)
# Hash_Table.remove("pig")
# outcome = Hash_Table.contains("pig")
# print(outcome)
