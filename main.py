#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from draw_tree import *
from eight_game import *
from game_activity import *
from tree import *

def main():
    eight_game = EightGame()

    tree = Tree(eight_game)
    print('Arvore gerada!')

    DrawTree(tree)


if __name__ == '__main__':
    main()
