"""
Homogênio --> Aceita somente um tipo de dado;

Heterogênio --> Aceita mais de um tipo de dado;

As estruturas de dados em py. são declaradas com snake_case.
"""


## Declaração de listas [];
# Ordenadas, mutáveis e heterogênias.

sabores = ["Calabresa", "Frango com catupiry", "Mussarela", "Portuguesa"]
dados_pizza = [["Calabresa", 29.90], ["Frango com catupiry", 29.90], ["Mussarela", 29.90], ["Portuguesa", 29.90]]



## Operações com Listas

# 1. apppend() -> Adiciona um novo valor ao final da lista;
sabores.append("Margherita")

# 2. remove() -> Remove o primeiro valor da lista;
sabores.remove("Calabresa")

# 3. sort() -> Ordena a lista;
sabores.sort()

# 4. reverse() -> Inverte a ordem da lista;
sabores.reverse()

# 5. len() -> Retorna o tamanho da lista;
len(sabores)

# 6. clear() -> Limpa a lista;
sabores.clear()

# 7. copy() -> Copia a lista;
sabores_copy = sabores.copy()

# 8. count() -> Conta quantas vezes um valor aparece na lista;
sabores.count("Mussarela")

# 9. extend() -> Adiciona um novo valor ao final da lista;
sabores.extend(["Calabresa", "Frango com catupiry", "Mussarela", "Portuguesa"])

# 10. insert() -> Insere um novo valor na posição especificada;
sabores.insert(2, "Margherita")

# 11. pop() -> Remove o ultimo valor da lista;
sabores.pop()

# 12. index() -> Retorna o indice do valor especificado;
sabores.index("Mussarela")
