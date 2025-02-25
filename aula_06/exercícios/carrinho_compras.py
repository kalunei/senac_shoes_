"""
Carrinho de Compras 🛒​
💡 Enunciado:
Crie um programa que permita adicionar produtos a um carrinho de compras. O programa deve continuar pedindo produtos até que o usuário digite "finalizar". No final, exiba todos os produtos comprados.
📝 Regras:
O usuário digita o nome do produto e ele é adicionado a uma lista.
Se o usuário digitar "finalizar", o programa encerra e mostra os produtos comprados.


🔍 Exemplo esperado:
    Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Pizza
    Produto 'Pizza' adicionado ao carrinho!
    Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): Refrigerante
    Produto 'Refrigerante' adicionado ao carrinho!
    Digite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar): finalizar

    🛍️ Você comprou:
    - Pizza
    - Refrigerante
"""

# var 
pular_l=("_")*90
dicionario_disp = {
    "COCA":3,
    "PIZZA":2,
    "REFRIGERANTE":4,
    "MACARRÃO":1,
    "ARROZ":3,
    "FEIJAO":4,
    "OLEO": 1,
    "LEITE":1,
    "AÇUCAR":4,
    "CAFE": 2,
    "FARINHA":1, 
    "DETERGENTE":2, 
    "SABAO EM PO":2, 
}
dicionario_usuario = {

}
# var 

# function 
print(f"\n{pular_l}\n\n\t\t Bem Vindo ao Supermecado Naguabara!! \n{pular_l}") # nome anti-processo

for item,qnt in dicionario_disp.items():
    print(f"{item} ---> Quantidade disponível: {qnt}")
    

def principal():
    controlador = input("\nDigite um produto para adicionar ao carrinho (ou 'finalizar' para encerrar):" )

    if controlador.upper() in dicionario_usuario:
        dicionario_usuario[controlador.upper()] = dicionario_usuario[controlador.upper()]+1
    else:
        dicionario_usuario[controlador.upper()] = 1
   




    if controlador.upper() in dicionario_disp:
        if dicionario_disp[controlador.upper()] == 1 :
            del dicionario_disp[controlador.upper()]
            print(f"{controlador} foi adicionado a sua esteira de compras 😄")
        else: 
            print(f"{controlador.upper()} foi adicionado a sua esteira de compras 😄")
            dicionario_disp[controlador.upper()] -= 1
            
        
    else:
        print("Erro de digitação ou Produto fora de estoque 😭😭😭😭😭😭😭")



# function 

# programa
x = True
while x:
    principal()
    

    while True:
        laco = input("\ndeseja adicionar mais itens (n\s): ")
        if laco == "n" : x= False ; break
        elif laco == "s" : break
        else : print("Digita direito burro") ; continue

print(f"Sua lista de compras: \n".upper())

for item,chave in dicionario_usuario.items():
    print(f"{item}({chave})")

# programa




input()