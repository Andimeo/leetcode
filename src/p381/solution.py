class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.pos = collections.defaultdict(list)
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        result = not (val in self.pos and len(self.pos[val]) > 0)
        self.pos[val].append(len(self.nums))
        self.nums.append((val, len(self.pos[val]) - 1))

        return result

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        result = val in self.pos and len(self.pos[val]) > 0
        if result:
            last = self.nums[-1]
            self.pos[last[0]][last[1]] = self.pos[val][-1]
            self.nums[self.pos[val][-1]] = last
            self.pos[val].pop()
            self.nums.pop()
        return result

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.nums[random.randint(0, len(self.nums) - 1)][0]


t = RandomizedCollection()
t.insert(1)
t.insert(1)
t.insert(2)
t.insert(2)
t.insert(2)
t.remove(1)
t.remove(1)
t.remove(2)
t.insert(1)
t.remove(2)
