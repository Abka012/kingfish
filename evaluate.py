import chess

piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 479,
    chess.KNIGHT: 280,
    chess.BISHOP: 320,
    chess.QUEEN: 929,
    chess.KING: 60000
}

pawnEvalWhite = [
    0,   0,   0,   0,   0,   0,   0,   0,
    78,  83,  86,  73, 102,  82,  85,  90,
    7,  29,  21,  44,  40,  31,  44,   7,
    -17,  16,  -2,  15,  14,   0,  15, -13,
    -26,   3,  10,   9,   6,   1,   0, -23,
    -22,   9,   5, -11, -10,  -2,   3, -19,
    -31,   8,  -7, -37, -36, -14,   3, -31,
    0,   0,   0,   0,   0,   0,   0,   0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    -66, -53, -75, -75, -10, -55, -58, -70,
    -3,  -6, 100, -36,   4,  62,  -4, -14,
    10,  67,   1,  74,  73,  27,  62,  -2,
    24,  24,  45,  37,  33,  41,  25,  17,
    -1,   5,  31,  21,  22,  35,   2,   0,
    -18,  10,  13,  22,  18,  15,  11, -14,
    -23, -15,   2,   0,   2,   0, -23, -20,
    -74, -23, -26, -24, -19, -35, -22, -69
]

bishopEvalWhite = [
    -59, -78, -82, -76, -23,-107, -37, -50,
    -11,  20,  35, -42, -39,  31,   2, -22,
    -9,  39, -32,  41,  52, -10,  28, -14,
    25,  17,  20,  34,  26,  25,  15,  10,
    13,  10,  17,  23,  17,  16,   0,   7,
    14,  25,  24,  15,   8,  25,  20,  15,
    19,  20,  11,   6,   7,   6,  20,  16,
    -7,   2, -15, -12, -14, -15, -10, -10
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    35,  29,  33,   4,  37,  33,  56,  50,
    55,  29,  56,  67,  55,  62,  34,  60,
    19,  35,  28,  33,  45,  27,  25,  15,
     0,   5,  16,  13,  18,  -4,  -9,  -6,
    -28, -35, -16, -21, -13, -29, -46, -30,
    -42, -28, -42, -25, -25, -35, -26, -46,
    -53, -38, -31, -26, -29, -43, -44, -53,
    -30, -24, -18,   5,  -2, -18, -31, -32
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    6,   1,  -8,-104,  69,  24,  88,  26,
    14,  32,  60, -10,  20,  76,  57,  24,
    -2,  43,  32,  60,  72,  63,  43,   2,
     1, -16,  22,  17,  25,  20, -13,  -6,
    -14, -15,  -2,  -5,  -1, -10, -20, -22,
    -30,  -6, -13, -11, -16, -11, -16, -27,
    -36, -18,   0, -19, -15, -15, -21, -38,
    -39, -30, -31, -13, -31, -36, -34, -42
]

kingEvalWhite = [
    4,  54,  47, -99, -99,  60,  83, -62,
    -32,  10,  55,  56,  56,  55,  10,   3,
    -62,  12, -57,  44, -67,  28,  37, -31,
    -55,  50,  11,  -4, -19,  13,   0, -49,
    -55, -43, -52, -28, -51, -47,  -8, -50,
    -47, -42, -43, -79, -64, -32, -29, -32,
    -4,   3, -14, -50, -57, -18,  13,   4,
    17,  30,  -3, -14,   6,  -1,  40,  18
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    0,  10,   7,  -15, -15,  20,  30, -10,
    -10,   5,  10,  20,  20,  10,   5,  -5,
    -10,   8, -10,  25, -10,  15,  20, -10,
    -10,  20,   5,  -5, -10,  10,   0, -15,
    -10, -10, -10,  -5, -15, -10,   0, -10,
    -10,  -5,  -5, -25, -20, -10,  -5, -10,
    0,   5,   0, -10, -10,   0,  10,   5,
    20,  30,   0, -10,  10,   5,  40,  25    
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))

def move_value(board: chess.Board, move: chess.Move, endgame: bool) -> float:
    if move.promotion is not None:
        return -float("inf") if board.turn == chess.BLACK else float("inf")

    _piece = board.piece_at(move.from_square)
    if _piece:
        _from_value = evaluate_piece(_piece, move.from_square, endgame)
        _to_value = evaluate_piece(_piece, move.to_square, endgame)
        position_change = _to_value - _from_value
    else:
        raise Exception(f"A piece was expected at {move.from_square}")

    capture_value = 0.0
    if board.is_capture(move):
        capture_value = evaluate_capture(board, move)

    current_move_value = capture_value + position_change
    if board.turn == chess.BLACK:
        current_move_value = -current_move_value

    return current_move_value


def evaluate_capture(board: chess.Board, move: chess.Move) -> float:
    if board.is_en_passant(move):
        return piece_value[chess.PAWN]
    _to = board.piece_at(move.to_square)
    _from = board.piece_at(move.from_square)
    if _to is None or _from is None:
        raise Exception(
            f"Pieces were expected at _both_ {move.to_square} and {move.from_square}"
        )
    return piece_value[_to.piece_type] - piece_value[_from.piece_type]


def evaluate_piece(piece: chess.Piece, square: chess.Square, end_game: bool) -> int:
    piece_type = piece.piece_type
    mapping = []
    if piece_type == chess.PAWN:
        mapping = pawnEvalWhite if piece.color == chess.WHITE else pawnEvalBlack
    if piece_type == chess.KNIGHT:
        mapping = knightEval
    if piece_type == chess.BISHOP:
        mapping = bishopEvalWhite if piece.color == chess.WHITE else bishopEvalBlack
    if piece_type == chess.ROOK:
        mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
    if piece_type == chess.QUEEN:
        mapping = queenEval
    if piece_type == chess.KING:
        if end_game:
            mapping = (
                kingEvalEndGameWhite
                if piece.color == chess.WHITE
                else kingEvalEndGameBlack
            )
        else:
            mapping = kingEvalWhite if piece.color == chess.WHITE else kingEvalBlack

    return mapping[square]


def evaluate_board(board: chess.Board) -> float:
    total = 0
    end_game = check_end_game(board)

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value = piece_value[piece.piece_type] + evaluate_piece(piece, square, end_game)
        total += value if piece.color == chess.WHITE else -value

    if not board.is_check():
        total += evaluate_king_safety(board, chess.WHITE)
        total -= evaluate_king_safety(board, chess.BLACK)

    total += len(list(board.legal_moves)) * 10
    return total

def evaluate_king_safety(board: chess.Board, color: chess.Color) -> int:
    king_square = board.king(color)
    pawn_shield = 0
    
    if king_square is None:  
        return pawn_shield

    pawn_direction = 8 if color == chess.WHITE else -8
    shield_offsets = [pawn_direction, pawn_direction + 1, pawn_direction - 1]

    for offset in shield_offsets:
        shield_square = king_square + offset
        if chess.A1 <= shield_square <= chess.H8:  
            piece = board.piece_at(shield_square)
            if piece and piece.piece_type == chess.PAWN and piece.color == color:
                pawn_shield += 20     

    return pawn_shield

def check_end_game(board: chess.Board) -> bool:
    queens = 0
    minors = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            queens += 1
        if piece and (
            piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT
        ):
            minors += 1

    if queens == 0 or (queens == 2 and minors <= 1):
        return True

    return False
