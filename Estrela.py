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
from pygame.sprite import Sprite
from pygame.sprite import Group
import animacoes

from funcoes import carregar_imagem, carregar_fonte
class Estrela(Sprite):
    """ Estrela exibida quando o lixo é colocado no local certo/errado """
    def __init__(self, mundo, pos, certo):
        Sprite.__init__(self)
        self.mundo = mundo
        if certo:
            self.image = carregar_imagem("estrela6.png")
        else:
            self.image = carregar_imagem("estrela0.png")
        self.certo = certo
        self.rect = self.image.get_bounding_rect()
        self.rect.x, self.rect.y = pos
        self.rect.x -= self.image.get_width() / 2
        self.rect.y -= self.image.get_height() / 2
        if not certo:
            self.rect.y -= 150
        self.estado = 0  # 0 = subindo; 1 = parado
        self.ticks = self.mundo.fase.jogo.central.janela.fps
        # é *só* fazer isso ;) (Andrés)
        #30 # igual ao FPS, nao sabia como pega-lo (Lin)
        self.animar = animacoes.animar_estrela
        self.mundo.adi(self)

    def desenhar(self, s):
        s.blit(self.image, self.rect)

    def atualizar(self, m_pos, clique):
#        print self.ticks
        self.animar(self)

    def sobre(self):
        pass
