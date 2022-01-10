# Uses python3

import sys


def explore(vertex, adj, visited):
    visited[vertex] = True

    for node in adj[vertex]:
        if not visited[node]:
            explore(node, adj, visited)


def number_of_components(adj):
    # write your code here
    visited = [False] * len(adj)
    components = 0

    for node in range(len(adj)):
        if not visited[node]:
            explore(node, adj, visited)
            components += 1

    return components


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
    print(number_of_components(adj))
