"""
Name: XXX
Student ID: XXX
"""

from utils import *

class Board():
    def __init__(self):
        self.state = ['.' for i in range(16)]
        self.mills = [[0, 1, 2], [3, 4, 5], [10, 11, 12], [13, 14, 15],
                      [0, 6, 13], [3, 7, 10], [5, 8, 12], [2, 9, 15]]
        # This parameter pre-defines all possible situations of mills on the board.
        self.edges = [[0, 1], [1, 2],
                      [3, 4], [4, 5],
                      [6, 7], [8, 9],
                      [10, 11], [11, 12],
                      [13, 14], [14, 15],
                      [0, 6], [6, 13],
                      [3, 7], [7, 10],
                      [1, 4], [11, 14],
                      [5, 8], [8, 12],
                      [2, 9], [9, 15]]
        # This parameter pre-defines all possible situations of connectivity of edges on the board.

    def print_board(self):
        def color(x):
            if x == '.': return x
            return g(x) if x == '#' else b(x)

        print(color(self.state[0]), '-' * 9, color(self.state[1]), '-' * 9, color(self.state[2]), end='    ');
        print('a', '-' * 9, 'b', '-' * 9, 'c')
        print('|   ', ' ' * 6, '|', ' ' * 6, '   |', end='    ');
        print('|   ', ' ' * 6, '|', ' ' * 6, '   |')
        print('|   ', color(self.state[3]), '-' * 4, color(self.state[4]), '-' * 4, color(self.state[5]), '   |', end='    ');
        print('|   ', 'd', '-' * 4, 'e', '-' * 4, 'f', '   |')
        print('|   ' * 2, ' ' * 7, '   |' * 2, end='    ');
        print('|   ' * 2, ' ' * 7, '   |' * 2)
        print(color(self.state[6]), '-', color(self.state[7]), ' ' * 13, color(self.state[8]), '-', color(self.state[9]), end='    ');
        print('g', '-', 'h', ' ' * 13, 'i', '-', 'j', )
        print('|   ' * 2, ' ' * 7, '   |' * 2, end='    ');
        print('|   ' * 2, ' ' * 7, '   |' * 2)
        print('|   ', color(self.state[10]), '-' * 4, color(self.state[11]), '-' * 4, color(self.state[12]), '   |', end='    ');
        print('|   ', 'k', '-' * 4, 'l', '-' * 4, 'm', '   |')
        print('|   ', ' ' * 6, '|', ' ' * 6, '   |', end='    ');
        print('|   ', ' ' * 6, '|', ' ' * 6, '   |')
        print(color(self.state[13]), '-' * 9, color(self.state[14]), '-' * 9, color(self.state[15]), end='    ');
        print('n', '-' * 9, 'o', '-' * 9, 'p')

    def check_put(self, pos):
        """
        This function checks whether the PUT-movement is a legal movement. 
        The input arguments are the putting position.
        The output is a boolean variable.
        """
        valid_flag = True

        ### TODO DONE
        if self.state[pos] != '.':
            valid_flag = False

        return valid_flag

    def check_move(self, s, t, player):
        """
        This function checks whether the MOVE-movement is a legal movement for the player. 
        The input arguments are the source position, the target position, and the player. 
        The output is a boolean variable.
        """
        valid_flag = True
        if s < 0 or s > 15 or t < 0 or t > 15:
            valid_flag = False

        ### TODO DONE

        elif self.state[s] != player.get_symbol() or self.state[t] != '.':
            valid_flag = False

        else:
            path = {
                0: lambda d: d == 1 or d == 6,
                1: lambda d: d == 0 or d == 2 or d == 4,
                2: lambda d: d == 1 or d == 9,
                3: lambda d: d == 4 or d == 7,
                4: lambda d: d == 1 or d == 3 or d == 5,
                5: lambda d: d == 4 or d == 8,
                6: lambda d: d == 0 or d == 7 or d == 13,
                7: lambda d: d == 3 or d == 6 or d == 10,
                8: lambda d: d == 5 or d == 9 or d == 12,
                9: lambda d: d == 2 or d == 8 or d == 15,
                10: lambda d: d == 7 or d == 11,
                11: lambda d: d == 10 or d == 12 or d == 14,
                12: lambda d: d == 8 or d == 11,
                13: lambda d: d == 6 or d == 14,
                14: lambda d: d == 11 or d == 13 or d == 15,
                15: lambda d: d == 9 or d == 14,
            }
            valid_flag = path[s](t)

        return valid_flag

    def check_remove(self, pos, player):
        """
        This function checks whether the REMOVE-movement is a legal movement for the player. 
        The input arguments are the position on which the piece is expected to be removed and the player. 
        The output is a boolean variable.
        """
        valid_flag = True
        if pos < 0 or pos > 15:
            valid_flag = False

        ### TODO DONE
        ### player is opponent
        elif self.state[pos] != player.get_symbol():
            valid_flag = False

        return valid_flag

    def put_piece(self, pos, player):
        """This function does the PUT-movement on the board without checking. 
        """
        ### TODO DONE
        if self.check_put(pos):
            self.state[pos] = player.get_symbol()
        else:
            print('Invalid Put-Movement.')

    def move_piece(self, s, t, player):
        """This function does the MOVE-movement on the board without checking.
        """
        ### TODO DONE
        if self.check_move(s, t, player):
            self.state[t] = player.get_symbol()
            self.state[s] = '.'
        else:
            print('Invalid Move-Movement.')

    def remove_piece(self, pos, player):
        """This function does the REMOVE-movement on the board without checking.
        """
        self.state[pos] = '.'

    def form_mill(self, pos, player):
        """
        This function returns a Boolean variable that represents whether it forms a mill at this position for the player.
        """
        if_form = False

        ### TODO DONE
        for mile in self.mills:
            if pos in mile:
                count = 0
                for point in mile:
                    if point != pos and self.state[point] == player.get_symbol():
                        count += 1
                if count == 2:
                    return True

        return if_form

    def check_win(self, player, opponent):
        """
        This function returns a boolean variable that represents whether the current player wins. 
        If the current player wins the game, then it returns True. Otherwise, it returns False. 
        """
        if_win = False

        # Winning condition 1
        # check whether the opponent has less than 2 pieces. 
        num_pieces = 0

        ### TODO DONE (check every position to calculate the number of pieces for the player)
        for point in self.state:
            if point == opponent.get_symbol():
                num_pieces += 1

        if num_pieces <= 2:
            if_win = True
        else:
            # Winning condition 2
            # check whether the opponent cannot move

            can_move = False
            for i in range(len(self.state)):
                if self.state[i] == opponent.get_symbol():
                    piece_can_move = False
                    symbol = opponent.get_symbol()
                    for j, k in self.edges:
                        ### TODO DONE (check every edge to check whether there is a legal move)
                        j = self.state[j]
                        k = self.state[k]
                        if j == symbol or k == symbol:
                            if j == '.' or k == '.':
                                piece_can_move = True
                                break

                    if piece_can_move:
                        can_move = True
                        break
            if not can_move:
                if_win = True

        return if_win
