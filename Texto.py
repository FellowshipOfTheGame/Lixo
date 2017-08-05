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

class Texto(Elemento):
    '''Um texto puro'''

    def __init__(self, texto="TEXTO", tamanho=25, cor=(100, 200, 100),
                 img_botao="vazio.png"):

        self.x = 0
        self.y = 0
        self.texto = texto
        self.nome = "dalles_-_SMonohand.ttf"
        self.tam = tamanho
        self.cor = cor
#        self.negrito = True
#        self.italico = False

        self.fonte = carregar_fonte(self.nome, self.tam)
#        self.fonte = pygame.font.SysFont(self.nome,
#                                         self.tam,
#                                         self.negrito,
#                                         self.italico)

        self.imag_botao = carregar_imagem(img_botao).convert_alpha()
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

    def alt_texto(self, texto):
        self.texto = texto
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

    def ret_alt(self):
        alt = max(self.imag_texto.get_height(),
                  self.imag_botao.get_height())
        return alt

    def ret_lar(self):
        lar = max(self.imag_texto.get_width(),
                  self.imag_botao.get_width())
        return lar

    def atualizar(self, mouse, clique):
        pass

    def alt_cor(self, r, g, b):
        self.cor = (r, g, b)
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

    def posicionar(self, x, y):
        l = self.imag_botao.get_width()
        a = self.imag_botao.get_height()
        self.x, self.y = x - l / 2, y - a / 2

    def desenhar(self, s):
        s.blit(self.imag_botao, (self.x, self.y))
        l = self.imag_botao.get_width()
        a = self.imag_botao.get_height()
        pos = (self.x + (l - self.imag_texto.get_width()) / 2,
               self.y + (a - self.imag_texto.get_height()) / 2)
        s.blit(self.imag_texto, pos)

