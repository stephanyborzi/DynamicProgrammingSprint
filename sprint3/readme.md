# Explicação do Projeto

## Listagem de Pedidos
O projeto possui a possibilidade de exibição de todos os pedidos cadastrados em uma lista de dicionários, seja por ordem cronológica ou pela ordem de resposta do usuário. Dessa forma é possível visualizar todos os pedidos de forma clara e organizada.

### Fila de Pedidos
```
def listagem(lista):
    var = ""
    for i in lista:
        var+=f"""Pedido {i["id_pedido"]}:\n{i}\n"""
    return var
```
### Pilha de Atendimento
```
def historico(lista):
    lista.reverse()
    executar(listagem, lista=lista)
    lista.reverse()
```

## Busca de Pedidos
Para localizar pedidos em uma lista de dicionários, foram implementadas duas funções de busca: uma utilizando o algoritmo de busca binária e outra utilizando a busca linear. Ambas as funções recebem uma lista de dicionários e um `id_pedido` como parâmetros e retornam o dicionário correspondente ao pedido, caso encontrado, ou uma mensagem indicando que o pedido não foi localizado.

### Busca Binária em Lista de Dicionários
A busca binária é eficiente para listas ordenadas, reduzindo o número de comparações necessárias para encontrar o item desejado.
```
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
```

### Busca Linear em Lista de Dicionários
A busca linear percorre cada elemento da lista até encontrar o item desejado ou até o final da lista.
```
def busca_linear(lista, id_buscado):
    for i in range(len(lista)):
        if lista[i]["id_pedido"] == id_buscado:
            return lista[i]

    return "Pedido não localizado"
```

## Ordenação de Pedidos
Para permitir uma melhor organização dos pedidos, foi implementada uma função de ordenação customizada.

### Ordenação por quantidade
Devido à importância de se manter um controle rigoroso sobre a quantidade de insumos em estoque, foram desenvolvidas duas funções de ordenação: uma utilizando o algoritmo Quick Sort e outra utilizando o Merge Sort. Ambas as funções organizam a lista de pedidos com base na quantidade de insumos, facilitando a gestão do inventário.
```
def quantidade_quick(lista):
    if len(lista) <= 1:
        return lista

    else:
        pivo = lista[0]["quantidade"]
        menores = [x for x in lista[1:] if x["quantidade"] <= pivo]
        maiores = [x for x in lista[1:] if x["quantidade"] > pivo]

        return quantidade_quick(menores) + [lista[0]] + quantidade_quick(maiores)
```
```
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
```

### Ordenação por validade
Considerando a importância de monitorar a validade dos insumos para garantir a segurança e a qualidade dos produtos, foram implementadas duas funções de ordenação: uma utilizando o algoritmo Quick Sort e outra utilizando o Merge Sort. Ambas as funções organizam a lista de pedidos com base na data de validade dos insumos, facilitando a gestão do estoque e a tomada de decisões.
```
def validade_quick(lista):
    if len(lista) <= 1:
        return lista

    else:
        pivo = lista[0]["insumo"]["validade"]
        menores = [x for x in lista[1:] if x["insumo"]["validade"] <= pivo]
        maiores = [x for x in lista[1:] if x["insumo"]["validade"] > pivo]

        return validade_quick(menores) + [lista[0]] + validade_quick(maiores)
```
```
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
```