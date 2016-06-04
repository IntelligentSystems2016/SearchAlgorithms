#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random
from square import *

class QueensPuzzle(object):
    """docstring for QueensPuzzle"""
    def __init__(self, size, squares=None):
        super(QueensPuzzle, self).__init__()

        self.size = size

        if squares is None:
            # Cria lista vazia
            self.squares = []

            for i in range(self.size):
                # Adiciona nova lista vazia
                self.squares.append([])

                # Adiciona quadrados com label 0
                for j in range(self.size):
                    self.squares[i].append(Square(0))

                # Coloca rainha em coluna aleatória
                pos = random.randint(0,self.size - 1)
                self.squares[i][pos] = Square(1)
        else:
            self.squares = copy.deepcopy(squares)

        for i in range(self.size):
            for j in range(self.size):
                self.squares[i][j].adjacents['left_top'] = Square(-1)
                self.squares[i][j].adjacents['top'] = Square(-1)
                self.squares[i][j].adjacents['right_top'] = Square(-1)
                self.squares[i][j].adjacents['left_bottom'] = Square(-1)
                self.squares[i][j].adjacents['bottom'] = Square(-1)
                self.squares[i][j].adjacents['right_bottom'] = Square(-1)
                self.squares[i][j].adjacents['left'] = Square(-1)
                self.squares[i][j].adjacents['right'] = Square(-1)

                if i > 0:
                    if j > 0:
                        self.squares[i][j].adjacents['left_top'] = self.squares[i-1][j-1]

                if i > 0:
                    self.squares[i][j].adjacents['top'] = self.squares[i-1][j]

                if i > 0:
                    if j < self.size - 1:
                        self.squares[i][j].adjacents['right_top'] = self.squares[i-1][j+1]

                if j > 0:
                    self.squares[i][j].adjacents['left'] = self.squares[i][j-1]

                if i < self.size - 1:
                    if j > 0:
                        self.squares[i][j].adjacents['left_bottom'] = self.squares[i+1][j-1]

                if i < self.size - 1:
                    self.squares[i][j].adjacents['bottom'] = self.squares[i+1][j]

                if i < self.size - 1:
                    if j < self.size - 1:
                        self.squares[i][j].adjacents['right_bottom'] = self.squares[i+1][j+1]

                if j < self.size - 1:
                    self.squares[i][j].adjacents['right'] = self.squares[i][j+1]


    def is_objective(self):
        count = [0] * self.size

        for i in range(self.size):
            for j in range(self.size):
                # Soma a quantidade de rainhas por coluna
                count[j] += self.squares[i][j].label

                # Se alguma das colunas tiver(em) mais de uma rainha
                if count[j] > 1:
                    return False

                # Se for uma rainha
                if self.squares[i][j].label == 1:
                    i_diag = i
                    j_diag_l = j    # Esquerda
                    j_diag_r = j    # Direita
                    count_diag = 0
                    while i_diag >= 0:
                        i_diag -= 1
                        j_diag_l -=1
                        j_diag_r +=1

                        if j_diag_l >= 0:
                            count_diag += self.squares[i_diag][j_diag_l].label

                        if j_diag_r < self.size:
                            count_diag += self.squares[i_diag][j_diag_r].label

                        # Se houver alguma rainha na diagonal
                        if count_diag > 1:
                            return False

                    i_diag = i
                    j_diag_l = j    # Esquerda
                    j_diag_r = j    # Direita
                    count_diag = 0
                    while i_diag < self.size - 1:
                        i_diag += 1
                        j_diag_l -=1
                        j_diag_r +=1

                        if j_diag_l >= 0:
                            count_diag += self.squares[i_diag][j_diag_l].label

                        if j_diag_r < self.size:
                            count_diag += self.squares[i_diag][j_diag_r].label

                        # Se houver alguma rainha na diagonal
                        if count_diag > 1:
                            return False


        return True


    def __str__(self):
        """Retorna uma representação em string do jogo"""
        squares_str = ""

        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j].label == 1:
                    # squares_str += chr(169)
                    squares_str += "®"
                else:
                    squares_str += "_"
                # squares_str += str(self.squares[i][j].label)
                if j != self.size - 1:
                    squares_str += " "
                else:
                    squares_str += "\n"

        return squares_str
