def displayPathtoPrincess(n, grid):
    bot_pos = None
    princess_pos = None

    # Find the positions of the bot and princess
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                bot_pos = (i, j)
            elif grid[i][j] == 'p':
                princess_pos = (i, j)

    # Calculate the moves needed to rescue the princess
    vertical_moves = princess_pos[0] - bot_pos[0]
    horizontal_moves = princess_pos[1] - bot_pos[1]

    # Generate the sequence of moves
    moves = []
    if vertical_moves > 0:
        moves.extend(['DOWN'] * vertical_moves)
    else:
        moves.extend(['UP'] * (-vertical_moves))

    if horizontal_moves > 0:
        moves.extend(['RIGHT'] * horizontal_moves)
    else:
        moves.extend(['LEFT'] * (-horizontal_moves))

    return moves

# Read input
n = int(input())
grid = [input() for _ in range(n)]

# Get the sequence of moves
moves = displayPathtoPrincess(n, grid)

# Print the moves
for move in moves:
    print(move)
