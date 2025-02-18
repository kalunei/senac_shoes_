'''
1. **Lista de Pedidos**
    `Crie uma lista de sabores de pizzas pedidos` pelo cliente. Adicione `3 sabores à lista` e `remova 1 sabor.` Exiba o pedido final.
'''

sabores = ["calabresa", "catupiry", "frango", "atum"]

s1 = input("Digite o 1° sabor da pizza que deseja: ")
s2 = input("Digite o 2° sabor da pizza que deseja: ")
s3 = input("Digite o 3° sabor da pizza que deseja: ")

sabores.append(s1)
sabores.append(s2)
sabores.append(s3)
print("Adicionados!")

s_1 = input("Digite o 1° sabor da pizza que deseja remover: ")
sabores.remove(s_1)
print("Removidos!")

print(sabores)