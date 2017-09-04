class KeyNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class ValueNode:
    def __init__(self, value, prev, next):
        self.value = value
        self.prev = prev
        self.next = next
        self.first = self.last = None


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_dict = {}
        self.value_dict = {}
        self.head, self.last = None, None

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.key_dict:
            self.increase(key)
            return
        self.key_dict[key] = key_node = KeyNode(key, 1)
        value_node = self.value_dict.get(1)
        if value_node is None:
            self.value_dict[1] = value_node = ValueNode(1, None, self.head)
            if self.head:
                self.head.prev = value_node
            self.head = value_node
            if self.last is None:
                self.last = value_node
        self.insert_key_node(key_node)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.key_dict:
            return
        self.decrease(key)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.last is None:
            return ""
        return self.last.first.key

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.head is None:
            return ""
        return self.head.first.key

    def increase(self, key):
        key_node = self.key_dict[key]
        value_node = self.value_dict[key_node.value]
        key_node.value += 1
        if key_node.value not in self.value_dict:
            self.insert_value_node_after(key_node.value, value_node)
        self.unlink_key_node(key_node, value_node)
        self.insert_key_node(key_node)

    def insert_value_node_after(self, new_value, value_node):
        self.value_dict[new_value] = new_value_node = ValueNode(new_value, None, None)
        new_value_node.prev = value_node
        new_value_node.next = value_node.next
        if value_node.next:
            value_node.next.prev = new_value_node
        value_node.next = new_value_node
        if self.last == value_node:
            self.last = new_value_node

    def decrease(self, key):
        key_node = self.key_dict[key]
        value_node = self.value_dict[key_node.value]
        key_node.value -= 1
        if key_node.value == 0:
            self.remove_key_node(key_node, value_node)
            return
        if key_node.value not in self.value_dict:
            self.insert_value_node_before(key_node.value, value_node)
        self.unlink_key_node(key_node, value_node)
        self.insert_key_node(key_node)

    def insert_value_node_before(self, new_value, value_node):
        self.value_dict[new_value] = new_value_node = ValueNode(new_value, None, None)
        new_value_node.prev = value_node.prev
        new_value_node.next = value_node
        if value_node.prev:
            value_node.prev.next = new_value_node
        value_node.prev = new_value_node
        if self.head == value_node:
            self.head = new_value_node

    def insert_key_node(self, key_node):
        value_node = self.value_dict[key_node.value]
        key_node.prev, key_node.next = None, value_node.first
        if value_node.first:
            value_node.first.prev = key_node
        value_node.first = key_node
        if value_node.last is None:
            value_node.last = key_node

    def remove_key_node(self, key_node, value_node):
        self.unlink_key_node(key_node, value_node)
        del self.key_dict[key_node.key]

    def unlink_key_node(self, key_node, value_node):
        prev, next = key_node.prev, key_node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if value_node.last == key_node:
            value_node.last = prev
        if value_node.first == key_node:
            value_node.first = next
        if value_node.first is None:
            self.remove_value_node(value_node)

    def remove_value_node(self, value_node):
        prev, next = value_node.prev, value_node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if self.last == value_node:
            self.last = prev
        if self.head == value_node:
            self.head = next
        del self.value_dict[value_node.value]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
