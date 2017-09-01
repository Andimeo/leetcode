class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r, i = int(a.split('+')[0]), int(a.split('+')[1][:-1])
        a = complex(r, i)
        r, i = int(b.split('+')[0]), int(b.split('+')[1][:-1])
        b = complex(r, i)
        p = a * b
        return '{}+{}i'.format(int(p.real), int(p.imag))
