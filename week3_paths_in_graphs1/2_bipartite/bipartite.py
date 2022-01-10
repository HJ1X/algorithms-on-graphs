#Uses python3

import sys
from collections import deque


def is_bipartite(root, adj, colored):
    colored[root] = 0

    # initializing queue
    q = deque()
    q.appendleft(root)

    while q:
        u = q.pop()
        for v in adj[u]:
            if colored[v] == -1:
                colored[v] = 1 - colored[u]
                q.appendleft(v)
            elif colored[v] == colored[u]:
                return False

    return True


def bipartite(adj):
    # initializing colors array with -1. Let colors be 1 and 0
    colored = [-1] * len(adj)

    for node in range(len(adj)):
        if colored[node] == -1:
            if not is_bipartite(node, adj, colored):
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
