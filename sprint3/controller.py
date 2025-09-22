import pprint

from utils import *

def busca_binaria(lista, id_buscado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio]["id_pedido"] == id_buscado:
            return lista[meio]
        elif lista[meio]["id_pedido"] < id_buscado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return "Pedido não localizado"

def busca_linear(lista, id_buscado):
    for i in range(len(lista)):
        if lista[i]["id_pedido"] == id_buscado:
            return lista[i]

    return "Pedido não localizado"

def quantidade_quick(lista):
    if len(lista) <= 1:
        return lista

    else:
        pivo = lista[0]["quantidade"]
        menores = [x for x in lista[1:] if x["quantidade"] <= pivo]
        maiores = [x for x in lista[1:] if x["quantidade"] > pivo]

        return quantidade_quick(menores) + [lista[0]] + quantidade_quick(maiores)

def validade_quick(lista):
    if len(lista) <= 1:
        return lista

    else:
        pivo = lista[0]["insumo"]["validade"]
        menores = [x for x in lista[1:] if x["insumo"]["validade"] <= pivo]
        maiores = [x for x in lista[1:] if x["insumo"]["validade"] > pivo]

        return validade_quick(menores) + [lista[0]] + validade_quick(maiores)

def merge_sort(lista, merge_type):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], merge_type)
    direita = merge_sort(lista[meio:], merge_type)

    return merge_type(esquerda, direita)

def quantidade_merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i]["quantidade"] <= direita[j]["quantidade"]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def validade_merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i]["insumo"]["validade"] <= direita[j]["insumo"]["validade"]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def opcao_busca(lista, id):
    print(f"""
Selecione o tipo de busca:
(Total de pedidos cadastrados: {len(lista)})

(1) - Linear
(2) - Binária
""")

    match str(input("R:")):
        case "1":
            executar(busca_linear, lista=lista, id_buscado=id)
        case "2":
            executar(busca_binaria, lista=lista, id_buscado=id)
        case _:
            print("Opção inválida")

def campo_ordenacao(lista):
    print(f"""
Selecione o campo à ser ordenado:

(1) - Quantidade de insumos
(2) - Validade
""")

    campo = str(input("R:"))
    match campo:
        case "1":
            tipo_ordenacao(lista, campo)
        case "2":
            tipo_ordenacao(lista, campo)
        case _:
            print("Opção inválida")

def tipo_ordenacao(lista, campo):
    print(f"""
Selecione o tipo de ordenação ordenado:

(1) - Quick
(2) - Merge
""")

    match str(input("R:")):
        case "1":
            ordenacao_quick(lista, campo)
        case "2":
            ordenacao_merge(lista, campo)
        case _:
            print("Opção inválida")

def ordenacao_quick(lista, campo):
    if campo == "1":
        executar(quantidade_quick, lista=lista)
    else:
        executar(validade_quick, lista=lista)

def ordenacao_merge(lista, campo):
    if campo == "1":
        executar(merge_sort, lista=lista, merge_type=quantidade_merge)
    else:
        executar(merge_sort, lista=lista, merge_type=validade_merge)

def listar_todos(lista):
    executar(listagem, lista=lista)

def listagem(lista):
    var = ""
    for i in lista:
        var+=f"""Pedido {i["id_pedido"]}:\n{i}\n"""
    return var

def historico(lista):
    lista.reverse()
    executar(listagem, lista=lista)
    lista.reverse()

def menu(db):
    print("""
Selecione uma função:

(1) - Buscar um pedido
(2) - Ordenar pedidos
(3) - Exibir todos os pedidos
(4) - Exibir histórico
(5) - Encerrar
""")

    match str(input("R:")):
        case "1":
            opcao_busca(db, valor_buscado())
            return None
        case "2":
            campo_ordenacao(db)
            return None
        case "3":
            listar_todos(db)
            return None
        case "4":
            historico(db)
            return None
        case "5":
            return True
        case _:
            print("Opção inválida")
            return None