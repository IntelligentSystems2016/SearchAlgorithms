#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import os
import os.path
from tree import *
from graphviz import Digraph

class DrawTree(object):

    global dot

    def __init__(self, tree, name='Arvore_8-Game'):
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

        # Renderiza a imagem da árvore
        dot.render(name)
        # dot.view(name)

        # Remove os arquivos desnecessarios apos renderizacao
        os.remove(name)

        # Chamada de sistema para abrir imagem
        os.system('shotwell ' + name + '.png')


    def draw(self, tree):
        """Percorre árvore e desenha"""

        # Cópia da árvore
        tree = copy.deepcopy(tree)

        global dot

        # Testa se jogo existe
        if not tree.eight_game is None:
            # Cria nó com id e jogo
            dot.node(str(tree.id), str(tree.eight_game))
            # Testa se existe lista com os filhos do nó atual
            if tree.childrens:
                # Percorre lista de filhos
                for child in tree.childrens:
                    # Recursão para desenhar sub-árvore de filhos
                    self.draw(child)
                    # Aresta entre árvore e sub-árvore
                    dot.edge(str(tree.id), str(child.id))
