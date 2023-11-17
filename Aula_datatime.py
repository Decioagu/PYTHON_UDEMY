'''
    O módulo datetime em Python fornece classes para manipular datas e horas. 
    Ele suporta uma ampla gama de operações, incluindo:

    # https://pt.wikipedia.org/wiki/Era_Unix
    # datetime.fromtimestamp(Unix Timestamp)
    # https://docs.python.org/3/library/datetime.html
    # Para timezones
    # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    # Instalando o pytz
    # pip install pytz types-pytz
'''

# criar data e hora
from datetime import datetime

data1 = datetime(2023, 5, 15) # (ano, mês, dia)
print(data1, type(data1))
data2 = datetime(2022, 4, 20, 7, 49, 23) # (ano, mês, dia, hora, min., seg.)
print(data2, type(data2))

data_str_data = '2022/04/20 07:49:23'
data_str_fmt = '%d/%m/%Y %H:%M:%S'
data3 = datetime.strptime(data_str_data, data_str_fmt)
print(data3, type(data3))
#-----------------------------------------------------------------------------------------------

# data de hoje
from datetime import date

today = date.today() # data de hoje

print("Today:", today) # ano/mês/dia
print("Year:", today.year) # ano
print("Month:", today.month) # mês
print("Day:", today.day) # dia

print('<==========================================================>')
#-----------------------------------------------------------------------------------------------
