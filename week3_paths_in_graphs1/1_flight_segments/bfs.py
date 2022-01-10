#Uses python3

import sys
from collections import deque


def distance(adj, s, t):
    # Using infinite distance to be num_vertices + 1
    inf = len(adj) + 1

    # Initializing dist and prev arrays
    dist = [inf] * len(adj)
    dist[s] = 0

    # initializing queue
    queue = deque()
    queue.appendleft(s)

    while queue:
        u = queue.pop()
        for v in adj[u]:
            if dist[v] == inf:
                queue.appendleft(v)
                dist[v] = dist[u] + 1

    if dist[t] != inf:
        return dist[t]
    else:
        return -1


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
