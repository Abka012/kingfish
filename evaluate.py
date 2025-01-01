import chess

piece_value = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

pawnEvalWhite = [
    0,  0,  0,  0,  0,  0,  0,  0,
    5, 10, 10,-20,-20, 10, 10,  5,
    5, -5,-10,  0,  0,-10, -5,  5,
    0,  0,  0, 20, 20,  0,  0,  0,
    5,  5, 10, 25, 25, 10,  5,  5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0,  0,  0,  0,  0,  0,  0,  0
]
pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEvalWhite = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20,   0,   5,   5,   0, -20, -40,
    -30,   5,  10,  15,  15,  10,   5, -30,
    -30,   0,  15,  20,  20,  15,   0, -30,
    -30,   5,  15,  20,  20,  15,   5, -30,
    -30,   0,  10,  15,  15,  10,   0, -30,
    -40, -20,   0,   0,   0,   0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50
]
knightEvalBlack = list(reversed(knightEvalWhite))

bishopEvalWhite = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10,   5,   0,   0,   0,   0,   5, -10,
    -10,  10,  10,  10,  10,  10,  10, -10,
    -10,   0,  10,  10,  10,  10,   0, -10,
    -10,   5,   5,  10,  10,   5,   5, -10,
    -10,   0,   5,  10,  10,   5,   0, -10,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20
]
bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    0,   0,   0,   5,   5,   0,   0,   0,
   -5,   0,   0,   0,   0,   0,   0,  -5,
   -5,   0,   0,   0,   0,   0,   0,  -5,
   -5,   0,   0,   0,   0,   0,   0,  -5,
   -5,   0,   0,   0,   0,   0,   0,  -5,
   -5,   0,   0,   0,   0,   0,   0,  -5,
    5,  10,  10,  10,  10,  10,  10,   5,
    0,   0,   0,   0,   0,   0,   0,   0
]
rookEvalBlack = list(reversed(rookEvalWhite))

queenEvalWhite = [
    -20, -10, -10,  -5,  -5, -10, -10, -20,
    -10,   0,   5,   0,   0,   0,   0, -10,
    -10,   5,   5,   5,   5,   5,   0, -10,
      0,   0,   5,   5,   5,   5,   0,  -5,
     -5,   0,   5,   5,   5,   5,   0,  -5,
    -10,   0,   5,   5,   5,   5,   0, -10,
    -10,   0,   0,   0,   0,   0,   0, -10,
    -20, -10, -10,  -5,  -5, -10, -10, -20
]
queenEvalBlack = list(reversed(queenEvalWhite))

kingEvalWhite = [
     20,  30,  10,   0,   0,  10,  30,  20,
     20,  20,   0,   0,   0,   0,  20,  20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30
]
kingEvalBlack = list(reversed(kingEvalWhite))

kingEvalEndGameWhite = [
    -50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30,   0,   0,   0,   0, -30, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  30,  40,  40,  30, -10, -30,
    -30, -10,  20,  30,  30,  20, -10, -30,
    -30, -20, -10,   0,   0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50 
]
kingEvalEndGameBlack = list(reversed(kingEvalEndGameWhite))

def evaluate_piece(piece: chess.Piece, square: chess.Square, end_game: bool) -> int:
    piece_type = piece.piece_type
    mapping = []
    
    if piece_type == chess.PAWN:
        mapping = pawnEvalWhite if piece.color == chess.WHITE else pawnEvalBlack
         
        
    elif piece_type == chess.KNIGHT:
        mapping = knightEvalWhite if piece.color == chess.WHITE else knightEvalBlack
        
    elif piece_type == chess.BISHOP:
        mapping = bishopEvalWhite if piece.color == chess.WHITE else bishopEvalBlack
          

    elif piece_type == chess.ROOK:
        mapping = rookEvalWhite if piece.color == chess.WHITE else rookEvalBlack
        

    elif piece_type == chess.QUEEN:
        mapping = queenEvalWhite if piece.color == chess.WHITE else queenEvalBlack
        

    elif piece_type == chess.KING:
        if end_game:
            mapping = kingEvalEndGameWhite if piece.color == chess.WHITE else kingEvalEndGameBlack
        else:
            mapping = kingEvalWhite if piece.color == chess.WHITE else kingEvalBlack
        
    return mapping[square]

def evaluate_capture(board: chess.Board, move: chess.Move) -> float:
    if board.is_en_passant(move):
        return piece_value[chess.PAWN]
    captured_piece = board.piece_at(move.to_square)
    capturing_piece = board.piece_at(move.from_square)
    if captured_piece and capturing_piece:
        return piece_value[captured_piece.piece_type] - piece_value[capturing_piece.piece_type]
    return 0.0


def evaluate_king_safety(board: chess.Board, color: chess.Color) -> int:
    king_square = board.king(color)
    if king_square is None:
        return 0

    pawn_direction = 8 if color == chess.WHITE else -8
    shield_offsets = [pawn_direction, pawn_direction + 1, pawn_direction - 1]
    pawn_shield = 0

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
        if piece and piece.piece_type in {chess.BISHOP, chess.KNIGHT}:
            minors += 1
    return queens == 0 or (queens == 2 and minors <= 1)


def evaluate_board(board: chess.Board) -> float:
    total = 0.0
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

    mobility = len(list(board.legal_moves))
    total += mobility * 10 if board.turn == chess.WHITE else -mobility * 10
    return total


def move_value(board: chess.Board, move: chess.Move) -> float:
    if move.promotion is not None:
        return -float("inf") if board.turn == chess.BLACK else float("inf")

    _piece = board.piece_at(move.from_square)
    if _piece:
        _from_value = evaluate_piece(_piece, move.from_square, check_end_game(board))
        _to_value = evaluate_piece(_piece, move.to_square, check_end_game(board))
        position_change = _from_value - _to_value
        print(f"Move {move} from {_from_value} to {_to_value}, position change: {position_change}")
    else:
        raise Exception(f"A piece was expected at {move.from_square}")

    capture_value = 0.0
    if board.is_capture(move):
        capture_value = evaluate_capture(board, move)
        print(f"Capture value: {capture_value}")

    current_move_value = capture_value + position_change
    if board.turn == chess.BLACK:
        current_move_value = -current_move_value

    print(f"Move value for {move}: {current_move_value}")
    return current_move_value
