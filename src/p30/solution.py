class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        import collections
        d = collections.defaultdict(int)
        for word in words:
            d[word] += 1
        num = len(words)
        length = len(words[0])
        result = []
        for i in range(length):
            start, end = i
            cnt = 0
            cur = collections.defaultdict(int)
            while end + length <= len(s):
                w = s[end:end + len]
                if w in d:
                    cur[w] += 1
                    cnt += 1
                    if cur[w] > d[w]:
                        j = start
                        while True:
                            sw = s[j:j + length]
                            cur[sw] -= 1
                            cnt -= 1
                            if sw == w:
                                start = j + length
                                break
                            j += length
                    if cnt == num:
                        result.append(start)
                else:
                    start = end + length
                    cnt = 0
                    cur.clear()
                end += length
        return result
