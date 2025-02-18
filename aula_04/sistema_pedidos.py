# Cardápio pizzaria 
cardapio ={
    "mussarela": 25.90,
    "calabresa": 27.90,
    "frango com catupiry": 29.90
}

pedido = []

# Pedido cliente
pedido = []
pedido.append ("mussarela")
pedido.append ("calabresa")

# Calcular total do pedido
total_pedido = sum(cardapio[i] for i in pedido) 

# Resumo do pedido 
for i in pedido:
    print(f'🍕 - {i}: R$ {cardapio[i]:.2f}')
sep = ("-")*35
print(f'{sep} \n Total do pedido: R$ {total_pedido}')



input()
