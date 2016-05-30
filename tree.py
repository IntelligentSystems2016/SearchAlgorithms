#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import time
from game_activity import *

class Tree(object):
    """docstring for Tree"""

    def __init__(self, eight_game, tree_parent=None):
        super(Tree, self).__init__()
        # Id gerado automaticamente
        self.id = time.time()

        # Tabela com o jogo atual
        self.eight_game = copy.deepcopy(eight_game)

        # Lista com resultado do jogo após os possíveis movimentos serem feitos
        self.childrens = []

        # Pai do nó atual
        self.tree_parent = copy.deepcopy(tree_parent)


    def generates_nodes(self):
        # Gerenciador de movimentos do jogo
        game_activity = GameActivity(self.eight_game)

        # Possíveis movimentos a serem feitos
        top = game_activity.move_to_top()
        bottom = game_activity.move_to_bottom()
        left = game_activity.move_to_left()
        right = game_activity.move_to_right()

        if top:
            top = Tree(top, copy.deepcopy(self))
            if not top.parent_equal():
                self.childrens.append(top)
        if bottom:
            bottom = Tree(bottom, copy.deepcopy(self))
            if not bottom.parent_equal():
                self.childrens.append(bottom)
        if left:
            left = Tree(left, copy.deepcopy(self))
            if not left.parent_equal():
                self.childrens.append(left)
        if right:
            right = Tree(right, copy.deepcopy(self))
            if not right.parent_equal():
                self.childrens.append(right)


    def parent_equal(self):
        """ Verifica se algum dos seu nós antecessores é igual a ele mesmo. """

        # Cópia do pai do jogo atual
        parent = copy.deepcopy(self.tree_parent)

        # Enquanto não chegar na raiz
        while not parent is None:
            # Se o jogo de um antecessor for igual, retorna verdadeiro
            if str(parent.eight_game) == str(self.eight_game):
                return True
            else:
                # Cópia do pai de um antecessor
                parent = copy.deepcopy(parent.tree_parent)

        return False


    def __str__(self):
        """Retorna uma representação em string da árvore"""
        # tree_str = str(self.eight_game)
        # tree_str += '\n  |\n'
        tree_str = ''
        for i in range(len(self.childrens)):
            tree_str += str(self.childrens[i].eight_game)
            tree_str += '\n -' + str(i) + '-\n'
            tree_str += '\t' + str(self.childrens[i])

        return tree_str
