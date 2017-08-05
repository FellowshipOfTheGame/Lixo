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


def carregar_imagem(arquivo):
    #Carrega uma imagem de dentro do diretório gfx
    return pygame.image.load(os.path.join("gfx", arquivo))


def carregar_fonte(arquivo, tamanho):
    #Carrega uma fonte de dentro do diretório fonts
    return pygame.font.Font(os.path.join("fonts", arquivo), tamanho)

