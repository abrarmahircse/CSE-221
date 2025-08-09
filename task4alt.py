def dfs_iterative(graph, start, visited):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)


def eulerian_path():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())

    if m == 0:
        print("YES")
        return

    u = list(map(int, input().split()))
    v = list(map(int, input().split()))

    degree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    vertices_with_edges = set()

    for i in range(m):
        st = u[i]
        end = v[i]
        degree[st] += 1
        degree[end] += 1
        graph[st].append(end)
        graph[end].append(st)
        vertices_with_edges.add(st)
        vertices_with_edges.add(end)

    visited = [False] * (n + 1)
    start_vertex = next(iter(vertices_with_edges))

    dfs_iterative(graph, start_vertex, visited)

    for vertex in vertices_with_edges:
        if not visited[vertex]:
            print("NO")
            return

    odd_count = sum(1 for i in range(1, n + 1) if degree[i] % 2 == 1)

    if odd_count == 0 or odd_count == 2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    eulerian_path()
