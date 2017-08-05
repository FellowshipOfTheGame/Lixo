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

from pygame.sprite import Group

from Gui import Gui
from Texto import Texto
from Desenho import Desenho
from BotaoToggle import BotaoToggle
from BotaoSimples import BotaoSimples
from Lixeira import Lixeira
from Lixo import Lixo
from Flor import Flor

import animacoes
import barulho

class Mundo(Group):

    win = False

    def __init__(self, fase):
        Group.__init__(self)
        self.fase = fase

        self.coisas = []
        self.win = False
		
        # listas de cada coisa
        self.lixos = []
        self.lixeiras = []
        self.flores = []

        self.mouse = fase.jogo.central.janela.mouse 
        self.mouse.mundo = self
        self.gui = Gui()

        self.texto = Texto(texto="TEXTO", tamanho=25, cor=(200, 100, 100),
                           img_botao="botao.png")
        self.texto.alt_pos(400, 20)
#        self.gui.adi(self.texto)

        desenho = Desenho("barra_de_lixo.png")
        desenho.alt_pos(0, 0)
        self.gui.adi(desenho)

        desenho = Desenho("fundo_simb.png")
        desenho.alt_pos(500, 0)
        self.gui.adi(desenho)

        self.simbolo = Desenho("fundo_simb.png")
        self.simbolo.alt_pos(500, 0)
        self.gui.adi(self.simbolo)

        #self.alt_controle_som(True)

        self.controleSom = BotaoToggle(self.alt_controle_som,
                                       "",
                                       "comSom.png",
                                       self.alt_controle_som, "",
                                       "semSom.png")
        self.controleSom.posicionar(85, 25)
        self.gui.adi(self.controleSom)

        self.controleSom = BotaoToggle(barulho.desligar,
                                       "",
                                       "comMusica.png",
                                       barulho.ligar, "",
                                       "semMusica.png")
        self.controleSom.posicionar(115, 25)
        self.gui.adi(self.controleSom)

        self.bot_voltar = BotaoSimples(self.fase.fim,
                                       "",
                                       "botao_menu.png")
        self.bot_voltar.posicionar(35, 25)
        self.gui.adi(self.bot_voltar)

        self.vitoria = animacoes.animar_vitoria
        self.estado_vitoria = 200  # contador para a animacao de vitoria
        self.contador_final = 200
        self.venceu = False

        self.lixeiras.append(Lixeira(self, 50, 568, "Metal", "lixeira_metal"))
        self.lixeiras.append(Lixeira(self, 240, 568, "Papel", "lixeira_papel"))
        self.lixeiras.append(Lixeira(self, 430, 568, "Plastico",
                                     "lixeira_plastico"))
        self.lixeiras.append(Lixeira(self, 620, 568, "Vidro", "lixeira_vidro"))
        self.lixeiras.append(Lixeira(self, 810, 568, "Organico",
                                     "lixeira_organico"))

    def alt_controle_som(self):
        barulho.alt_tipo("ajuda")

    def alt_texto(self, texto):
        self.texto.alt_texto(texto)

    def alt_simb(self, imag):
        self.simbolo.alt_imag(imag)

    def adi(self, coisa):
        if isinstance(coisa, Lixo):
            self.lixos.append(coisa)
#            ok = False
#            while not ok:
#                ok = True
#                for c in self.lixeiras:
#                    if pygame.sprite.collide_mask(c, coisa) != None:
#                        ok = False
#                if not ok:
#                    coisa.reposiciona(random.randint(0, 900),
#            random.randint(200, 550)) # mais ou menos para ficar no gramado
        elif isinstance(coisa, Flor):
            self.flores.append(coisa)
        self.coisas.append(coisa)
        self.add(coisa)

    def rem(self, coisa):
        self.coisas.remove(coisa)
        self.remove(coisa)
        if isinstance(coisa, Lixo):
            self.lixos.remove(coisa)
        elif isinstance(coisa, Lixeira):
            self.lixeiras.remove(coisa)
        elif isinstance(coisa, Flor):
            self.flores.remove(coisa)

    def atualizar(self, m_pos, clique, m_pressi):
        self.gui.atualizar(m_pos, clique)

        for lixeira in self.lixeiras:
            lixeira.atualizar(m_pos, clique, m_pressi, self.mouse)

        for c in self.coisas:
            c.atualizar(m_pos, clique)

        if len(self.lixos) == 0:
            self.vitoria(self)
            self.venceu = True
			
            #Toca som de vitoria
            if self.win == False:
                barulho.parar_musica()
                barulho.tocar_musica("vitoria")
                self.win = True
            
            self.contador_final -= 1
            if not self.contador_final:
                self.fase.fim()
                barulho.parar_musica()
                barulho.tocar_musica("feliz")

    def desenhar(self, s):
#        if self.venceu:
#            pygame.draw.circle(s, (255, 255, 0), (0, 0),
#                               self.estado_vitoria, 5)
        self.gui.desenhar(s)

        for c in self.coisas:
            c.desenhar(s)
        for lixeira in self.lixeiras:
            lixeira.desenhar(s)

