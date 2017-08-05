#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from math import sqrt


def animar_estrela(self):
    if self.estado == 0:
        if self.certo:
            self.rect.y -= 5
        else:
            self.rect.y += 5
        self.ticks -= 1
        if self.ticks <= 0:
            self.estado = 1
            self.ticks = 30
    else:
        self.ticks -= 1
        if self.ticks <= 0:
            self.mundo.rem(self)


def animar_flor(self):
    if self.estado == -1:
        self.image_copy = pygame.transform.scale(self.image, (0, 0))
    elif self.estado == 0:
        self.image_copy = pygame.transform.scale(self.image, (self.largura,
                                                              self.altura))
#        print self.largura, self.altura
        if self.altura <= 150:
            self.altura += 5
        else:
            self.estado = 1
    elif self.estado == 1:
        ok1 = True
        ok2 = True
        self.image_copy = pygame.transform.scale(self.image, (self.largura,
                                                              self.altura))
        if self.largura <= self.image.get_width():
            self.largura += 5
            ok1 = False
        if self.altura >= self.image.get_height():
            self.altura -= 5
            ok2 = False
        if ok1 and ok2:
            self.estado = 2


def animar_lixo(self):
    if self.retornando == True:
        dx = self.pos_anterior[0] - self.rect.x
        dy = self.pos_anterior[1] - self.rect.y
        dist = math.sqrt(dx * dx + dy * dy)

        if dist <= 15:  # chegou praticamente no lugar certo
            self.rect.x, self.rect.y = self.pos_anterior
            self.retornando = False
#            self.apto = True
            # para nao colidir com outras lixeiras ate chegar ao destino
            self.tem_estrela = False
        else:
            if self.tem_estrela == False:
                self.adicionar_estrela()
            self.rect.x += 20 * dx / (dist)  # anda 20 px por "frame"
            self.rect.y += 20 * dy / (dist)
#            self.apto = False # para que não possa colidir novamente


def animar_vitoria(self):
    if self.estado_vitoria < 1792:  # altura + largura da tela
        for f in self.flores:
            if (((f.estado == -1) and
                 (f.rect.x + f.rect.y) <= self.estado_vitoria)):
                f.brotar()
                #print(f.rect.x, f.rect.y, f.rect.x + f.rect.y,
                      #self.estado_vitoria)
        self.estado_vitoria += 20
