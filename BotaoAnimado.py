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
import pygame
class BotaoAnimado(Elemento):
    def __init__(self, funcao, texto="TEXTO", img_botao="botao.png", linha=0):
        self.funcao = funcao

        self.vetor = []
        r = pygame.Rect(0, linha * 200, 200, 200)
        imagem_toda = carregar_imagem("botoes.png").convert_alpha()
        for i in range(6):
            self.vetor.append(imagem_toda.subsurface(r))
            r.move_ip(200, 0)
        self.mostrar = 0
        self.linha = linha
#        self.pos = (0, linha * 200)
        self.estado = 0  # 0 = sem mouse, 1 = subindo, 2 = descendo animacao
        self.tempo = 0
        self.tempo_base = 10
        self.ligado = False

        self.posTexto = (0, 0)
        self.texto = texto
        self.nome = "dalles_-_SMonohand.ttf"
        self.tam = 20
        self.cor = (100, 0, 0)
        self.negrito = False
        self.italico = False
        self.fonte = carregar_fonte(self.nome, self.tam)
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

    def posicionar(self, x, y):
        l = self.vetor[0].get_width()
        a = self.vetor[0].get_height()
        self.x, self.y = x - l / 2, y - a / 2
        self.rect = pygame.Rect((self.x, self.y), (l, a))
        self.posTexto = (x - (self.imag_texto.get_width()) / 2,
                         y + a / 2 + 10)

    def alt_cor(self, r, g, b):
        self.cor = (r, g, b)
        self.imag_texto = self.fonte.render(self.texto, True, self.cor)

    def atualizar(self, mouse, clique):
        self.ligado = self.rect.collidepoint(mouse)
        if self.ligado:
            if self.estado == 0:
                self.estado = 1
                self.mostrar = 1
                self.tempo = self.tempo_base  # podemos mudar pra "0", tb...
            else:
                if (self.tempo > 0):
                    self.tempo -= 1  # espere...
                else:  # mude!
                    self.tempo = self.tempo_base
                    if self.estado == 1:  # aumentando numero
                        if self.mostrar < 5:  # ainda pode aumenta?
                            self.mostrar += 1
                        else:
                            self.mostrar = 1
            if clique:
                self.funcao()
        else:
            self.estado = 0
            self.mostrar = 0

    def desenhar(self, s):
        s.blit(self.vetor[self.mostrar], (self.x, self.y))
        s.blit(self.imag_texto, self.posTexto)
