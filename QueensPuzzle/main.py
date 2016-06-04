#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from queens_puzzle import *

def main():

    queens_puzzle = QueensPuzzle(4)
    print(queens_puzzle)
    print(queens_puzzle.is_objective())


if __name__ == '__main__':
    main()
