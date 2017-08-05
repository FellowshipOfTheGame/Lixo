
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
import animacoes

from pygame.sprite import Sprite

from funcoes import carregar_imagem
class Flor(Sprite):
    """ Flores exibidas ao terminar a fase """
    def __init__(self, mundo, pos):
        Sprite.__init__(self)
        self.mundo = mundo
        self.image = carregar_imagem("flor01.png")
        self.image_copy = None
        self.rect = self.image.get_bounding_rect()
        self.rect.x += pos[0]
        self.rect.y += pos[1]
        self.rect.x -= self.image.get_width() / 2
        self.rect.y += self.image.get_height() / 2
        self.estado = -1  # -1 = "pronta pra nascer,
                          # 0 = "nascendo" e crescendo,
                          # 1 = alargando, 2 = estavel
        self.altura = 10
        self.largura = 10
        self.animar = animacoes.animar_flor
        self.mundo.adi(self)

    def atualizar(self, m_pos, clique):
        self.animar(self)

    def desenhar(self, s):
#        print self.image.get_width()
        if self.estado == 2:
            s.blit(self.image, (self.rect.x - self.image.get_width() / 2,
                                self.rect.y - self.image.get_height()))
        else:
            s.blit(self.image_copy,
                   (self.rect.x - self.image_copy.get_width() / 2,
                    self.rect.y - self.image_copy.get_height()))
                    # desenhar a BASE onde estava o lixo
#            print self.rect.x - self.image_copy.get_width()/2,
#                   self.rect.y + self.image_copy.get_height()

    def brotar(self):
        self.estado = 0

    def sobre(self):
        pass
