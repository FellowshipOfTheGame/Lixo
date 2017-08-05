#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Copyright 2009 The Fellowship of the Game
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#-----------------------------------------------------------------------------


import pygame
class Gui(object):
    '''Classe para trabalhar com conjunto de menus'''

    def __init__(self):
        self.coisas = []
        pygame.font.init()

    def adi(self, algo):
        self.coisas.append(algo)

    def adiT(self, algo):
        self.coisas.insert(0, algo)

    def rem(self, algo):
        self.coisas.remove(algo)

    def atualizar(self, mouse, clique):
        for c in self.coisas:
            c.atualizar(mouse, clique)

    def desenhar(self, s):
        for c in self.coisas:
            c.desenhar(s)
