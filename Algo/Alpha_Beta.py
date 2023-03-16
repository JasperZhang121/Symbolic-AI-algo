# Alpha - Beta Pruning

def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player):
    # Check if the maximum depth is reached or the node is terminal
    if depth == 0 or node.is_terminal():
        return node.evaluate(), None

    # Maximizing player's turn
    if maximizing_player:
        max_val = float('-inf')
        best_child = None
        for child in node.generate_children():
            child_val, _ = minimax_alpha_beta(child, depth - 1, alpha, beta, False)
            if child_val > max_val:
                max_val = child_val
                best_child = child
            alpha = max(alpha, max_val)
            if beta <= alpha:
                break
        return max_val, best_child

    # Minimizing player's turn
    else:
        min_val = float('inf')
        best_child = None
        for child in node.generate_children():
            child_val, _ = minimax_alpha_beta(child, depth - 1, alpha, beta, True)
            if child_val < min_val:
                min_val = child_val
                best_child = child
            beta = min(beta, min_val)
            if beta <= alpha:
                break
        return min_val, best_child
