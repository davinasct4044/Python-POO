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
        self._estoque = estoque
        pass
    def exibir_info(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self._estoque}")
    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self._estoque:
            print('venda não realizada')
            print(f"restou {self._estoque}")
            
        else:
            self._estoque -= quantidade
            print('venda realizada')
            print(f"restou {self._estoque}")
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self._estoque += quantidade
            print(f'o estoque atual é: {self._estoque}')
        else:
            print('não foi possível mudar o valor pq está negativo')
    @property
    def estoque(self):
        return self._estoque




computador = Produto("Teclado", 100, 10) 
computador.exibir_info()
computador.vender(9)
print(computador.estoque)

 

