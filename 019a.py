# Escrever texto no arquivo
arquivo = open('texto_a.txt', 'w', encoding='utf8') # Abre o arquivo "myfile.txt" para leitura
arquivo.writelines(
'''
Prezado(a) %{nome},

Informamos que sua mensalidade será cobrada no valor de %{valor} no dia %{data}. Caso deseje cancelar o serviço, entre em contato com a %{empresa} pelo telefone %telefone.

Atenciosamente: %{empresa}
'''
) 

# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'texto_a.txt' # caminho do arquivo

locale.setlocale(locale.LC_ALL, 'pt_BR') # configurações de idioma

'''
    # symbol=False: Este é um argumento de palavra-chave opcional que especifica se o símbolo 
    de moeda deve ser incluído na cadeia de caracteres formatada. 
    Exemplo:
    resposta = locale.currency(123456, symbol=True)
    resposta = R$ 1234,56

    # grouping=True: Este é outro argumento de palavra-chave opcional que especifica se os 
    separadores de agrupamento (por exemplo, vírgulas) devem ser aplicados à cadeia de 
    caracteres formatada. 
    Exemplo:
    resposta = locale.currency(123456, grouping=True)
    resposta = 1.234,56
'''

def converte_para_brl(numero: float) -> str:
    # formatar um número de acordo com as regras de formatação de moeda da localidade atual
    brl = locale.currency(numero, symbol=True, grouping=True)
    return brl


data = datetime(2022, 12, 28)

# dicionário
dados = dict(
    nome='João',
    valor=converte_para_brl(1234567), # função converte_para_brl
    data=data.strftime('%d/%m/%Y'), # formatação data
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

'''
    # string.Template()
    É uma função que substitui espaços reservados em uma cadeia de caracteres, 
    geralmente é feito usando um dicionário ou outra estrutura de dados que 
    mapeia nomes de espaço reservado para seus valores correspondentes. 
'''
class MyTemplate(string.Template):
    delimiter = '%'


with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read() # ler arquivo
    template = MyTemplate(texto) # class MyTemplate
    print(template.safe_substitute(dados)) # método usado para substituir variáveis em um template.

