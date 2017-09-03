class KeyNode:
    def __init__(self, key, value, freq=1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = self.next = None


class FreqNode:
    def __init__(self, freq, prev, next):
        self.freq = freq
        self.prev = prev
        self.next = next
        self.first = self.last = None


class LFUCache(object):
    # http://bookshadow.com/weblog/2016/11/22/leetcode-lfu-cache/
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key_dict = {}
        self.freq_dict = {}
        self.head = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.key_dict:
            key_node = self.key_dict[key]
            value = key_node.value
            self.increase_freq(key, value)
            return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return
        if key in self.key_dict:
            self.increase_freq(key, value)
            return
        if len(self.key_dict) == self.capacity:
            self.remove_key_node(self.head.last)
        self.insert_key_node(key, value)

    def increase_freq(self, key, value):
        key_node = self.key_dict[key]
        key_node.value = value
        freq_node = self.freq_dict[key_node.freq]
        next_freq_node = freq_node.next
        key_node.freq += 1
        if next_freq_node is None or next_freq_node.freq > key_node.freq:
            next_freq_node = self.insert_freq_node_after(key_node.freq, freq_node)
        self.unlink_key_node(key_node, freq_node)
        self.link_key_node(key_node, next_freq_node)

    def insert_freq_node_after(self, freq, freq_node):
        new_freq_node = FreqNode(freq, freq_node, freq_node.next)
        self.freq_dict[freq] = new_freq_node
        if freq_node.next:
            freq_node.next.prev = new_freq_node
        freq_node.next = new_freq_node
        return new_freq_node

    def unlink_key_node(self, key_node, freq_node):
        next, prev = key_node.next, key_node.prev
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if freq_node.first == key_node:
            freq_node.first = next
        if freq_node.last == key_node:
            freq_node.last = prev
        if freq_node.first is None:
            self.remove_freq_node(freq_node)

    def link_key_node(self, key_node, freq_node):
        first_key_node = freq_node.first
        key_node.prev = None
        key_node.next = first_key_node
        if first_key_node:
            first_key_node.prev = key_node
        freq_node.first = key_node
        if freq_node.last is None:
            freq_node.last = key_node

    def remove_freq_node(self, freq_node):
        prev, next = freq_node.prev, freq_node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if self.head == freq_node:
            self.head = next
        del self.freq_dict[freq_node.freq]

    def insert_key_node(self, key, value):
        key_node = self.key_dict[key] = KeyNode(key, value)
        freq_node = self.freq_dict.get(1)
        if freq_node is None:
            freq_node = self.freq_dict[1] = FreqNode(1, None, self.head)
            if self.head:
                self.head.prev = freq_node
            self.head = freq_node
        self.link_key_node(key_node, freq_node)

    def remove_key_node(self, key_node):
        self.unlink_key_node(key_node, self.freq_dict[key_node.freq])
        del self.key_dict[key_node.key]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
