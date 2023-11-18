from Node import Node
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lib = {}
        self.head = Node()
        self.tail = Node()
        
        self.head.right = self.tail
        self.tail.left = self.head
        
    def get(self, key: int) -> int:
        if key in self.lib:
            node = self.lib[key]
            self._remove_node(node)
            self._insert_after(self.head, node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lib:
            node = self.lib[key]
            self._remove_node(node)
            self._insert_after(self.head, node)
            node.val = value
            return

        if self.capacity == len(self.lib):
            last_node = self.tail.left
            self._remove_node(last_node)
            del self.lib[last_node.key]

        new_node = Node(key, value)
        self._insert_after(self.head, new_node)
        self.lib[key] = new_node

    def _remove_node(self, node: Node) -> None:
        node.left.right = node.right
        node.right.left = node.left
    
    def _insert_after(self, prev: Node, node: Node) -> None:
        node.right = prev.right
        prev.right.left = node
        
        node.left = prev
        prev.right = node

# Your LRUCache object will be instantiated and called as such:
if __name__ == "__main__":
    obj = LRUCache(2)
    get_res = obj.get(1)
    print(f"get 1: {get_res}")
    obj.put(1,"hai")
    get_res = obj.get(1)
    print(f"get 1 after put: {get_res}")
