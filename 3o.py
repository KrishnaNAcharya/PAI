def minimax(depth, pos, is_max, values, alpha=-1000, beta=1000):
    # At bottom level, just return the value
    if depth == 3 or pos >= len(values):
        return values[pos]
    
    # If current player is the maximizing player
    if is_max:
        best = -1000
        for i in range(2):
            val = minimax(depth + 1, pos * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    # If current player is the minimizing player
    else:
        best = 1000
        for i in range(2):
            val = minimax(depth + 1, pos * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]
print("Optimal value:", minimax(0, 0, True, values))
