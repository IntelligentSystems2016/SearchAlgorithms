#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Square(object):
    """docstring for Square"""
    def __init__(self, label):#, top, bottom, left, right):
        super(Square, self).__init__()
        # Rótulo do nó atual
        self.label = label

        # Nós adjacentes
        self.adjacents = {}
        """
        # EXEMPLO DO USO
        self.adjacents['top'] = top
        self.adjacents['bottom'] = bottom
        self.adjacents['left'] = left
        self.adjacents['right'] = right
        """


    def __str__(self):
        """Retorna uma representação em string do quadrado"""
        square_str = '[T'
        square_str += str(self.adjacents['top'].label)
        square_str += ', B'
        square_str += str(self.adjacents['bottom'].label)
        square_str += ', L'
        square_str += str(self.adjacents['left'].label)
        square_str += ', R'
        square_str += str(self.adjacents['right'].label)
        square_str += ']'

        return square_str
