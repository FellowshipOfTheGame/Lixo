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
from Selecionavel import Selecionavel
from Estrela import Estrela
import animacoes
import random
class Lixo(Selecionavel):
    def __init__(self, mundo, tipo):
        """Carrega as características do lixo e gera uma imagem randomica de acordo com seu tipo"""
        if tipo == 0: #papel
            nome_arq = "pa-" + str(random.randint(1,9)) + ".png"
            self.som = "papel.wav"
            self.simbolo = "simbPA.png"
            self.tipo = "Papel"
            self.nome = "Papel"
            
        elif tipo == 1: #plastico
            nome_arq = "pl-" + str(random.randint(1,7)) + ".png"
            self.som = "plastico.wav"
            self.simbolo = "simbPL.png"
            self.tipo = "Plastico"
            self.nome = "Plastico"
        elif tipo == 2: #metal
            nome_arq = "me-" + str(random.randint(1,7)) + ".png"
            self.som = "metal.wav"
            self.simbolo = "simbME.png"
            self.tipo = "Metal"
            self.nome = "Metal"
        elif tipo == 3: #vidro
            nome_arq = "vi-" + str(random.randint(1,8)) + ".png"
            self.som = "vidro.wav"
            self.simbolo = "simbVI.png"
            self.tipo = "Vidro"
            self.nome = "Vidro"
        elif tipo == 4: #organico
            nome_arq = "or-" + str(random.randint(1,5)) + ".png"
            self.som = "organico.wav"
            self.simbolo = "simbOR.png"
            self.tipo = "Organico"
            self.nome = "Organico"
        x = random.randint(10,1000)
        y = random.randint(80,550)
        Selecionavel.__init__(self, mundo, x, y, nome_arq)
        self.retornando = False
#        self.apto = True
        self.tem_estrela = False
        self.animar = animacoes.animar_lixo

    def atualizar(self, m_pos, clique):
        Selecionavel.atualizar(self, m_pos, clique)
        if self.retornando:
            self.animar(self)

    def retornar(self):
        """caso seja jogado na lata errada, estará marcado como
        "errado" e a animacao o fara voltar"""
        self.retornando = True

    def adicionar_estrela(self):
        self.mundo.adi(Estrela(self.mundo,
                               (self.rect.x + self.image.get_width() / 2,
                                self.rect.y-200), False))  # estrela triste
        self.tem_estrela = True

    def reposiciona(self, x, y):
        self.rect.x = x
        self.rect.y = y
