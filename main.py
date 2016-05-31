#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random
from draw_tree import *
from eight_game import *
from game_activity import *
from square import *
from tree import *

def main():
    eight_game = EightGame()

    shuffle = random.randint(5,20)
    for i in range(shuffle):
        game_activity = GameActivity(eight_game)

        while True:
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
                break


    print(eight_game)

    # eight_game = EightGame([[Square(1), Square(2), Square(3)], [Square(4), Square(8), Square(5)], [Square(0), Square(7), Square(6)]])
    # eight_game = EightGame([[Square(1), Square(2), Square(0)], [Square(4), Square(5), Square(3)], [Square(7), Square(8), Square(6)]])
    # eight_game = EightGame([[Square(1), Square(2), Square(3)], [Square(4), Square(5), Square(0)], [Square(7), Square(8), Square(6)]])

    tree = Tree(eight_game)
    # print('Arvore gerada!')
    tree.search_in_width([tree])
    # tree.search_in_depth(tree)

    DrawTree(tree)


if __name__ == '__main__':
    main()
