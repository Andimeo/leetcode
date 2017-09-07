class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.pi_table = None
        self.compute_pi_table()

    # pi[q] means at position q, the length of the longest prefix of pattern
    # which is a suffix of pattern[:q + 1]
    def compute_pi_table(self):
        n = len(self.pattern)
        self.pi_table = [-1]
        k = -1
        for q in range(1, n):
            while k >= 0 and self.pattern[k + 1] != self.pattern[q]:
                k = self.pi_table[k]
            if self.pattern[k + 1] == self.pattern[q]:
                k += 1
            self.pi_table.append(k)

    def match(self, text):
        n = len(text)
        m = len(self.pattern)
        q = -1
        for i in range(1, n):
            while q >= 0 and self.pattern[q + 1] != text[i]:
                q = self.pi_table[q]
            if self.pattern[q + 1] == text[i]:
                q += 1
            if q == m - 1:
                return True

    def count(self, text):
        n = len(text)
        m = len(self.pattern)
        q = -1
        result = 0
        for i in range(1, n):
            while q >= 0 and self.pattern[q + 1] != text[i]:
                q = self.pi_table[q]
            if self.pattern[q + 1] == text[i]:
                q += 1
            if q == m - 1:
                result += 1
                q = self.pi_table[q]
        return result
