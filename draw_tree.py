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
        # dot.render(name)
        dot.view()

        # Chamada de sistema para abrir imagem
        # os.system('shotwell ' + name + '.png')

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
        if not tree.eight_game is None:
            # Cria nó com id e jogo
            if tree.is_visited:
                if tree.is_objective:
                    dot.node(str(tree.id), str(tree.eight_game), fillcolor = 'cornflowerblue')
                else:
                    dot.node(str(tree.id), str(tree.eight_game), fillcolor = '#FFFFFF')

                # Testa se existe lista com os filhos do nó atual
                if tree.childrens:
                    # Percorre lista de filhos
                    for child in tree.childrens:
                        if child.is_visited:
                            # Recursão para desenhar sub-árvore de filhos
                            self.draw(child)
                            # Aresta entre árvore e sub-árvore
                            dot.edge(str(tree.id), str(child.id))
