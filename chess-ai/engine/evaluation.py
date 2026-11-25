import chess

# piece value assignation
PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 0
}

CHECKMATE_SCORE = 100000

def evaluate(board: chess.BOARD) -> int:
    """
    Evaluate a chess position from White's perspective.

    Positive score = a white advantage
    Negative score = a black advantage
    zero = Equal / draw
    """

    # check if game has ended
    outcome = board.outcome(claim_draw=True)

    if outcome is not None:
        if outcome.winner == chess.WHITE:
            return CHECKMATE_SCORE
        elif outcome.winner == chess.BLACK:
            return -CHECKMATE_SCORE
        else: return 0

    score = 0

    # Iterate through the pieces currently on the board
    for piece in board.piece_map().values():
        value = PIECE_VALUES[piece.piece_type]

        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value
            
    return score