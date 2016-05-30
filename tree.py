#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from game_activity import *

class Tree(object):
    """docstring for Tree"""
    def __init__(self, eight_game):
        super(Tree, self).__init__()
        # Tabela com o jogo atual
        self.eight_game = copy.deepcopy(eight_game)

        # Lista com os possíveis movimentos a serem feitos
        self.list_tree = []

        # Gerenciador de movimentos do jogo
        game_activity = GameActivity(self.eight_game)

        # Possíveis movimentos a serem feitos
        top = game_activity.move_to_top()
        bottom = game_activity.move_to_bottom()
        left = game_activity.move_to_left()
        right = game_activity.move_to_right()

        if top:
            self.list_tree.append(top)
        if bottom:
            self.list_tree.append(bottom)
        if left:
            self.list_tree.append(left)
        if right:
            self.list_tree.append(right)


    def __str__(self):
        """Retorna uma representação em string da árvore"""
        tree_str = str(self.eight_game)
        tree_str += '\n  |\n'
        for i in range(len(self.list_tree)):
            tree_str += str(self.list_tree[i])
            tree_str += '\n -' + str(i) + '-\n'

        return tree_str
