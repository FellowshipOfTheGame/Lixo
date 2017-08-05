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
import sys
import pygame

from BotaoAnimado import BotaoAnimado
from Gui import Gui

class MenuPrincipal():
    """Menu principal de jogo"""

    def __init__(self, central):
        """Cria o menu com seus textos e botoes"""
        self.gui = Gui()
        self.fundo = "fundo.png"

        #self.mouse = RatazanaSimples(self, 0, 0)

        #titulo = Texto("L I X O !", tamanho=30, img_botao="botao.png")
        #titulo.alt_cor(128, 128, 0)
        #titulo.posicionar(512, 128)
        #self.adi(titulo)
        bot_iniciar = BotaoAnimado(central.comecar_jogo, texto="Iniciar!",
                         img_botao="iniciar.png", linha=0)
        bot_iniciar.posicionar(400, 384)
        bot_iniciar.alt_cor(0, 255, 0)
        self.adi(bot_iniciar)
        #bot_aju = BotaoAnimado(central.ajuda, texto="Ajuda",
         #                img_botao="ajuda.png", linha=1)
#        bot_aju.posicionar(512, 384)
#        bot_aju.alt_cor(0, 0, 255)
 #       self.adi(bot_aju)
        bot_sair = BotaoAnimado(sys.exit, texto="Sair",
                                img_botao="sair.png", linha=2)
        bot_sair.posicionar(650, 384)
        bot_sair.alt_cor(255, 0, 0)
        self.adi(bot_sair)

        pygame.mouse.set_visible(False)

    def comecar(self, janela):
        """Faz a janela mostrar esse menu"""
        janela.alt_mundo(self)
        janela.alt_fundo(self.fundo)

    def adi(self, coisa):
        """Adiciona alguma coisa na Gui"""
        self.gui.adi(coisa)

    def rem(self, coisa):
        """Remove algo da Gui"""
        self.gui.rem(coisa)

    def atualizar(self, m_pos, clique, m_pressi):
        """Atualiza menu verificando posicao e clique do mouse"""
        self.gui.atualizar(m_pos, clique)
        #self.mouse.atualizar(m_pos, clique, m_pressi)

    def desenhar(self, superf):
        """Desenha menu e mouse"""
        self.gui.desenhar(superf)
        #self.mouse.desenhar(superf)

