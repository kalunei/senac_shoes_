"""
Homogênio --> Aceita somente um tipo de dado;

Heterogênio --> Aceita mais de um tipo de dado;

As estruturas de dados em py. são declaradas com snake_case
"""


# Declaração de listas [].
# Ordenadas, mutáveis e heterogênias.

sabores = ["Calabresa", "Frango com catupiry", "Mussarela", "Portuguesa"]
dados_pizza = [["Calabresa", 29.90], ["Frango com catupiry", 29.90], ["Mussarela", 29.90], ["Portuguesa", 29.90]]


sabores.append("Margherita")
sabores.remove("Calabresa")