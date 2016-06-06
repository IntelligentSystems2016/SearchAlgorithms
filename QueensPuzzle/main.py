#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import time
from draw_tree import *
from queens_puzzle import *
from tree import *

def main():

    ini = time.time()

    queens_puzzle = QueensPuzzle(8)
    # print(queens_puzzle)

    tree = Tree(queens_puzzle)
    # print(tree.queens_puzzle.is_objective())

    tree.search_in_width()
    DrawTree(tree)

    fim = time.time()
    print("Tempo TOTAL =", fim - ini, "segundos")

if __name__ == '__main__':
    main()
