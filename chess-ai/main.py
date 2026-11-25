import chess
from engine.evaluation import evaluate

def main():
    # create a new chessboard
    board = chess.Board()

    print("<<<< Starting Postion >>>>")
    print(board)
    print(f"Evaluation: {evaluate(board)}")

    # cool shorthand sanity check
    assert evaluate(board) == 0

    # playing a few moves
    board.push_san("e4")
    board.push_san("d5")
    board.push_san("exd5")

    print("\n<<<< After 1.3f d5 2.exd5 >>>>")
    print(board)
    print(f"Evaluation: {evaluate(board)}")


    # white capture 1 black pawn
    assert evaluate(board) == 100
    print("\nAll evaluation tests passed!")
    

if __name__ == "__main__":
    main()