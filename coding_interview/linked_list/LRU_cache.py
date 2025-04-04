# put(1, 100)  # cache is[1: 100]
# put(2, 250)  # cache is[1: 100, 2: 250]
# put(4, 300)  # cache is[1: 100, 2: 250, 4: 300]t
# put(3, 200)  # cache is[2: 250, 4: 300, 3: 200]
# get(4)      # return 300
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
        self.head = Node()  # sentinel nodes
        self.tail = Node()  # sentinel nodes
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self._remove_node(node)
        self._add_node(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
            
        if key in self.hashmap:
            self._remove_node(self.hashmap[key])
        
        node = Node(key=key, value=value)
        self._add_node(node)
        self.hashmap[key] = node
            
        if len(self.hashmap) > self.capacity:
            lru_node = self.head.next
            self._remove_node(lru_node)
            del self.hashmap[lru_node.key]
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_node(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

