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

    def __len__(self) -> int: # retorna o comprimento da sequência.
        return self._index

    def __getitem__(self, index): # obtém um elemento da sequência pelo seu índice
        return self._data[index]

    def __setitem__(self, index, value): # atualiza um elemento da sequência pelo seu índice
        self._data[index] = value

    def __iter__(self): # retorna um iterador para a sequência.
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
    print(lista)
    lista.append('Maria', 'Helena', 'Décio')
    print(lista[0])
    print(lista[1])
    print(lista[2])

    lista[0] = 'João'
    # lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    # for item in lista:
    #     print(item)
    # print('---')
    # for item in lista:
    #     print(item)
    # print('---')
    # atualizado