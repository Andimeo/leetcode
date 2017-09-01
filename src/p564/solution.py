class Solution(object):
    MAX = 10 ** 18 + 1

    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if len(n) == 1:
            if n == '0':
                return '1'
            return str(int(n) - 1)
        if len(n) == 2 and n[0] == '1':
            if n[1] > '1':
                return '11'
            else:
                return '9'

        def mirror(n):
            mid = len(n) // 2
            return n[:mid] + ("" if len(n) % 2 == 0 else n[mid]) + n[:mid][::-1]

        mid = (len(n) + 1) // 2
        l = []
        s = mirror(n)
        diff1 = abs(int(n) - int(s))
        if diff1 == 0:
            diff1 = self.MAX
        l.append((diff1, s))

        left = int(n[:mid]) - 1
        n_new = str(left) + n[mid:]
        # we have to raise the new middle value to 9 if the len is changed
        if len(n_new) % 2 == 1 and len(n) % 2 == 0:
            mid = len(n_new) // 2
            n_new = n_new[:mid] + '9' + n_new[mid + 1:]
        s = mirror(n_new)
        diff2 = abs(int(n) - int(s))
        l.append((diff2, s))

        left = int(n[:mid]) + 1
        n_new = str(left) + n[mid:]
        s = mirror(n_new)
        diff3 = abs(int(n) - int(s))
        l.append((diff3, s))
        import functools
        return min(l, key=functools.cmp_to_key(
            lambda a, b: int(a[1]) - int(b[1]) if a[0] == b[0] else int(a[0]) - int(b[0])))[1]
