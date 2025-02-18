'''
4. **Controle de Estoque**
`Crie` um `dicionário com os estoques` de cada sabor. `Decremente` o estoque conforme os pedidos feitos e exiba uma `mensagem se o
 estoque acabar.`
'''


estoque = {
    "uva": 1,
    "abacaxi": 2,
    "banana": 1,
    "pavê": 2,
    "melancia": 3,
    "laranja": 2,
    "pudin": 1
}


pedido = input("Digite o item desejado: ")

if pedido in estoque : 
    estoque[pedido] -= 1 
    restante = estoque[pedido]
    if restante == 0:
        print("Estoque de uva acabou")
        del estoque[pedido]
elif pedido not in estoque:
    print("Item fora de estoque")
else:
    print("Estoque completamente vazio")
