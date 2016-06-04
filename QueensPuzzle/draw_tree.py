#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import os
import os.path
from tree import *
from graphviz import Digraph

class DrawTree(object):

    global dot

    def __init__(self, tree, name='Arvore_QueensPuzzle'):
        """Contrutor da classe DrawTree"""
        super(DrawTree, self).__init__()
        # Cópia da árvore
        self.tree = copy.deepcopy(tree)

        global dot
        # Cria grafo direcionado
        dot = Digraph(name = name)
        dot.format = 'png'

        # Desenha árvore
        self.draw(self.tree)

        # Visualiza a imagem da árvore
        dot.view()

        # Remove os arquivos desnecessarios apos renderizacao
        os.remove(name + '.gv')
        # os.remove(name + '.gv.png')


    def draw(self, tree):
        """Percorre árvore e desenha"""

        # Cópia da árvore
        tree = copy.deepcopy(tree)

        global dot
        dot.node_attr['style'] = 'filled'

        # Testa se jogo existe
        if not tree.queens_puzzle is None:
            # Cria nó com id e jogo
            if tree.is_visited:
                if tree.is_objective:
                    dot.node(str(tree.id), str(tree.queens_puzzle), fillcolor = 'cornflowerblue')
                else:
                    dot.node(str(tree.id), str(tree.queens_puzzle), fillcolor = '#FFFFFF')

                # Testa se existe lista com os filhos do nó atual
                if tree.childrens:
                    # Percorre lista de filhos
                    for child in tree.childrens:
                        if child.is_visited:
                            # Recursão para desenhar sub-árvore de filhos
                            self.draw(child)
                            # Aresta entre árvore e sub-árvore
                            dot.edge(str(tree.id), str(child.id))
