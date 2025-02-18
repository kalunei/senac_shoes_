### D I C I O N Á R I O S ###
"""
Dicionários (listas mutaveis)
    ---> São acompanhados por uma 'chave:valor'
    ---> 
"""

##/ EX:
cardapio = {
    "mussarela": 25.90, 
    "calabresa": 27.90, 
}

print(cardapio)
##*/ EX:


##/ Operações com dicionário :

#/ Acessar itens; 
print("🍕 Mussarela:", cardapio["mussarela"])
#*/ Acessar itens. 

#/ Adicionar itens;
cardapio["portuguesa"] = 30.90
print("Cardápio atualizado:", cardapio)
#*/ Adicionar tiens.

#/ Atualizar valores;
cardapio["mussarela"] = 26.90
print("Preço do cardápio atualizado:", cardapio)
#*/ Atualizar valores.


#/ Iterar sobre o dicionário;
for sabor,preco in cardapio.items():
    print(f'A pizza de {sabor} custa R$ {preco}.') 
#*/ Iterar sobre o dicionário.

##*/ Operações com dicionário :