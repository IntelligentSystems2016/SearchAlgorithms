#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import time
from draw_tree import *
from queens_puzzle import *
from tree import *

"""
pip install -U memory_profiler
python -m memory_profiler main.py

@profile antes da função
"""
@profile
def main():

    ini = time.time()

    # queens_puzzle = QueensPuzzle(8,[[Square(1),Square(0),Square(0),Square(0),Square(0),Square(0),Square(0),Square(0)],[Square(0),Square(0),Square(0),Square(0),Square(1),Square(0),Square(0),Square(0)],[Square(0),Square(0),Square(0),Square(0),Square(0),Square(0),Square(0),Square(1)],[Square(0),Square(0),Square(0),Square(0),Square(0),Square(1),Square(0),Square(0)],[Square(0),Square(0),Square(1),Square(0),Square(0),Square(0),Square(0),Square(0)],[Square(0),Square(0),Square(0),Square(0),Square(0),Square(0),Square(1),Square(0)],[Square(0),Square(1),Square(0),Square(0),Square(0),Square(0),Square(0),Square(0)],[Square(0),Square(0),Square(0),Square(1),Square(0),Square(0),Square(0),Square(0)]])
    queens_puzzle = QueensPuzzle(8)

    tree = Tree(queens_puzzle)
    # tree.is_visited = True

    # # Busca em largura
    # tree.search_in_width()

    # # Busca em profundidade
    # tree.search_in_depth()

    # Busca com Algoritmo A*
    tree.search_in_A()

    # # Busca gulosa
    # tree.search_greedy()

    # DrawTree(tree)

    fim = time.time()
    print("Tempo TOTAL =", fim - ini, "segundos")

if __name__ == '__main__':
    main()
