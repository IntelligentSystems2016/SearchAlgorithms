#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from queens_puzzle import *

class GameActivity(object):
    """docstring for GameActivity"""
    def __init__(self, queens_puzzle):
        super(GameActivity, self).__init__()

        # Cópia de um QueensPuzzle
        self.queens_puzzle = copy.deepcopy(queens_puzzle)


    def move_to_left(self, row_pos, squares=None):
        # Cópia dos quadrados originais
        if squares is None:
            squares = copy.deepcopy(self.queens_puzzle.squares)
        else:
            squares = copy.deepcopy(squares)

        for j in range(self.queens_puzzle.size):
            # Se a posição for o quadrado vazio
            if squares[row_pos][j].label == 1:
                if squares[row_pos][j].adjacents['left'].label != -1:
                    # Cópia auxiliar do quadrado vazio
                    sq_aux = copy.deepcopy(squares[row_pos][j])

                    # Troca quadrados de posição
                    squares[row_pos][j] = copy.deepcopy(squares[row_pos][j-1])
                    squares[row_pos][j-1] = copy.deepcopy(sq_aux)

                    return QueensPuzzle(self.queens_puzzle.size, squares)

        return []


    def move_to_right(self, row_pos, squares=None):
        # Cópia dos quadrados originais
        if squares is None:
            squares = copy.deepcopy(self.queens_puzzle.squares)
        else:
            squares = copy.deepcopy(squares)

        for j in range(self.queens_puzzle.size):
            # Se a posição for o quadrado vazio
            if squares[row_pos][j].label == 1:
                if squares[row_pos][j].adjacents['right'].label != -1:
                    # Cópia auxiliar do quadrado vazio
                    sq_aux = copy.deepcopy(squares[row_pos][j])

                    # Troca quadrados de posição
                    squares[row_pos][j] = copy.deepcopy(squares[row_pos][j+1])
                    squares[row_pos][j+1] = copy.deepcopy(sq_aux)

                    return QueensPuzzle(self.queens_puzzle.size, squares)

        return []
