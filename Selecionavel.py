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
#
# ATENÇÃO!!!
#
# Esta classe foi desenvolvida em parceria com a PEI: Piada Extremamente Infame
from Guarana import Guarana
class Selecionavel(Guarana):

    def __init__(self, mundo, x, y, nome_arq="lixo.png"):
        Guarana.__init__(self, mundo, x, y, nome_arq)
        self.selecionado = False
        self.pos_anterior = (self.rect.x, self.rect.y)
        self.offset = (0, 0)

    def sumir(self):
        self.mundo.rem(self)

    def selecionar(self, pos):
        self.selecionado = True
        self.pos_anterior = (self.rect.x, self.rect.y)  # posicao anterior
        self.offset = pos[0] - self.rect.w / 2, pos[1] - self.rect.height / 2

    def deselecionar(self):
        self.selecionado = False

    def atualizar(self, m_pos, clique):
        if self.selecionado == True:
            self.rect.x, self.rect.y = m_pos
            self.rect.move_ip(self.offset)
