def is_winner(board, player):
    win_patterns = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    return any(all(board[i] == player for i in pattern) for pattern in win_patterns)

def minimax(board, is_maximizing):
    if is_winner(board, 'X'): return -1
    if is_winner(board, 'O'): return 1
    if '' not in board: return 0

    scores = []
    for i, cell in enumerate(board):
        if cell == '':
            board[i] = 'O' if is_maximizing else 'X'
            scores.append(minimax(board, not is_maximizing))
            board[i] = ''
    return max(scores) if is_maximizing else min(scores)

def best_move(board):
    return max((i for i, cell in enumerate(board) if cell == ''), key=lambda i: minimax(board[:i] + ['O'] + board[i+1:], False))

def main():
    board = [''] * 9
    while '' in board and not any(is_winner(board, p) for p in 'XO'):
        print(' '.join(board[i] or str(i) for i in range(9)))
        board[int(input("Enter move (0-8): "))] = 'X'
        if '' not in board or is_winner(board, 'X'): break
        board[best_move(board)] = 'O'
    print(' '.join(board[i] or str(i) for i in range(9)))
    print("You win!" if is_winner(board, 'X') else "AI wins!" if is_winner(board, 'O') else "It's a draw!")

if __name__ == "__main__":
    main()