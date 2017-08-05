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
from Elemento import Elemento
from funcoes import carregar_imagem, carregar_fonte
class Desenho(Elemento):
    '''Um desenho'''

    def __init__(self, img_botao):
        self.x = 0
        self.y = 0
        self.imag_botao = carregar_imagem(img_botao).convert_alpha()

    def alt_imag(self, arquivo):
        self.imag_botao = carregar_imagem(arquivo).convert_alpha()

    def ret_alt(self):
        alt = self.imag_botao.get_height()
        return alt

    def ret_lar(self):
        lar = self.imag_botao.get_width()
        return lar

    def atualizar(self, mouse, clique):
        pass

    def posicionar(self, x, y):
        l = self.imag_botao.get_width()
        a = self.imag_botao.get_height()
        self.x, self.y = x - l / 2, y - a / 2

    def desenhar(self, s):
        s.blit(self.imag_botao, (self.x, self.y))

