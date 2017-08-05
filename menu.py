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

class Menu(Elemento):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.tam_x = 0
        self.tam_y = 0
        self.espacamento = 20
        self.botoes = []
        self.fundo = None
        self.moldura = None
        self.imag_borda = carregar_imagem("borda.png").convert_alpha()
        self.imag_canto = carregar_imagem("canto.png").convert_alpha()

        self.posicionar()

    def adi_bot(self, botao):
        self.botoes.append(botao)

    def ajustar_tam(self):

        # Ajusta altura
        acu = 0
        for b in self.botoes:
            acu += b.ret_alt() + self.espacamento
        acu += self.espacamento
        a = self.imag_borda.get_height()
        acu = (acu / a) * a
        acu += self.imag_canto.get_height() * 2
        self.tam_y = acu

        # Ajusta largura
        acu = 0
        for b in self.botoes:
            if b.ret_lar() > acu:
                acu = b.ret_lar()
        acu += self.espacamento * 2
        a = self.imag_borda.get_width()
        acu = (acu / a) * a
        acu += 2 * self.imag_canto.get_height()
        self.tam_x = acu

        self.fundo = pygame.Surface((self.tam_x, self.tam_y)).convert_alpha()
        self.moldura = pygame.Surface((self.tam_x, self.tam_y))

        self.posicionar()

    def atualizar(self, mouse, clique):
        mouse2 = (mouse[0] - self.x, mouse[1] - self.y)
        for b in self.botoes:
            b.atualizar(mouse2, clique)

    def posicionar(self):

        self.moldura = pygame.Surface((self.tam_x, self.tam_y)).convert_alpha()
        self.moldura.fill((0, 0, 0, 0))

        cant_l = self.imag_canto.get_width()
        cant_a = self.imag_canto.get_height()

        # NO
        pos = (0, 0)
        self.moldura.blit(self.imag_canto, pos)
        # SO
        cant2 = pygame.transform.rotate(self.imag_canto, 90)
        pos = (0, self.tam_y - cant_a)
        self.moldura.blit(cant2, pos)
        # SE
        cant2 = pygame.transform.rotate(cant2, 90)
        pos = (self.tam_x - cant_l, self.tam_y - cant_a)
        self.moldura.blit(cant2, pos)
        # NE
        cant2 = pygame.transform.rotate(cant2, 90)
        pos = (self.tam_x - cant_l, 0)
        self.moldura.blit(cant2, pos)

        bord_l = self.imag_borda.get_width()
        bord_a = self.imag_borda.get_height()

        # Horizontais
        for i in range(0, (self.tam_x - 2 * cant_l) / bord_l):
            pos = (cant_l + i * bord_l, (cant_a - bord_a) / 2)
            self.moldura.blit(self.imag_borda, pos)
            pos = (cant_l + i * bord_l, self.tam_y - cant_a +
                   (cant_a - bord_a) / 2)
            self.moldura.blit(self.imag_borda, pos)

        bord2 = pygame.transform.rotate(self.imag_borda, 90)
        # Verticais
        for i in range(0, (self.tam_y - 2 * cant_a) / bord_a):
            pos = ((cant_l - bord_l) / 2, cant_a + i * bord_a)
            self.moldura.blit(bord2, pos)
            pos = (self.tam_x - cant_l +
                   (cant_l - bord_l) / 2, cant_a + i * bord_a)
            self.moldura.blit(bord2, pos)

        acu = self.imag_canto.get_height() + self.espacamento * 2
        for b in self.botoes:
            pos = (self.tam_x / 2, acu)
            b.posicionar(pos[0], pos[1])
            acu += b.ret_alt() + self.espacamento

    def desenhar(self, s):
        self.fundo.fill((0, 0, 0, 0))
        self.fundo.blit(self.moldura, (0, 0))
        for b in self.botoes:
            b.desenhar(self.fundo)
        s.blit(self.fundo, (self.x, self.y))
