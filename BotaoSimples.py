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

import os
import pygame
from pygame.locals import * #K_F1, K_ESCAPE
from pygame.sprite import Sprite
from pygame.sprite import Group

from Elemento import Elemento
from funcoes import carregar_imagem, carregar_fonte

class BotaoSimples(Elemento):

    def __init__(self, funcao, texto="TEXTO", img_botao="botao.png"):
        self.funcao = funcao
        self.x = 0
        self.y = 0
        self.posTexto = (0, 0)
        self.texto = texto
        self.nome = "dalles_-_SMonohand.ttf"
        self.tam = 20
        self.cor = (100, 0, 0)
        self.negrito = False
        self.italico = False

        self.fonte = carregar_fonte(self.nome, self.tam)

        self.img_botao = carregar_imagem(img_botao).convert_alpha()
#        self.img_sobre = carregar_imagem(img_sobre).convert_alpha()
#        self.fundo = pygame.Surface((0, 0)).convert_alpha()
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

        self.posicionar(self.x, self.y)

        self.sobre = False

    def alt_cor(self, r, g, b):
        self.cor = (r, g, b)
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

    def posicionar(self, x, y):
        l = self.img_botao.get_width()
        a = self.img_botao.get_height()
        self.x, self.y = x - l / 2, y - a / 2
        self.rect = pygame.Rect((self.x, self.y), (l, a))
        self.posTexto = (x - (self.imag_texto.get_width()) / 2,
                         y + a / 2 + 10)

    def ret_alt(self):
        alt = self.img_botao.get_height()
        return alt

    def ret_lar(self):
        lar = self.img_botao.get_width()
        return lar

    def atualizar(self, mouse, clique):
        self.sobre = self.rect.collidepoint(mouse)

        if self.sobre and clique:
            self.funcao()

    def desenhar(self, s):
        s.blit(self.img_botao, (self.x, self.y))
        s.blit(self.imag_texto, self.posTexto)

