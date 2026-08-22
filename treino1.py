"""
import subprocess
class Pessoa():
    pass

pessoa1 = Pessoa()
pessoa2 = pessoa1

print(pessoa1 is pessoa2)
"""



#dog1 = Cachorro("Rex")
#dog2 = Cachorro("Thor")

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
    def exibir_info(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: {self.preco}")
        print(f"Estoque: {self.estoque}")
    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self._estoque:
            self._estoque -= quantidade
            print('venda realizada')
            print(f"restou {self.estoque}")
            
        else:
            print('venda não realizada')
            print(f"restou {self.estoque}")
            
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self._estoque += quantidade
            print(f'o estoque atual é: {self.estoque}')
        else:
            print('não foi possível mudar o valor pq está negativo')
    @property
    def estoque(self):
            return self._estoque

    @estoque.setter
    def estoque(self, valor):
        if valor >= 0:
            self._estoque = valor
        else:
            print('o estoque não pode ser negativo')




#computador = Produto("Teclado", 100, 10) 
#computador.adicionar_estoque(2)




from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome
    def comer(self):
        print(f' {self.nome} comeu')
    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade
    pass
    def falar(self):
        print('au au')

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome)
        self.idade = idade
    def miar(self):
        print('miau')
    def falar(self):
        print('ai ai')

""" 
super() permite que uma classe filha utilize métodos da classe pai, especialmente o __init__, sem precisar reescrever sua lógica.
"""

animais = [Gato("fiu", 10), Cachorro("bro", 12)]

for falas in animais:
    falas.falar()
