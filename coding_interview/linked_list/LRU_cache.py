# put(1, 100)  # cache is[1: 100]
# put(2, 250)  # cache is[1: 100, 2: 250]
# get(2)       # return 250
# put(4, 300)  # cache is[1: 100, 2: 250, 4: 300]t
# put(3, 200)  # cache is[2: 250, 4: 300, 3: 200]
# get(4)       # return 300
# get(1)       # key 1 was evicted when adding key 3 due to the capacity
#              # limit: return -1

class Node:
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap: dict[int, Node] = {}
        self.head = None
        self.tail = None
        self.len = 0


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        # Get node by key
        n = self.hashmap[key]
            
        # If node is tail, just return
        if self.tail == n:
            return n.value
        
        # remove node from Linked List
        self.remove_node(n)
        # move it to the tail - most recently accessed
        self.add_node_to_tail(n)
        return n.value
        

    def put(self, key: int, value: int) -> None:
        print(f"\nPUT: {key}, {value}, HM {self.hashmap}")
        if self.capacity <= 0:
            return
        
        # update existing node
        if key in self.hashmap:
            n = self.hashmap[key]
            n.value = value  # update existing value in hashmap
            self.remove_node(n)  # remove node, it will be added to the tail
        else:
            n = Node(key=key, value=value, prev=self.tail)
            self.hashmap[key] = n  # add new node to the hashmap
            if self.len >= self.capacity and self.head:
                #  evict head when the capacity exceeds (least recently used)
                self.hashmap.pop(self.head.key, -1)
                self.remove_node(self.head)

        self.add_node_to_tail(n)  # add node to the tail: either new one or the existing one (most recently accessed)
        
        if self.head:
            print(f"DEBUG END: len {self.len}, HM: {self.hashmap.keys()} LL: head {self.head.key} <- head.prev {self.head.prev} tail {self.tail.key} -> {self.tail.next}")
    
    
    def remove_node(self, node):
        self.len -= 1
        if node == self.tail and node == self.head:
            self.head == None
            self.tail == None
            return
            
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
            
        # If node is head and not tail, move head 
        if node == self.head:
            self.head = node.next
            node.next.prev = None  # remove pointers
            node.next = None
        else:                        
            # If node is in the middle
            node.prev.next = node.next
            node.next.prev = node.prev
        return
    
    
    def add_node_to_tail(self, node):
        self.len += 1
        # put the 1st item
        if self.head is None:
            self.head = node
            self.tail = self.head
            node.next = None
            node.prev = None
            return
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node  # make new tail
        


if __name__ == "__main__":
    lru = LRUCache(capacity=2)
    
    lru.put(1, 1)
    lru.put(2, 2)
    a = lru.get(1) # 1, move 1 to tail
    
    lru.put(3, 3) # remove 2 add 3
    b = lru.get(2) # -1
    
    lru.put(4, 3) # remove 1
    c = lru.get(1) # -1

    print(f"{a} {b} {c}")
    
    lru2 = LRUCache(capacity=2)
    
    lru2.put(1, 1)
    a = lru2.get(1) # 1, move 1 to tail
    
    lru2.put(3, 3) # remove 2 add 3
    b = lru2.get(2) # -1
    
    c = lru2.get(1) # -1
    lru2.put(2, 2)
    d = lru2.get(3) # -1


    print(f"{a} {b} {c} {d}")