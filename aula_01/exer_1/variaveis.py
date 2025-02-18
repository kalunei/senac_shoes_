''' 
        Pizzaria sabores;
        Calabresa, Mussarela, Frango;
        Grande.
'''
controle = 1
while True:
        
        if controle == 1: pizza = input("Digite a pizza desejada: ")
        controle= controle +1
        TAMANHO_DA_PIZZA = "Grande" #constante fake
        preço = 29.90
        barra = ("="*45)
        print(f""" 
        {barra}
                A pizza escolhida é {pizza},
                a pizza é {TAMANHO_DA_PIZZA}
                e o preço dela é {preço}

        {barra}
        """)
        
