class Hungarian:
    def __init__(self, graph):
        """
        :param graph: A list of list, each element graph[i] contains the points in the right side which connects to i
        """
        self.graph = graph
        self.visited = set()
        self.matched = {} # right to left

    def match(self, u):
        for v in self.graph[u]:
            if v not in self.visited:
                self.visited.add(v)
                if v not in self.matched or self.match(self.matched[v]):
                    self.matched[v] = u
                    return True
        return False

    def hungary(self):
        result = 0
        self.matched.clear()
        for u in self.graph:
            self.visited.clear()
            if self.match(u):
                result += 1
        return result


if __name__ == '__main__':
    # https://www.51nod.com/Challenge/Problem.html#!#problemId=2006
    graph = {}
    m, n = [int(x) for x in input().split()]
    while True:
        u, v = [int(x) for x in input().split()]
        if u == -1 and v == -1:
            break
        graph.setdefault(u, []).append(v)
    algo = Hungarian(graph)
    result = algo.hungary()
    print('No Slution!' if result == 0 else result)

