def knights_of_konigsberg():
    import sys
    input = sys.stdin.readline

    N, M, K = map(int, input().split())
    knights = set() # empty lists

    for _ in range(K):
        x, y = map(int, input().split())
        knights.add((x, y)) # add to set 

    # All 8 possible knight moves
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    for x, y in knights:
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (nx, ny) in knights:
                print("YES")
                return
    print("NO")
if __name__ == "__main__":
    knights_of_konigsberg()
