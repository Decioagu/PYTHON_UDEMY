'''
    # Implementando o protocolo do "Iterator" em Python
    # Essa é apenas uma aula para introduzir os protocolos de collections.abc no
    # Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
    # estrutura usada nessa aula.
    # https://docs.python.org/3/library/collections.abc.html

    A classe abstrata Sequence define uma interface comum para sequências em Python, 
    como listas, tuplas e strings. Isso significa que qualquer classe que implementa 
    a interface Sequence deve fornecer os métodos definidos nela,
    como __len__, __getitem__, __iter__ e __contains__.

    * __len__(): Retorna o comprimento da sequência.
    * __getitem__(): Obtém um elemento da sequência pelo seu índice.
    * __iter__(): Retorna um iterador para a sequência.
    * __contains__(): Verifica se um elemento está presente na sequência.

    Além desses métodos abstratos, a classe Sequence também define alguns métodos mixin que podem ser sobrescritos, mas não são necessários para implementar a interface Sequence. Esses métodos incluem:

    * index(): Obtém o índice de um elemento na sequência.
    * count(): Conta o número de vezes que um elemento aparece na sequência.

    Alguns exemplos de classes que implementam a interface Sequence incluem:

    * list(): Listas são sequências mutáveis que podem ser criadas usando a função list().
    * tuple(): Tuplas são sequências imutáveis que podem ser criadas usando a função tuple().
    * str(): Strings são sequências imutáveis de caracteres que podem ser criadas usando a função str().
'''
from collections.abc import Sequence

class MySequence(Sequence):

  def __init__(self, data):
    self.data = data

  def __len__(self):
    return len(self.data)

  def __getitem__(self, index):
    return self.data[index]

  def __iter__(self):
    return iter(self.data)

  def __contains__(self, item):
    for element in self.data:
      if element == item:
        return True
    return False


my_sequence = MySequence(["a", "b", "c"])

print(my_sequence.)

print("a está presente na sequência:", "a" in my_sequence)
print("d não está presente na sequência:", "d" in my_sequence)

print('<==========================================================>')

from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self): # construtor
        self._data = {} # dicionário
        self._index = 0
        self._next_index = 0 

    def append(self, *values): # adiciona valores no dicionário
        for value in values:
            self._data[self._index] = value
            self._index += 1
            # resposta = {self._index: 'valor'}

    def __len__(self) -> int:
        return self._index

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')