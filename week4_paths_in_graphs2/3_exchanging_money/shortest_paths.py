#Uses python3

import sys
import queue
from collections import deque


def relax(u, v, weight_uv, dist, reachable):
    if dist[v] > dist[u] + weight_uv:
        dist[v] = dist[u] + weight_uv
        reachable[v] = 1


def shortest_paths(adj, cost, s, dist, reachable, shortest):
    inf = float('inf')
    dist[s] = 0
    reachable[s] = 1

    # relaxing edges till v-1 iterations
    for i in range(len(adj) - 1):
        for u in range(len(adj)):
            for v_ind in range(len(adj[u])):
                relax(u, adj[u][v_ind], cost[u][v_ind], dist, reachable)

    # detecting negative cycles on vth iteration
    q = deque()
    for u in range(len(adj)):
        for v_ind in range(len(adj[u])):
            v = adj[u][v_ind]
            weight_uv = cost[u][v_ind]

            # adding relaxed nodes to queue
            if dist[v] > dist[u] + weight_uv:
                dist[v] = dist[u] + weight_uv
                shortest[v] = 0
                q.appendleft(v)

    # Doing BFS on relaxed nodes
    visited = [False] * n
    while q:
        u = q.pop()
        visited[u] = True

        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.appendleft(v)
                shortest[v] = 0

    # print(dist)
    # print(reachable)
    # print(shortest)

    return


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
    s = data[0]
    s -= 1

    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
