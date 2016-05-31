#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import time
from game_activity import *
from random import shuffle

class Tree(object):
    """docstring for Tree"""

    global is_finished
    is_finished = False

    def __init__(self, eight_game, generated_trees=[]):
        super(Tree, self).__init__()
        # Id gerado automaticamente
        self.id = time.time()

        # Tabela com o jogo atual
        self.eight_game = copy.deepcopy(eight_game)

        # Lista com resultado do jogo após os possíveis movimentos serem feitos
        self.childrens = []

        # Indica se o nó foi ou não marcado
        self.is_visited = False

        # Indica se o nó é ou não objetivo
        self.is_objective = False

        # Nós gerados até o momento
        if not str(eight_game) in generated_trees:
            generated_trees.append(str(eight_game))
        self.generated_trees = copy.deepcopy(generated_trees)


    def generates_nodes(self):
        # Gerenciador de movimentos do jogo
        game_activity = GameActivity(self.eight_game)

        # Possíveis movimentos a serem feitos
        top = game_activity.move_to_top()
        bottom = game_activity.move_to_bottom()
        left = game_activity.move_to_left()
        right = game_activity.move_to_right()

        #
        # while '[]' in generated:
        #     generated.remove('[]')

        generated = []

        if top and not str(top) in self.generated_trees:
            top = Tree(top, self.generated_trees)
            generated.append(str(top))
            self.childrens.append(top)

        if  bottom and not str(bottom) in self.generated_trees:
            bottom = Tree(bottom, self.generated_trees)
            generated.append(str(bottom))
            self.childrens.append(bottom)

        if  left and not str(left) in self.generated_trees:
            left = Tree(left, self.generated_trees)
            generated.append(str(left))
            self.childrens.append(left)

        if  right and not str(right) in self.generated_trees:
            right = Tree(right, self.generated_trees)
            generated.append(str(right))
            self.childrens.append(right)

        self.generated_trees += generated
        shuffle(self.childrens)


    def search_in_width(self, trees):
        """Preenche árvore e faz uma busca em largura pelo objetivo"""

        if trees:
            # Verifica se algum dos nós gera o nó obejetivo
            for tree in trees:
                # Marca nó atual como visitado
                tree.is_visited = True
                # Verifica se o jogo atual é o objetivo
                if tree.eight_game.is_objective():
                    # Marca nó atual como objetivo
                    tree.is_objective = True
                    return

            # Lista auxiliar para colocar os nós do próximo nível
            list_trees = []

            # Gera todos os nós do próximo nível
            for tree in trees:
                tree.generates_nodes()
                list_trees += tree.childrens

            # Recursão para desenhar sub-árvore de filhos
            self.search_in_width(list_trees)


    def search_in_depth(self, tree):
        """Preenche árvore e faz uma busca em largura pelo objetivo"""

        global is_finished

        if tree:
            # Marca nó atual como visitado
            tree.is_visited = True
            # Verifica se o jogo atual é o objetivo
            if tree.eight_game.is_objective():
                # Marca nó atual como objetivo
                tree.is_objective = True
                is_finished = True
                return

            # Gera os nós do próximo nível
            tree.generates_nodes()

            # Gera todos os nós do próximo nível
            for child in tree.childrens:
                # Recursão para desenhar sub-árvore de filhos
                if is_finished:
                    return
                else:
                    self.search_in_depth(child)


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
