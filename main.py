class NoAVL:
    def __init__(self, chave, nome):
        self.chave = chave
        self.nome = nome
        self.altura = 1
        self.esq = None
        self.dir = None


class ArvoreAVL:
    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def fator_balanceamento(self, no):
        return self.altura(no.esq) - self.altura(no.dir)

    def rotacao_direita(self, y):
        x = y.esq
        T2 = x.dir

        x.dir = y
        y.esq = T2

        y.altura = max(self.altura(y.esq), self.altura(y.dir)) + 1
        x.altura = max(self.altura(x.esq), self.altura(x.dir)) + 1

        return x

    def rotacao_esquerda(self, x):
        y = x.dir
        T2 = y.esq

        y.esq = x
        x.dir = T2

        x.altura = max(self.altura(x.esq), self.altura(x.dir)) + 1
        y.altura = max(self.altura(y.esq), self.altura(y.dir)) + 1

        return y

    def inserir(self, raiz, chave, nome):
        if not raiz:
            return NoAVL(chave, nome)

        if chave < raiz.chave:
            raiz.esq = self.inserir(raiz.esq, chave, nome)
        elif chave > raiz.chave:
            raiz.dir = self.inserir(raiz.dir, chave, nome)
        else:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esq),
                              self.altura(raiz.dir))

        fb = self.fator_balanceamento(raiz)

        if fb > 1 and chave < raiz.esq.chave:
            return self.rotacao_direita(raiz)

        if fb < -1 and chave > raiz.dir.chave:
            return self.rotacao_esquerda(raiz)

        if fb > 1 and chave > raiz.esq.chave:
            raiz.esq = self.rotacao_esquerda(raiz.esq)
            return self.rotacao_direita(raiz)

        if fb < -1 and chave < raiz.dir.chave:
            raiz.dir = self.rotacao_direita(raiz.dir)
            return self.rotacao_esquerda(raiz)

        return raiz

    def buscar(self, raiz, chave):
        if not raiz or raiz.chave == chave:
            return raiz
        if chave < raiz.chave:
            return self.buscar(raiz.esq, chave)
        return self.buscar(raiz.dir, chave)


# Exemplo de uso
arvore = ArvoreAVL()
raiz = None

raiz = arvore.inserir(raiz, 2023001, "Ana")
raiz = arvore.inserir(raiz, 2023002, "Carlos")
raiz = arvore.inserir(raiz, 2023003, "Maria")

resultado = arvore.buscar(raiz, 2023002)
if resultado:
    print("Estudante encontrado:", resultado.nome)
else:
    print("Estudante não encontrado")
