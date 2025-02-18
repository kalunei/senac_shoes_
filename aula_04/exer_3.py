'''
Crie um dicionário para o cardápio e adicione um novo sabor com preço. Atualize o preço de um sabor existente e remova um sabor do cardápio.
'''

cardapio = {
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90
}

# novo
cardapio["atum"] = 78.80

# att
cardapio["calabresa"] = 25.80

# del
cardapio.pop("frango com catupiry") # ou del cardapio["frango com catupiry"]

print(cardapio)