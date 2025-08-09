import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
neighbors = [[] for _ in range(N+1)]

def gcd(a, b):
    while b:
        a, b = b, a % b # algo e erom
    return a

for i in range(1, N+1): # iterating every node 
    for j in range(1, N+1): # you check all possible nodes j to see if they should be connected.
        if i != j and gcd(i, j) == 1: # self node skip,GCF=1
            neighbors[i].append(j)

for _ in range(Q):# queries
    X, K = map(int, input().split())
    if K > len(neighbors[X]): # out of bounds 
        print(-1)
    else:
        print(neighbors[X][K-1])
