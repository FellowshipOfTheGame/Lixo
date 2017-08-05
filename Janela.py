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

from pygame.locals import * #K_F1, K_ESCAPE

from Gui import Gui
from BotaoToggle import BotaoToggle
from BotaoSimples import BotaoSimples
from Ratazana import Ratazana

from funcoes import carregar_imagem, carregar_fonte
class Janela(object):

    janela = None

    TECLA_TELA_CHEIA = K_F1
    TECLA_SAIDA = K_ESCAPE
    M_ESQ = 1
    M_MEI = 2
    M_DIR = 3
    M_CIM = 4
    M_BAI = 5

    def __init__(self, l, a, texto, mundo, fundo):
        self.largura = l
        self.altura = a
        self.fps = 25
        #self.tela = pygame.display.set_mode((l, a), pygame.FULLSCREEN)
        self.tela = pygame.display.set_mode((l, a))
        pygame.display.set_caption(texto)
        self.clock = pygame.time.Clock()
        self.mundo = mundo
        self.fundo = carregar_imagem(fundo).convert()

        self.gui = Gui()
        self.bot_maxi = BotaoToggle(self.maximizar,
                                       "",
                                       "botao_fullscreen.png",
                                       self.maximizar,
                                       "",
                                       "botao_fullscreen2.png")
        self.bot_maxi.posicionar(950, 25)
        self.gui.adi(self.bot_maxi)

        self.bot_fechar = BotaoSimples(self.fechar,
                                       "",
                                       "botao_sair.png")
        self.bot_fechar.posicionar(1000, 25)
        self.gui.adi(self.bot_fechar)

        self.mouse = Ratazana(None, 0, 0)

    def alt_fundo(self, fundo):
        self.fundo = carregar_imagem(fundo).convert()

    def alt_mundo(self, mundo):
        self.mundo = mundo

    def atualizar(self, m_pos, clique):
        self.gui.atualizar(m_pos, clique)
        self.gui.desenhar(self.tela)

    def loop(self):
        self.rodando = True
        #mouse_pressionado = (False, False, False)
        #mpf = False
		
        while self.rodando:
            clique = False
            events = pygame.event.get()
            event_types = [event.type for event in events]
            teclas_pressionadas = pygame.key.get_pressed()
            teclas = [event.key for event in events if event.type == KEYDOWN]
            mousesUP = [event.button for event in events\
                         if event.type == MOUSEBUTTONUP]
            mousesDO = [event.button for event in events\
                         if event.type == MOUSEBUTTONDOWN]
			
            m_pos = pygame.mouse.get_pos()
            if MOUSEBUTTONDOWN in event_types:
                if self.M_ESQ in mousesDO:
                    clique = True
            if self.TECLA_TELA_CHEIA in teclas:
                self.maximizar()
            if (QUIT in event_types) or (self.TECLA_SAIDA in teclas):
                self.fechar()

            mouse_pressionado = pygame.mouse.get_pressed()	
            #if pygame.mouse.get_pressed()[0] == True and mpf == False and clique == True:
            #    print('PRESSED')
            #    mouse_pressionado = pygame.mouse.get_pressed()
            #    mpf = True
            #elif pygame.mouse.get_pressed()[0] == True and mpf == True and clique == True:
            #    print('DISSSSPRESSED')
            #    mouse_pressionado = (False, False, False)
            #    mpf = False
				
            self.mundo.atualizar(m_pos, clique, mouse_pressionado)
            self.mundo.desenhar(self.tela)
            self.atualizar(m_pos, clique)
            self.mouse.atualizar(m_pos, clique, mouse_pressionado)
            self.mouse.desenhar(self.tela)
            pygame.display.flip()
            self.clock.tick(self.fps)
            self.tela.blit(self.fundo, (0, 0))

    def maximizar(self):
        pygame.display.toggle_fullscreen()

    def fechar(self):
        self.rodando = False
