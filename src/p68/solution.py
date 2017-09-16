class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        sentences = []
        cur_line = [words[0]]
        l = len(words[0])
        for i in range(1, len(words)):
            if l + 1 + len(words[i]) <= maxWidth:
                cur_line.append(words[i])
                l += 1 + len(words[i])
            else:
                sentences.append(cur_line)
                cur_line = [words[i]]
                l = len(words[i])
        results = []
        for line in sentences:
            results.append(self.stringify(line, maxWidth))
        s = []
        s.extend(list(cur_line[0]))
        l = len(cur_line[0])
        for i in range(1, len(cur_line)):
            s.append(' ')
            s.extend(list(cur_line[i]))
            l += 1 + len(cur_line[i])
        for i in range(l, maxWidth):
            s.append(' ')
        results.append(''.join(s))
        return results

    def stringify(self, words_line, maxWidth):
        n = len(words_line)
        if n == 1:
            return words_line[0] + ' ' * (maxWidth - len(words_line[0]))
        l = sum((len(word) for word in words_line)) + n - 1
        p = (maxWidth - l) / (n - 1)
        q = (maxWidth - l) % (n - 1)
        result = list(words_line[0])
        for i in range(1, n):
            result.extend(' ' * (p + 1))
            if q > 0:
                result.extend(' ')
                q -= 1
            result.extend(list(words_line[i]))
        return ''.join(result)
