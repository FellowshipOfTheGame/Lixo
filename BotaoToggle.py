from Elemento import Elemento
from BotaoSimples import BotaoSimples
class BotaoToggle(Elemento):

    def __init__(self, funcao1, texto1, imagem1, funcao2, texto2, imagem2):
        self.atual = BotaoSimples(funcao1, texto1, imagem1)
        self.outro = BotaoSimples(funcao2, texto2, imagem2)

    def alt_cor(self, r, g, b):
        self.atual.alt_cor(r, g, b)
        self.outro.alt_cor(r, g, b)

    def posicionar(self, x, y):
        self.atual.posicionar(x, y)
        self.outro.posicionar(x, y)

    def ret_alt(self):
        return self.atual.ret_alt()

    def ret_lar(self):
        return self.atual.ret_lar()

    def atualizar(self, mouse, clique):
        self.atual.sobre = self.atual.rect.collidepoint(mouse)

        if self.atual.sobre and clique:
            self.atual.funcao()
            self.atual, self.outro = self.outro, self.atual

    def desenhar(self, s):
        s.blit(self.atual.img_botao, (self.atual.x, self.atual.y))
        s.blit(self.atual.imag_texto, self.atual.posTexto)
