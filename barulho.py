#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#-----------------------------------------------------------------------------
# Copyright 2008 The Fellowship of the Game
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

"""Biblioteca que cuida dos sons e das músicas"""

from os import path

import pygame


FREQ = 44100   # same as audio CD
BITSIZE = -16  # unsigned 16 bit
CHANNELS = 2   # 1 == mono, 2 == stereo
BUFFER = 1024  # audio buffer size in no. of samples

PASTA = "sons"

LIGADO = True
TIPOS_DESLIGADOS = []
CERTO_ERRADO = False

SONS = {}
MUSICAS = {}




def carr_som(nome_arquivo, nome=None, tipo=None):
    """Carrega um som de uma arquivo e o coloca no vetor de sons"""
    if nome is None:
        nome = nome_arquivo

    arq = path.join(PASTA, nome_arquivo)
    SONS[nome] = (tipo, pygame.mixer.Sound(arq))


def carr_musica(nome_arquivo, nome=None):
    """Carrega uma música de um arquivo e a coloca no vetor de músicas"""
    if nome is None:
        nome = nome_arquivo

    arq = path.join(PASTA, nome_arquivo)
    MUSICAS[nome] = arq


def alt_pasta(nova):
    """Altera a pasta onde estão os sons"""
    global PASTA
    PASTA = nova

def tocar_som_sozinho(nome):
    global ULTIMO_CANAL
    global CERTO_ERRADO
    """Toca um som de acordo com o índice dele no vetor de sons"""
    if LIGADO and pode_substituir():
        pygame.mixer.stop()
        CERTO_ERRADO = False
        tipo, som = SONS[nome]
        if tipo not in TIPOS_DESLIGADOS:
            som.set_volume(1)
            ULTIMO_CANAL = som.play()        
        
def pode_substituir():
    """Verifica se o som tocando no momento é o prioritário (dizer se acertou ou errou)"""
    if CERTO_ERRADO and ULTIMO_CANAL.get_sound() != None :
        return False
    else: return True
    
def tocar_musica(nome):
    """Toca uma música de acordo com o índice dela no vetor de músicas"""
    if LIGADO:
        pygame.mixer.music.load(MUSICAS[nome])
        pygame.mixer.music.set_volume(0.15)
        pygame.mixer.music.play()


def parar_musica():
    """Para de tocar a música"""
    pygame.mixer.music.stop()


def desligar():
    """Para de tocar a música e os sons"""
    global LIGADO
    LIGADO = False
    pygame.mixer.stop()
    pygame.mixer.music.stop()


def desligar_tipo(tipo):
    """Desliga um tipo de sons"""
    TIPOS_DESLIGADOS.append(tipo)


def ligar_tipo(tipo):
    """Liga um tipo de som"""
    TIPOS_DESLIGADOS.remove(tipo)


def alt_tipo(tipo):
    """Alterna um tipo de som entre ligado e desligado"""
    if tipo in TIPOS_DESLIGADOS:
        TIPOS_DESLIGADOS.remove(tipo)
    else:
        TIPOS_DESLIGADOS.append(tipo)


def ret_tipo(tipo):
    """Retorna se o tipo está desligado"""
    if tipo in TIPOS_DESLIGADOS:
        return True
    else:
        return False


def ligar():
    """Ativa o tocar de sons e da música"""
    global LIGADO
    LIGADO = True
    pygame.mixer.music.play()


def alt_ligado():
    """Alterna entre ligado e desligado o tocar de sons e da música"""
    global LIGADO
    LIGADO = not LIGADO
    if not LIGADO:
        pygame.mixer.stop()
        pygame.mixer.music.stop()


def inicio():
    """Inicializa essa biblioteca"""
    try:
        pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
    except:
        #print("Erro ao tentar inicializar sistema de sons!")
        pass


def fim():
    """Finaliza essa biblioteca"""
    pygame.mixer.quit()
