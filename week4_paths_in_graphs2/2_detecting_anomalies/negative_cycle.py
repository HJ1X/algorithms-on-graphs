# Uses python3

import sys


def relaxed(u, v, weight_uv, dist):
    if dist[v] > dist[u] + weight_uv:
        dist[v] = dist[u] + weight_uv
        return True

    return False


def contains_negative_cycle(adj, cost, dist, source):
    dist[source] = 0

    for iter_count in range(len(adj) + 1):
        relaxed_in_iteration = False
        for u in range(len(adj)):
            for v_ind in range(len(adj[u])):
                if relaxed(u, adj[u][v_ind], cost[u][v_ind], dist):
                    relaxed_in_iteration = True

        # print(iter_count, relaxed_in_iteration)
        if not relaxed_in_iteration:
            break

        if iter_count == len(adj):
            return True

    return False


def negative_cycle(adj, cost):
    inf = float('inf')

    # dist array
    dist = [inf] * len(adj)

    for node in range(len(adj)):
        if dist[node] == inf:
            if contains_negative_cycle(adj, cost, dist, node):
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
