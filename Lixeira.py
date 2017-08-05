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

import barulho

from Lixo import Lixo
from Flor import Flor

class Lixeira():

    imagemLixeiras = pygame.image.load(os.path.join("gfx", "lixeira.png"))

    def __init__(self, mundo, x, y, tipo=Lixo, nome_arq="lixeira"):

        self.mundo = mundo

        self.rect = pygame.Rect((x, y), (160, 200))

        self.tipo = tipo
        self.contador = 0    # ?? Alguem lembra o que eh isso? =P (Lin)
        # Acho colocou para fazer a lixeira voltar ao tamanho normal depois de
        # um tempo (Andrés) | Isso mesmo! Boa, Andrés! Estou usando de novo
        # pra "animação" de "engolir". =) (Lin)
        self.apto = True    # Se a lixeira esta apta a engolir algum lixo
        self.som = nome_arq + ".wav"
        self.nome = "Lixeira"
        self.tamanho = 0

        if tipo == "Metal":
            linha = 0
        elif tipo == "Papel":
            linha = 1
        elif tipo == "Plastico":
            linha = 2
        elif tipo == "Vidro":
            linha = 3
        elif tipo == "Organico":
            linha = 4

        self.imagens = []
        r = pygame.Rect((0, linha * 200), (160, 200))
        for i in range(4):    # com 4 imagens cada uma
            self.imagens.append(self.imagemLixeiras.subsurface(r))
            r.move_ip(160, 0)
            # "anda" com o retangulo de recorte 160 pixels pra direita

    def atualizar(self, m_pos, clique, m_pressi, mouse):
        if self.rect.collidepoint(m_pos):
            if self.tamanho < 3:
                self.tamanho += 1
                if self.tamanho == 2:
                    barulho.tocar_som_sozinho(self.som)
            if mouse.alvo is not None:
                if clique:
                    if mouse.alvo.tipo == self.tipo:
                        self.mundo.adi(Flor(self.mundo,
                                            (mouse.alvo.pos_anterior[0] +
                                             mouse.alvo.image.get_width(),
                                             mouse.alvo.pos_anterior[1] +
                                             mouse.alvo.image.get_height())))
                                       # flor nasce onde estava
                        mouse.alvo.sumir()
                        
                        barulho.tocar_som_sozinho("certo")
                        barulho.CERTO_ERRADO = True
                        self.contador = 10
                        self.apto = False
                    else:
                        mouse.alvo.retornar()
                        barulho.tocar_som_sozinho("errado")
                        barulho.CERTO_ERRADO = True

        elif self.tamanho > 0:
            self.tamanho -= 1

    def desenhar(self, s):
        if self.contador > 0:
            temp = self.imagens[3]
            xtemp = self.contador * 5 + self.rect.x
            ytemp = self.contador * 5 + self.rect.y
            rectTemp = pygame.Rect(self.rect.x - self.contador * 5,
                                   self.rect.y - self.contador * 10,
                                   self.rect.w + 10 * self.contador,
                                   self.rect.h + 10 * self.contador)
            temp = pygame.transform.scale(temp, (rectTemp.w, rectTemp.h))
            s.blit(temp, rectTemp)
            self.contador -= 1
            if self.contador == 0:
                self.tamanho = 3
                self.apto = True
        else:
            temp = self.imagens[self.tamanho]
            s.blit(temp, self.rect)

#    def desenhar(self, s):
#        temp = self.imagens[self.tamanho]
#        temp = pygame.transform.scale(temp, (200, 200))
#        s.blit(temp, self.rect)
