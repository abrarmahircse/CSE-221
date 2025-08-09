N = int(input())
adj_matrix = [[0] * N for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    k = line[0] # no of neighbours          
    neighbors = line[1:] # 0 chilo tiotal er so 1 theke end neighbors
    for neighbor in neighbors:
        adj_matrix[i][neighbor] = 1  #why?>
for i in range(N): #row
    for j in range(N): # col akare print 
        print(adj_matrix[i][j], end=" ")
    print() # break and print 
