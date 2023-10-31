
# CONTEXT MANAGER (aula 240)
'''
    Context Manager com classes - Criando e Usando gerenciadores de contexto
    Você pode implementar seus próprios protocolos
    Para criar um context manager, os métodos __enter__ e __exit__
    devem ser implementados.
    O método __exit__ receberá a classe de exceção, a exceção e o
    traceback. Se ele retornar True, exceção no with será
    suprimidas.

    Ex:
    with open('aula149.txt', 'w') as arquivo:
'''

class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
      


with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n') 
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)

#-----------------------------------------------------------------------------------------------
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        print('-' * 60)
        print(class_exception) # exibe class da exceção
        print(exception_) # exibe tipo da exceção
        print(traceback_) # exibe objeto da exceção
        print('-' * 60)
        return True # ignora a exceção


with MyOpen('aula149.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123) # gerar erro (exceção)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)
