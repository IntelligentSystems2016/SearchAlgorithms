#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random
from draw_tree import *
from eight_game import *
from game_activity import *
from square import *
from tree import *
from tree import *

"""
pip install -U memory_profiler
python -m memory_profiler main.py

@profile antes da função
"""
@profile
def main():

    ini = time.time()
    eight_game = GameActivity(EightGame()).shuffle()

    #OI

    """Exemplos de entrada"""
    # eight_game = EightGame([[Square(1), Square(2), Square(3)], [Square(4), Square(8), Square(5)], [Square(0), Square(7), Square(6)]])
    # eight_game = EightGame([[Square(1), Square(2), Square(3)], [Square(8), Square(6), Square(4)], [Square(0), Square(7), Square(5)]])
    # eight_game = EightGame([[Square(1), Square(2), Square(0)], [Square(4), Square(5), Square(3)], [Square(7), Square(8), Square(6)]])
    # eight_game = EightGame([[Square(1), Square(2), Square(3)], [Square(4), Square(5), Square(0)], [Square(7), Square(8), Square(6)]])

    # Árvore criada a partir do jogo inicial
    tree = Tree(eight_game)

    # # Busca em largura
    # tree.search_in_width()

    # # Busca em profundidade
    # tree.search_in_depth()

    # # Busca com Algoritmo A*
    # tree.search_in_A()

    # Busca gulosa
    tree.search_greedy()

    DrawTree(tree)

    fim = time.time()
    print("Tempo TOTAL =", fim - ini, "segundos")


if __name__ == '__main__':
    main()
