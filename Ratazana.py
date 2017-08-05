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

from Guarana import Guarana
from funcoes import carregar_imagem
class Ratazana(Guarana):
    # Mouse =P
	
    def __init__(self, mundo, x, y, nome_arq="mao_aberta.png"):
        Guarana.__init__(self, mundo, x, y, nome_arq)
      #  self.mundo.rem(self)
	  
        #self.mpf = False
        self.mao_fechada = carregar_imagem("mao_fechada.png")
        self.mao_fechada_rect = self.mao_fechada.get_bounding_rect()
        self.mao_fechada_rect.x, self.mao_fechada_rect.y = x, y

        self.alvo = None  # Caso esteja segurando algo, aponta para esse algo
        self.comportamento = False  # Alterna comportamento drag and drop
        self.sobre = None  # Algo q o mouse esteja sobrevoando

    def atualizar(self, m_pos, clique, m_pressi):
        self.rect.x, self.rect.y = m_pos
        self.mao_fechada_rect.x, self.mao_fechada_rect.y = m_pos

        # Verfica se colidiu com algo que não é o alvo
        if self.mundo is not None:
            colidiu = self.colidir([self.alvo])
        else:
            colidiu = None

        if colidiu != None and colidiu != self.sobre:
            self.sobre = colidiu
            colidiu.sobre()
        elif colidiu == None and self.alvo == None:
            self.sobre = None

        if self.comportamento:
            if clique:
                if self.alvo == None:
                    self.selecionar(colidiu)
                else:
                    self.alvo.deselecionar()
                    self.alvo = None
        else:
            if clique and self.alvo == None:
                self.selecionar(colidiu)
            elif clique and self.alvo != None:
                self.alvo.deselecionar()
                self.alvo = None
				#if type(item) is type(Class):

    def colidir(self, incolidiveis=[]):
        for c in self.mundo.coisas.__reversed__():
            if pygame.sprite.collide_mask(self, c):
                if c not in incolidiveis:
                    return c

    def selecionar(self, colidiu):
        if hasattr(colidiu, "selecionar"):
            self.alvo = colidiu
            if self.alvo != None:
                self.alvo.selecionar((self.rect.w / 2, self.rect.h / 2))

    def desenhar(self, s):
        if self.alvo == None:
            s.blit(self.image, self.rect)
        else:
            self.alvo.desenhar(s)
            s.blit(self.mao_fechada, self.mao_fechada_rect)
