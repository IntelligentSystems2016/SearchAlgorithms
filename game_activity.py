#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from eight_game import *

class GameActivity(object):
    """docstring for GameActivity"""
    def __init__(self, eight_game):
        super(GameActivity, self).__init__()

        # Cópia de um EightGame
        self.eight_game = copy.deepcopy(eight_game)


    def move_to_top(self, squares=None):
        # Cópia dos quadrados originais
        if squares is None:
            squares = copy.deepcopy(self.eight_game.squares)
        else:
            squares = copy.deepcopy(squares)

        for i in range(len(squares)):
            for j in range(len(squares[i])):
                # Se a posição for o quadrado vazio
                if squares[i][j].label == 0:
                    if squares[i][j].adjacents['bottom'].label != -1:
                        # Cópia auxiliar do quadrado vazio
                        sq_aux = copy.deepcopy(squares[i][j])

                        squares[i][j] = copy.deepcopy(squares[i+1][j])
                        squares[i+1][j] = copy.deepcopy(sq_aux)

                        return EightGame(squares)

        return []


    def move_to_bottom(self, squares=None):
        # Cópia dos quadrados originais
        if squares is None:
            squares = copy.deepcopy(self.eight_game.squares)
        else:
            squares = copy.deepcopy(squares)

        for i in range(len(squares)):
            for j in range(len(squares[i])):
                # Se a posição for o quadrado vazio
                if squares[i][j].label == 0:
                    if squares[i][j].adjacents['top'].label != -1:
                        # Cópia auxiliar do quadrado vazio
                        sq_aux = copy.deepcopy(squares[i][j])

                        # Troca quadrados de posição
                        squares[i][j] = copy.deepcopy(squares[i-1][j])
                        squares[i-1][j] = copy.deepcopy(sq_aux)

                        return EightGame(squares)

        return []


    def move_to_left(self, squares=None):
        # Cópia dos quadrados originais
        if squares is None:
            squares = copy.deepcopy(self.eight_game.squares)
        else:
            squares = copy.deepcopy(squares)

        for i in range(len(squares)):
            for j in range(len(squares[i])):
                # Se a posição for o quadrado vazio
                if squares[i][j].label == 0:
                    if squares[i][j].adjacents['right'].label != -1:
                        # Cópia auxiliar do quadrado vazio
                        sq_aux = copy.deepcopy(squares[i][j])

                        # Troca quadrados de posição
                        squares[i][j] = copy.deepcopy(squares[i][j+1])
                        squares[i][j+1] = copy.deepcopy(sq_aux)

                        return EightGame(squares)

        return []


    def move_to_right(self, squares=None):
        # Cópia dos quadrados originais
        if squares is None:
            squares = copy.deepcopy(self.eight_game.squares)
        else:
            squares = copy.deepcopy(squares)

        for i in range(len(squares)):
            for j in range(len(squares[i])):
                # Se a posição for o quadrado vazio
                if squares[i][j].label == 0:
                    if squares[i][j].adjacents['left'].label != -1:
                        # Cópia auxiliar do quadrado vazio
                        sq_aux = copy.deepcopy(squares[i][j])

                        # Troca quadrados de posição
                        squares[i][j] = copy.deepcopy(squares[i][j-1])
                        squares[i][j-1] = copy.deepcopy(sq_aux)

                        return EightGame(squares)

        return []
