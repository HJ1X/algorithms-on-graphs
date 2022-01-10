#Uses python3

import sys

sys.setrecursionlimit(200000)


def reverse(adj):
    rev_adj = [[] for i in range(len(adj))]
    for u in range(len(adj)):
        for v in adj[u]:
            rev_adj[v].append(u)

    return rev_adj


def explore_post(vertex, adj, visited, post_list):
    visited[vertex] = True
    for node in adj[vertex]:
        if not visited[node]:
            explore_post(node, adj, visited, post_list)

    post_list.append(vertex)


def dfs(adj, visited, post_list):
    for node in range(len(adj)):
        if not visited[node]:
            explore_post(node, adj, visited, post_list)


def explore(vertex, adj, visited):
    visited[vertex] = True
    for node in adj[vertex]:
        if not visited[node]:
            explore(node, adj, visited)


def number_of_strongly_connected_components(adj):
    result = 0
    adj_rev = reverse(adj)

    visited = [False] * len(adj)
    post_list = []
    dfs(adj_rev, visited, post_list)

    visited = [False] * len(adj)
    for node in reversed(post_list):
        if not visited[node]:
            explore(node, adj, visited)
            result += 1

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))


