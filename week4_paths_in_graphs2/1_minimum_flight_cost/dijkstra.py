#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    #write your code here
    # implement using heapq or priorityqueue implementation. Instead of changing priority just add the same node with
    # new dist value. Can also use another bool array 'is_processed', to check if the node is already processed to
    # remove the overhead of processing it again as in the case of striver.

    # Setting infinity value for distances
    inf = float('inf')

    # Initializing dist and prev arrays
    dist = [inf] * len(adj)
    dist[s] = 0
    prev = [None] * len(adj)

    # Initializing priority queue
    pq = queue.PriorityQueue()
    for node in range(len(adj)):
        pq.put_nowait([inf, node])
    pq.put_nowait([0, s])

    while not pq.empty():
        u = pq.get_nowait()[1]
        for v_ind in range(len(adj[u])):
            v = adj[u][v_ind]
            weight_uv = cost[u][v_ind]

            if dist[v] > dist[u] + weight_uv:
                dist[v] = dist[u] + weight_uv
                prev[v] = u
                pq.put_nowait([dist[v], v])

    if dist[t] == inf:
        return -1
    else:
        return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
