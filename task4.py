import sys
input = sys.stdin.readline
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for i in range(M):
    a, b = u[i], v[i]
    graph[a].append(b)
    graph[b].append(a)
    if a == b: # self loop
        degree[a] += 2
    else:
        degree[a] += 1
        degree[b] += 1

start = -1
for i in range(1, N+1):
    if degree[i] > 0:
        start = i
        break

if start == -1:
    print("YES")
    sys.exit()

visited = [False] * (N+1)

def dfs_iterative(start):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

dfs_iterative(start)

for i in range(1, N+1):
    if degree[i] > 0 and not visited[i]:
        print("NO")
        sys.exit()

odd_count = sum(d % 2 for d in degree)

print("YES" if odd_count in (0, 2) else "NO")
