# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000 # empréstimo 
inicio_emprestimo = datetime(2020, 12, 20) # inicio do empréstimo
tempo_de_emprestimo = relativedelta(years=5) # tempo do empréstimo em anos
fim_emprestimo = inicio_emprestimo + tempo_de_emprestimo # fim do empréstimo
parcelas= [] # data das parcelas
data_parcela = inicio_emprestimo # 2020-12-20 até 2025-12-20

while data_parcela < fim_emprestimo: # número de parcelas por mês
    parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

numero_de_parcelas = len(parcelas) # número de parcelas em meses
valor_parcela = valor_total / numero_de_parcelas # valor da parcela no mês

for num, data in enumerate(parcelas, start=1): # exibir parcelas e valor
    print(f'{num}º parcela:', data.strftime('%d/%m/%Y'), f'| Valor R$: {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {tempo_de_emprestimo.years} anos '
    f'({numero_de_parcelas} meses) em parcelas fixa de '
    f'R$ {valor_parcela:,.2f}' 
    )