def king_moves():
    N = int(input())
    x, y = map(int, input().split())

    # Moves listed in ascending order by row, then column
    moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    valid_moves = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy 
        if 1 <= nx <= N and 1 <= ny <= N: #Checks if (nx, ny) is inside the chessboard boundaries.
            valid_moves.append((nx, ny)) #  appended here
    print(len(valid_moves))
    for move in valid_moves:
        print(move[0], move[1])
if __name__ == "__main__":
    king_moves()
