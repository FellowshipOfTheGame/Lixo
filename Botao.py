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

class Botao(Elemento):

    def __init__(self, funcao, texto="TEXTO", img_botao="botao.png",
                 img_sobre="tinta.png"):
        self.funcao = funcao
        self.x = 0
        self.y = 0
        self.texto = texto
        self.nome = "dalles_-_SMonohand.ttf"
        self.tam = 20
        self.cor = (100, 0, 0)
        self.negrito = False
        self.italico = False

        self.fonte = carregar_fonte(self.nome, self.tam)

#        self.fonte = pygame.font.SysFont(self.nome,
#                                         self.tam,
#                                         self.negrito,
#                                         self.italico)

        self.img_botao = carregar_imagem(img_botao).convert_alpha()
        self.img_sobre = carregar_imagem(img_sobre).convert_alpha()
        self.fundo = pygame.Surface((0, 0)).convert_alpha()
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

        self.sobre = False

    def ret_alt(self):
        alt = max(self.fundo.get_height(),
                  self.imag_texto.get_height(),
                  self.img_botao.get_height(),
                  self.img_sobre.get_height())
        return alt

    def ret_lar(self):
        lar = max(self.fundo.get_width(),
                  self.imag_texto.get_width(),
                  self.img_botao.get_width(),
                  self.img_sobre.get_width())
        return lar

    def atualizar(self, mouse, clique):
        if self.rect.collidepoint(mouse):
            self.sobre = True
        else:
            self.sobre = False

        if self.sobre and clique:
            self.funcao()

    def posicionar(self, x, y):
        self.imagem = self.fonte.render(self.texto, True, self.cor)

        l = self.img_botao.get_width()
        a = self.img_botao.get_height()
        self.x, self.y = x - l / 2, y - a / 2
        self.rect = pygame.Rect((self.x, self.y), (l, a))

        self.fundo = pygame.Surface((l, a)).convert_alpha()
        self.fundo.fill((0, 0, 0, 0))
        self.fundo.blit(self.img_botao, (0, 0))

    def desenhar(self, s):
        s.blit(self.fundo, (self.x, self.y))
        if self.sobre:
            s.blit(self.img_sobre, (self.x, self.y))

        l = self.img_botao.get_width()
        a = self.img_botao.get_height()
        pos = (self.x + (l - self.imag_texto.get_width()) / 2,
               self.y + (a - self.imag_texto.get_height()) / 2)
        s.blit(self.imag_texto, pos)

