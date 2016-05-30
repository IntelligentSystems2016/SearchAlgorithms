#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from eight_game import *
from game_activity import *

def main():
    eight_game = EightGame()
    print(eight_game, '\n')

    game_activity = GameActivity(eight_game)

    ga = game_activity.move_to_right()
    if ga:
        # eg = EightGame(ga)
        print(ga)

if __name__ == '__main__':
    main()
