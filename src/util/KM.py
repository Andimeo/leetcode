class KM:
    INF = 0x7fffffff

    def __init__(self, n, graph):
        self.n = n
        self.graph = graph  # adjacent matrix
        self.Lx = [max(self.graph[i]) for i in range(self.n)]
        self.Ly = [0] * n
        self.slack = None
        self.S = None
        self.T = None
        self.matched = [-1] * n

    def match(self, u):
        self.S[u] = True
        for v in range(self.n):
            # v is already in the cross road
            if self.T[v]:
                continue
            t = self.Lx[u] + self.Ly[v] - self.graph[u][v]
            if not t:
                self.T[v] = True
                if self.matched[v] == -1 or self.match(self.matched[v]):
                    self.matched[v] = u
                    return True
            else:
                self.slack[v] = min(self.slack[v], t)
        return False

    def update(self):
        d = min(self.slack[i] for i in range(self.n) if not self.T[i])
        for i in range(self.n):
            if self.S[i]:
                self.Lx[i] -= d
        for i in range(self.n):
            if self.T[i]:
                self.Ly[i] += d
            else:
                self.slack[i] -= d

    def km(self):
        for i in range(self.n):
            self.slack = [KM.INF] * self.n
            while True:
                self.S = [False] * self.n
                self.T = [False] * self.n
                if self.match(i):
                    break
                else:
                    self.update()
        return sum(self.graph[self.matched[i]][i] for i in range(self.n) if self.matched[i] != -1)


# http://codeforces.com/contest/321/problem/B
if __name__ == '__main__':
    inf = KM.INF
    maxn = 500
    graph = []
    for i in range(maxn):
        graph.append([0] * maxn)
    n, m = [int(x) for x in input().split()]
    jiro = [input().split() for i in range(n)]
    ciel = [int(input()) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if jiro[j][0] == 'ATK':
                if ciel[i] >= int(jiro[j][1]):
                    graph[i][j] = ciel[i] - int(jiro[j][1])
    ans = KM(m, graph).km()

    if m > n:
        for i in range(m):
            for j in range(n, m):
                graph[i][j] = ciel[i]
        for i in range(m):
            for j in range(n):
                if jiro[j][0] == 'ATK':
                    if ciel[i] >= int(jiro[j][1]):
                        graph[i][j] = ciel[i] - int(jiro[j][1])
                    else:
                        graph[i][j] = -inf
                else:
                    if ciel[i] > int(jiro[j][1]):
                        graph[i][j] = 0
                    else:
                        graph[i][j] = -inf
        ans = max(ans, KM(m, graph).km())
    print(ans)