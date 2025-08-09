N, M = map(int, input().split()) # reading multi
adj_mat = [[0] * N for _ in range(N)] #
 
for k in range(M):
  u,v,w = map(int, input().split())
  adj_mat[u-1][v-1] = w
 
for i in range(N): # row take nicchi
  for j in range(N): # col take dhore dhore print 
    print(adj_mat[i][j], end=" ")
  print() # new line anar jonno 
