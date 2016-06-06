#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import time
from random import shuffle

class Tree(object):
    """docstring for Tree"""

    def __init__(self, queens_puzzle):
        super(Tree, self).__init__()
        # Id gerado automaticamente
        self.id = time.time()

        # Tabela com o jogo atual
        self.queens_puzzle = copy.deepcopy(queens_puzzle)

        # Lista com resultado do jogo após os possíveis movimentos serem feitos
        self.childrens = []

        # Indica se o nó foi ou não marcado
        self.is_visited = False

        # Indica se o nó é ou não objetivo
        self.is_objective = False

        # Variável utilizada apenas nos Algoritmos A* e Guloso
        self.path_cost = 0


    def generates_nodes(self):
        for i in range(self.queens_puzzle.size):
            for j in range(self.queens_puzzle.size):

                if not self.queens_puzzle.is_check(i,j):

                    moved = copy.deepcopy(self.queens_puzzle)
                    moved.squares[i][j].label = 1
                    moved.queens_positions.append([i,j])
                    moved.qntd_queens += 1

                    moved = Tree(moved)
                    self.childrens.append(moved)

        # shuffle(self.childrens)


    def search_in_width(self):
        """Preenche árvore e faz uma busca em largura pelo objetivo"""

        # Lista auxiliar para colocar os nós do próximo nível
        list_trees = []
        tree = self

        while True:
            # Marca nó atual como visitado
            tree.is_visited = True
            # Verifica se o jogo atual é o objetivo
            if tree.queens_puzzle.is_objective():
                # Marca nó atual como objetivo
                tree.is_objective = True
                print(tree.queens_puzzle)
                return
            else:
                # Gera todos os nós do próximo nível
                tree.generates_nodes()
                list_trees += tree.childrens

            if not list_trees:
                print('Não foi possível encontrar solução!!')
                return

            tree = list_trees[0]
            del list_trees[0]


    def search_in_depth(self):
        """Preenche árvore e faz uma busca em profundidade pelo objetivo"""

        global is_finished

        queue = []
        tree = self

        while True:
            # Marca nó atual como visitado
            tree.is_visited = True

            # Verifica se o jogo atual é o objetivo
            if tree.queens_puzzle.is_objective():
                # Marca nó atual como objetivo
                tree.is_objective = True
                return
            else:
                # Gera os nós do próximo nível
                tree.generates_nodes()
                queue = tree.childrens + queue

            if not queue:
                print('Não foi possível encontrar solução!!')
                return

            tree = queue[0]
            del queue[0]


    def search_in_A(self):
        """Preenche árvore e faz uma busca com Algoritmos A* pelo objetivo"""

        tree = self
        # Marca nó raiz como visitado
        tree.is_visited = True

        # Lista auxiliar para colocar os nós do próximo nível
        list_trees = []

        while True:
            # Verifica se o jogo atual é o objetivo
            if tree.queens_puzzle.is_objective():
                # Marca nó atual como objetivo
                tree.is_objective = True
                return
            else:

                # Gera os nós do próximo nível
                tree.generates_nodes()

                for child in tree.childrens:
                    # Todos os nós filhos são tidos como visitados
                    child.is_visited = True
                    # Todos os nós filhos iniciam com o custo igual ao do seu pai
                    child.path_cost = tree.path_cost

                # Insere filhos na lista
                list_trees += tree.childrens
                self.sort_distance(list_trees)

            # Testa se a lista está vazia
            if not list_trees:
                print('Não foi possível encontrar solução!!')
                return

            tree = list_trees[0]
            del list_trees[0]


    def search_greedy(self):
        """Preenche árvore e faz uma busca gulosa pelo objetivo"""

        tree = self
        # Marca nó raiz como visitado
        tree.is_visited = True


        while True:
            # Verifica se o jogo atual é o objetivo
            if tree.queens_puzzle.is_objective():
                # Marca nó atual como objetivo
                tree.is_objective = True
                return
            else:
                # Lista auxiliar para colocar os nós do próximo nível
                list_trees = []

                # Gera os nós do próximo nível
                tree.generates_nodes()

                for child in tree.childrens:
                    # Todos os nós filhos são tidos como visitados
                    child.is_visited = True

                # Insere filhos na lista
                list_trees += tree.childrens
                self.sort_distance(list_trees)

            # Testa se a lista está vazia
            if not list_trees:
                print('Não foi possível encontrar solução!!')
                return

            tree = list_trees[0]


    # def sort_distance(self, list_trees):
    #     """ 1 2 3   [1,1] [1,2] [1,3]
    #         4 5 6   [2,1] [2,2] [2,3]
    #         7 8 0   [3,1] [3,2] [3,3]"""
    #
    #     # Calcula a distância Manhattan para cada nó
    #     for tree in list_trees:
    #         # Retorna posição do elemento
    #         pos = self.get_position(tree, 1)
    #         # Distância Manhattan do elemento
    #         manhattan_distance = abs(1 - pos[0]) + abs(1 - pos[1])
    #
    #         pos = self.get_position(tree, 2)
    #         manhattan_distance += abs(1 - pos[0]) + abs(2 - pos[1])
    #
    #         pos = self.get_position(tree, 3)
    #         manhattan_distance += abs(1 - pos[0]) + abs(3 - pos[1])
    #
    #         pos = self.get_position(tree, 4)
    #         manhattan_distance += abs(2 - pos[0]) + abs(1 - pos[1])
    #
    #         pos = self.get_position(tree, 5)
    #         manhattan_distance += abs(2 - pos[0]) + abs(2 - pos[1])
    #
    #         pos = self.get_position(tree, 6)
    #         manhattan_distance += abs(2 - pos[0]) + abs(3 - pos[1])
    #
    #         pos = self.get_position(tree, 7)
    #         manhattan_distance += abs(3 - pos[0]) + abs(1 - pos[1])
    #
    #         pos = self.get_position(tree, 8)
    #         manhattan_distance += abs(3 - pos[0]) + abs(2 - pos[1])
    #
    #         # Salva o custo do caminho do nó atual
    #         # Se
    #         tree.path_cost += manhattan_distance
    #
    #
    #     for i,tree in enumerate(list_trees):
    #         chave = tree
    #         j = i - 1
    #         while j >= 0 and list_trees[j].path_cost > chave.path_cost:
    #             list_trees[j + 1] = list_trees[j]
    #             j -= 1
    #         list_trees[j + 1] = chave


    # def get_position(self, tree, value):
    #     """Retorna posição do elemento no tabuleiro (matriz)"""
    #     game = tree.queens_puzzle.squares
    #
    #     for i in range(len(game)):
    #         for j in range(len(game[i])):
    #             if game[i][j].label == value:
    #                 return [i+1,j+1]
    #
    #     return []


    def __str__(self):
        """Retorna uma representação em string da árvore"""
        # tree_str = str(self.queens_puzzle)
        # tree_str += '\n  |\n'
        tree_str = ''
        for i in range(len(self.childrens)):
            tree_str += str(self.childrens[i].queens_puzzle)
            tree_str += '\n -' + str(i) + '-\n'
            tree_str += '\t' + str(self.childrens[i])

        return tree_str
