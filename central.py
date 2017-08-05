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
import pygame
import sys

import barulho

from Janela import Janela
from Jogo import Jogo
from MenuPrincipal import MenuPrincipal
"""Classe inicial. O programa deve ser chamado atravez de "python central.py"."""
class Central():
    """Inicializa tudo e alterna entre menu e jogo"""

    def __init__(self):
        """Carrega sons, fases e abre menu inicial"""
        barulho.inicio()
        barulho.carr_musica("Llamarama-musica_feliz2.mp3", "feliz")
        barulho.carr_musica("vitoria.mp3", "vitoria")
        barulho.carr_som("certo.wav", "certo")
        barulho.carr_som("errado.wav", "errado")
        barulho.carr_som("papel.wav", tipo="ajuda")
        barulho.carr_som("organico.wav", tipo="ajuda")
        barulho.carr_som("plastico.wav", tipo="ajuda")
        barulho.carr_som("vidro.wav", tipo="ajuda")
        barulho.carr_som("metal.wav", tipo="ajuda")
        barulho.carr_som("lixeira.wav", tipo="ajuda")
        barulho.carr_som("lixeira_papel.wav", tipo="ajuda")
        barulho.carr_som("lixeira_organico.wav", tipo="ajuda")
        barulho.carr_som("lixeira_metal.wav", tipo="ajuda")
        barulho.carr_som("lixeira_vidro.wav", tipo="ajuda")
        barulho.carr_som("lixeira_plastico.wav", tipo="ajuda")
        #barulho.carr_som("vitoria.wav", "vitoria")

        barulho.tocar_musica("feliz")

        self.janela = Janela(1024, 768, "LIXO!", None, "fundo.png")

		#Seta o jogo para rodar em fullscreen
        pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)

        self.jogo = Jogo(self)
        self.jogo.carregar_fases()

        self.menu = MenuPrincipal(self)
        self.menu.comecar(self.janela)

    def comecar_jogo(self):
        """Passa a janela para o jogo comecar"""
        self.jogo.comecar(self.janela)

    def fim_jogo(self):
        """Passa a janela do jogo para o menu"""
        self.menu.comecar(self.janela)

    def rodar(self):
        """Loop principal do jogo, quando termina, desliga os sons"""
        self.janela.loop()
        barulho.fim()

    def ajuda(self):
        """Mostra ajuda"""
        sys.exit()

if __name__ == "__main__":
    #import profile
    CENTRAL = Central()
    r = CENTRAL.rodar
    r()
    #profile.run("r()")

