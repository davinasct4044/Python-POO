"""
import subprocess
class Pessoa():
    pass

pessoa1 = Pessoa()
pessoa2 = pessoa1

print(pessoa1 is pessoa2)
"""

class Cachorro():
    def __init__(self,nome):
        self.nome = nome
    pass

dog1 = Cachorro("Rex")
dog2 = Cachorro("Thor")

#desafio

class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    pass

davi = Pessoa("Davi",20)
maria = Pessoa("Maria",25)

#print(davi.nome , maria.nome)
#print(davi.idade , maria.idade)

class Produto():
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        pass
    def exibir_info(self, nome, preco, estoque):
        print(f"Produto:{nome}\nPreço:{preco}\nEstoque:{estoque}")

computador = Produto("Teclado", 100, 10) 
computador.exibir_info()
