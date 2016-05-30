#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from draw_tree import *
from eight_game import *
from game_activity import *
from square import *
from tree import *

def main():
    eight_game = EightGame([[Square(1), Square(2), Square(3)], [Square(4), Square(8), Square(5)], [Square(0), Square(7), Square(6)]])

    tree = Tree(eight_game)
    # print('Arvore gerada!')
    tree.search_in_width([tree])

    DrawTree(tree)


if __name__ == '__main__':
    main()
