# Define the utility function that returns the score for a given state of the game
def utility(state, player):
    # Return a positive score if the player has won, a negative score if the opponent has won,
    # and 0 if the game is a tie or has not ended yet.
    pass


# Define the Minimax function that returns the best move for a given state of the game
def minimax(state, player, MAX_PLAYER=None, MIN_PLAYER=None):
    # Check if the game has ended
    if is_terminal(state):
        return None, utility(state, player)

    # If it is the player's turn, maximize their score
    if player == MAX_PLAYER:
        best_score = -float('inf')
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            _, score = minimax(new_state, MIN_PLAYER)
            if score > best_score:
                best_score = score
                best_move = move

    # If it is the opponent's turn, minimize the player's score
    else:
        best_score = float('inf')
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            _, score = minimax(new_state, MAX_PLAYER)
            if score < best_score:
                best_score = score
                best_move = move

    return best_move, best_score


def is_terminal():
    pass


def get_possible_moves():
    pass


def make_move(state, move, player):
    pass
