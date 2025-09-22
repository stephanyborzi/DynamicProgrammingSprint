from datetime import datetime
import calendar
import time
import pprint

def executar(func, **kwargs):
    tempo_inicio = time.time()
    pprint.pprint(func(**kwargs))
    tempo_fim = time.time()
    print(f"Tempo de execução: {tempo_fim - tempo_inicio:.6f} segundos")

def add_months(current_date, months_to_add):
    new_month = (current_date.month - 1 + months_to_add) % 12 + 1
    new_year = current_date.year + (current_date.month - 1 + months_to_add) // 12

    last_day_of_month = calendar.monthrange(new_year, new_month)[1]
    new_day = min(current_date.day, last_day_of_month)

    return datetime(new_year, new_month, new_day,
                    current_date.hour, current_date.minute, current_date.second)

def valor_buscado():
    try:
        return int(input("ID do pedido: "))

    except RuntimeError:
        print("Valor inválido")
        return -1