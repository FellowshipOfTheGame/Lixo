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

from funcoes import carregar_imagem
import barulho

class Guarana(Sprite):

    def __init__(self, mundo, x, y, nome_arq="lixo.png"):
        Sprite.__init__(self)

        self.image = carregar_imagem(nome_arq)
        self.rect = self.image.get_bounding_rect()
        self.rect.x, self.rect.y = x, y
        self.selec = False

        self.mundo = mundo
        if self.mundo is not None:
            self.mundo.adi(self)

    def trocar_imagem(self, nome_arq):
        self.imagem = carregar_imagem(nome_arq)

    def desenhar(self, s):
        s.blit(self.image, self.rect)

    def atualizar(self, m_pos, clique):
        pass

    def crescer(self):
        self.apto = False
        self.image = pygame.transform.scale(self.image,
                                            (int(self.rect.width * 2),
                                             int(self.rect.height)))
        self.rect.x -= 50
        self.contador = 5

    def reduzir(self):
        self.image = pygame.transform.scale(self.image,
                                            (self.rect.width,
                                             self.rect.height))
        self.rect.x += 50
        self.apto = True

    def sobre(self):
        self.mundo.alt_texto(self.nome)
        self.mundo.alt_simb(self.simbolo)
        barulho.tocar_som_sozinho(self.som)
