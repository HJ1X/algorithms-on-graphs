#Uses python3

import sys


def is_cyclic(vertex, adj, visited, in_stack):
    visited[vertex] = True
    in_stack[vertex] = True

    for node in adj[vertex]:
        if not visited[node]:
            if is_cyclic(node, adj, visited, in_stack):
                return True
        elif in_stack[node]:
            return True

    in_stack[vertex] = False
    return False


def acyclic(adj):
    visited = [False] * len(adj)
    in_stack = [False] * len(adj)

    for node in range(len(adj)):
        if not visited[node]:
            if is_cyclic(node, adj, visited, in_stack):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

