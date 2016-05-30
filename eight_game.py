#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import copy
from square import *

class EightGame(object):
    """docstring for EightGame"""
    def __init__(self, squares=None):
        super(EightGame, self).__init__()

        if squares is None:
            initial = Square(-1)
            self.squares = [[initial, initial, initial], [initial, initial, initial], [initial, initial, initial]]
        else:
            self.squares = copy.deepcopy(squares)

        i = 0
        j = 0

        # Tabela estará preenchida quando não existir mais nenhum label '-1'
        while self.existing_label(-1):
            # Cria laels de 0 á 8. Obs: 0 é considerado como o espaço vazio
            label = random.randint(0,8)

            if not self.existing_label(label):
                self.squares[i][j] = Square(label)

                if j == 2:
                    j = 0
                    i += 1
                else:
                    j += 1

        for i in range(3):
            for j in range(3):
                self.squares[i][j].adjacents['top'] = Square(-1)
                self.squares[i][j].adjacents['bottom'] = Square(-1)
                self.squares[i][j].adjacents['left'] = Square(-1)
                self.squares[i][j].adjacents['right'] = Square(-1)

                if i > 0:
                    self.squares[i][j].adjacents['top'] = self.squares[i-1][j]

                if j > 0:
                    self.squares[i][j].adjacents['left'] = self.squares[i][j-1]

                if i < 2:
                    self.squares[i][j].adjacents['bottom'] = self.squares[i+1][j]

                if j < 2:
                    self.squares[i][j].adjacents['right'] = self.squares[i][j+1]

    def existing_label(self, label):
        """ Verificar se determinado label existe na tabela """
        for i in range(3):
            for j in range(3):
                if label == self.squares[i][j].label:
                    return True;

        return False;


    def is_objective(self):
        objective = "0 1 2\n3 4 5\n6 7 8"

        if objective == self.__str__():
            return True;
        else:
            return False;


    def __str__(self):
        """Retorna uma representação em string do jogo"""
        squares_str = str(self.squares[0][0].label)
        squares_str += " "
        squares_str += str(self.squares[0][1].label)
        squares_str += " "
        squares_str += str(self.squares[0][2].label)
        squares_str += "\n"

        squares_str += str(self.squares[1][0].label)
        squares_str += " "
        squares_str += str(self.squares[1][1].label)
        squares_str += " "
        squares_str += str(self.squares[1][2].label)
        squares_str += "\n"

        squares_str += str(self.squares[2][0].label)
        squares_str += " "
        squares_str += str(self.squares[2][1].label)
        squares_str += " "
        squares_str += str(self.squares[2][2].label)

        # """Retorna uma representação em string do jogo com os adjacentes"""
        # squares_str = str(self.squares[0][0].label)
        # squares_str += str(self.squares[0][0])
        # squares_str += "\t"
        # squares_str += str(self.squares[0][1].label)
        # squares_str += str(self.squares[0][1])
        # squares_str += "\t"
        # squares_str += str(self.squares[0][2].label)
        # squares_str += str(self.squares[0][2])
        # squares_str += "\n"
        #
        # squares_str += str(self.squares[1][0].label)
        # squares_str += str(self.squares[1][0])
        # squares_str += "\t"
        # squares_str += str(self.squares[1][1].label)
        # squares_str += str(self.squares[1][1])
        # squares_str += "\t"
        # squares_str += str(self.squares[1][2].label)
        # squares_str += str(self.squares[1][2])
        # squares_str += "\n"
        #
        # squares_str += str(self.squares[2][0].label)
        # squares_str += str(self.squares[2][0])
        # squares_str += "\t"
        # squares_str += str(self.squares[2][1].label)
        # squares_str += str(self.squares[2][1])
        # squares_str += "\t"
        # squares_str += str(self.squares[2][2].label)
        # squares_str += str(self.squares[2][2])

        return squares_str
