n, m = map(int, input().split())
adj_list = {i: [] for i in range(1, n + 1)}

u = list(map(int, input().split())) # reuse / iterate e List 
v = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(m):
    adj_list[u[i]].append((v[i], w[i])) # tupple e append 

for key in adj_list:#the loop will run for key = 1, then key = 2, then key = 3.
    print(f"{key}:", end=" ") #{1: [...], 2: [...], 3: [...]},
    for value in adj_list[key]:#Each value is a tuple (destination, weight).
        print(f"({value[0]},{value[1]})", end=" ") #value[0] is the destination node, value[1] is the weight.
    print() 
    #It moves the cursor to the next line for the next node’s output.
    #This prints a newline (empty print() adds a line break).,