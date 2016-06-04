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


    def shuffle(self):
        """Função responsável por embaralhar o jogo aleatoriamente."""

        # Cópia do gerenciador de jogos
        game_activity = copy.deepcopy(self)

        # Quantidade de movimentos
        shuffle = random.randint(5,15)
        for i in range(shuffle):
            # Repetir enquanto não houver movimento
            while True:
                # Movimento aleatório
                moviment = random.randint(1,4)

                if moviment == 1:
                    eight_game = game_activity.move_to_top()
                elif moviment == 2:
                    eight_game = game_activity.move_to_bottom()
                elif moviment == 3:
                    eight_game = game_activity.move_to_left()
                elif moviment == 4:
                    eight_game = game_activity.move_to_right()

                if eight_game:
                    game_activity.eight_game = copy.deepcopy(eight_game)
                    break

        return eight_game
