from collections import defaultdict as dd

class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        row = dd(int)
        col = dd(int)
        ru_ld = dd(int)
        lu_rd = dd(int)
        lamp_set = set()
        for lamp in lamps:
            x, y = lamp
            row[x] += 1
            col[y] += 1
            ru_ld[x-y] += 1
            lu_rd[x+y] += 1
            lamp_set.add((x, y))
        
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        for query in queries:
            x, y = query
            if row[x] > 0 or col[y] > 0 or ru_ld[x-y] > 0 or lu_rd[x+y] > 0:
                result.append(1)
            else:
                result.append(0)
            for p, q in zip(dx, dy):
                nx = p + x
                ny = q + y
                if nx >= 0 and nx < N and ny >= 0 and ny < N and (nx, ny) in lamp_set:
                    row[nx] -= 1
                    col[ny] -= 1
                    ru_ld[nx - ny] -= 1
                    lu_rd[nx - ny] -= 1
                    lamp_set.remove((nx, ny))
        return result
