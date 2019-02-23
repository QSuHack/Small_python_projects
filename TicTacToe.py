import numpy as np
from random import choice
import unittest


class OverWriteException(Exception): pass


class FullBoardException(Exception): pass


def get_board():
    for x in board:
        print("")
        for y in x:
            print(y, end=" ")
    print("")


def insert(player_char, x, y):
    if not board[x][y] == "_":
        raise OverWriteException
    board[x][y] = player_char


def start_game():
    print("Gra w kółko i krzyżyk")
    print("Zaczyna:", end=" ")
    player = choice(["X", "O"])
    print(player)
    game(player)


def win(player_char):
    print(player_char, " Wygrał!")
    if input("Chcesz zagrać ponownie? Y/N: ") == "Y":
        start_game()


def game(player):
    if player == "X":
        player2 = "O"
    else:
        player2 = "X"
    while not check(board, player):
        get_board()
        try:
            position = input("Podaj pozycje:").rstrip().split(" ")
            x = int(position[0])
            y = int(position[1])
            insert(player, x, y)
        except (IndexError, ValueError):
            print("Błędne współrzędne pola!")
        except OverWriteException:
            print("Nadpisanie wartości")
            print("Nie oszukuj!")
        try:
            if check(board, player):
                win(player)
                break
        except FullBoardException:
            print("Koniec gry! Remis!")
            win("Nikt nie")
        player, player2 = player2, player


board = np.array([["_", "_", "_", ], ["_", "_", "_"], ["_", "_", "_"]])


# get_board()


def check(board, player_char):
    t = False
    for x in range(0, 3):
        if (board[x, :] == player_char).all():
            return True
        elif (board[:, x] == player_char).all():
            return True
    if (board.diagonal() == player_char).all():
        return True
    elif (np.diag(np.rot90(board)) == player_char).all():
        return True

    if "_" not in board:
        raise FullBoardException
    return False


class TestOfCheck(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.board1 = np.zeros((3, 3), dtype=str)

    def test(self):
        self.assertEqual(check(self.board1, "X"), False)

    def test_a(self):
        self.board1[:, 2] = "X"
        self.assertEqual(check(self.board1, "X"), True)

    def test_b(self):
        self.board1[1, 2] = "X"
        self.assertEqual(check(self.board1, "X"), True)

    def test_c(self):
        self.board1[2, :] = "O"
        print(self.board1)
        self.assertEqual(check(self.board1, "O"), True)


start_game()
