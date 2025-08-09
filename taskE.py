import sys
input = sys.stdin.readline
N, M = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
indegree = [0] * (N + 1) # empty list created 
outdegree = [0] * (N + 1)
for i in range(M): # in /out thaklei barai dibo
    outdegree[u[i]] += 1
    indegree[v[i]] += 1 
#result = [str(indegree[i] - outdegree[i]) for i in range(1, N + 1)]
#print(' '.join(result))
print(*[indegree[i] - outdegree[i] for i in range(1, N + 1)])
