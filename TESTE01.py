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