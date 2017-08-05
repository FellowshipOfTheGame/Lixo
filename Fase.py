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
from Mundo import Mundo
from Lixo import Lixo

class Fase():
    """Base para uma fase"""

    def __init__(self, jogo, xml_fase):
        self.jogo = jogo
        self.jogo.adi_fase(self)
        self.xml_fase = xml_fase
        descr_fase = self.xml_fase.getElementsByTagName("fase")[0]
        self.nome = descr_fase.getAttribute("nome")
        self.fundo = descr_fase.getAttribute("fundo")
        self.mundo = None

    def comecar(self):
        self.mundo = Mundo(self)

        for lixo in self.xml_fase.getElementsByTagName("lixo"):
            tipo = int(lixo.getAttribute("tipo"))
            quantidade = int(lixo.getAttribute("quantidade"))

            for i in range(quantidade):
                Lixo(self.mundo, tipo)

    def fim(self):
        """Termina essa fase"""
        self.jogo.fim()

    def ret_dados(self):
        """Retorna o mundo e o fundo"""
        return self.mundo, self.fundo

