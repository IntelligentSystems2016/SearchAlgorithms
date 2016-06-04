#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from draw_tree import *
from queens_puzzle import *
from tree import *

def main():

    queens_puzzle = QueensPuzzle(4)
    tree = Tree(queens_puzzle)

    tree.generates_nodes()
    DrawTree(tree)


if __name__ == '__main__':
    main()
