import collections


def least_nodes(edges):
    pred = collections.defaultdict(set)
    succ = collections.defaultdict(set)

    for start, end in edges:
        pred[end].add(start)
        succ[start].add(end)

    components = kosarajus(pred, succ)
    component_pred = collections.defaultdict(set)
    component_succ = collections.defaultdict(set)
    for start, end in edges:
        if components[start] != components[end]:
            component_start = components[start]
            component_end = components[end]

            component_pred[component_end].add(component_start)
            component_succ[component_start].add(component_end)

    return set(component_succ.keys()) - set(component_pred.keys())


def kosarajus(pred, succ):
    all_nodes = set(pred.keys()) | set(succ.keys())
    order = []
    visited = set()

    def visit(node):
        if node not in visited:
            visited.add(node)
            for out_neighbor in succ[node]:
                visit(out_neighbor)
            order.insert(0, node)

    for node in all_nodes:
        visit(node)

    components = {}

    def assign(node, root):
        if node not in components:
            components[node] = root
            for in_neighbor in pred[node]:
                assign(in_neighbor, root)

    for node in order:
        assign(node, node)

    return components
