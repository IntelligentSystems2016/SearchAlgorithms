#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random

class QueensPuzzle(object):
    """docstring for QueensPuzzle"""
    def __init__(self, size, squares=None, queens_positions=[]):
        super(QueensPuzzle, self).__init__()

        # Quantidade de rainhas no jogo
        self.size = size

        # Lista de posições onde se encontram as rainhas
        self.queens_positions = queens_positions

        # Quantidade de rainhas no jogo
        self.qntd_queens = 0

        if squares is None:
            # Cria lista vazia
            self.squares = []

            for i in range(self.size):
                # Adiciona nova lista vazia
                self.squares.append([])

                # Adiciona quadrados com label 0
                for j in range(self.size):
                    self.squares[i].append(0)

            self.squares[0][0] = 1
            self.queens_positions.append([0,0])
            self.qntd_queens += 1
        else:
            self.squares = copy.deepcopy(squares)


    def is_objective(self):

        if self.qntd_queens == self.size:
            return True

        return False


    def is_check(self, pos_x, pos_y):

        for pos in self.queens_positions:

            queen_pos_x = pos[0]
            queen_pos_y = pos[1]

            # Mesma coluna
            if queen_pos_x == pos_x:
                return True

            # Mesma linha
            if queen_pos_y == pos_y:
                return True

            # Diagonal secundária
            if (queen_pos_y-queen_pos_x) == (pos_y-pos_x):
                return True

            # Diagonal principal
            if (queen_pos_y+queen_pos_x) == (pos_y+pos_x):
                return True

        return False



    def __str__(self):
        """Retorna uma representação em string do jogo"""
        squares_str = ""

        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j] == 1:
                    # squares_str += chr(169)
                    squares_str += "®"
                else:
                    squares_str += "_"
                # squares_str += str(self.squares[i][j])
                if j != self.size - 1:
                    squares_str += " "
                else:
                    squares_str += "\n"

        return squares_str
