class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache(object):
    # Double linked list
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_dict = {}
        self.head = None
        self.last = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_dict:
            return -1
        key_node = self.key_dict[key]
        self.unlink(key_node)
        self.prepend(key_node)
        return key_node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.key_dict:
            key_node = self.key_dict[key]
            key_node.value = value
            self.unlink(key_node)
            self.prepend(key_node)
            return
        if len(self.key_dict) == self.capacity:
            key_node = self.last
            self.unlink(key_node)
            del self.key_dict[key_node.key]
        key_node = self.key_dict[key] = KeyNode(key, value)
        self.prepend(key_node)

    def unlink(self, key_node):
        prev, next = key_node.prev, key_node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if self.head == key_node:
            self.head = next
        if self.last == key_node:
            self.last = prev

    def prepend(self, key_node):
        head = self.head
        key_node.prev = None
        key_node.next = head
        if head:
            head.prev = key_node
        self.head = key_node
        if self.last is None:
            self.last = key_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)