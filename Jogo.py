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
import xml.dom.minidom as dom


from Fase import Fase

class Jogo():
    """Organiza e inicia fases"""

    def __init__(self, central):
        """Jogo com lista de fases para gerencia-las melhor"""
        self.fases = []
        self.central = central

    def carregar_fases(self):
        """Carrega as fases para depois serem jogadas"""

        arquivos = os.listdir("fases")

        arquivos_fases = []
        for arq in arquivos:
            if arq[-4:] == ".xml":
                arquivos_fases.append(arq)
        arquivos_fases.sort()
        arquivos_fases.reverse()

        for arq in arquivos_fases:
            try:
                xml_fase = dom.parse(os.path.join("fases", arq))
            except:
                #print("XML invalido!")
                pass
            Fase(self, xml_fase)

    def adi_fase(self, fase):
        """Adiciona um fase na lista de fases"""
        self.fases.append(fase)

    def fim(self):
        """Termina e inicia a proxima fase"""
        self.central.comecar_jogo()

    def comecar(self, janela):
        """Comeca uma fase"""
        #print(self.fases)
        if self.fases == []:
            self.carregar_fases()
        fase = self.fases.pop()
        fase.comecar()
        mundo, fundo = fase.ret_dados()
        janela.alt_mundo(mundo)
        janela.alt_fundo(fundo)
