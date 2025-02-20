"""
Caixa Eletrônico 💰​
💡 Enunciado:
Crie um programa que simule um caixa eletrônico. O usuário deve poder sacar valores até que o saldo disponível acabe ou até que ele digite "sair".
📝 Regras:
Comece com um saldo inicial de R$ 500.
Peça para o usuário digitar um valor para saque.
Se o valor for maior que o saldo, avise que não há saldo suficiente.
Se o usuário digitar "sair", encerre o programa.
🔍 Exemplo esperado:
Saldo disponível: R$ 500
Digite o valor para sacar ou 'sair' para encerrar: 200
Saque realizado! Novo saldo: R$ 300
Digite o valor para sacar ou 'sair' para encerrar: 400
❌ Saldo insuficiente!
Digite o valor para sacar ou 'sair' para encerrar: sair
🏦 Operação encerrada.
"""

# var
saldo = float(500)
ciclo = True
valor = float()
# var

# função(s)
def comparacao():
    global saldo

    while True:
        valor = input(f"Você tem {saldo:.2f}, quando deseja retirar: ")
        try:
            valor=float(valor)
            break
        except:
            print("Erro de digitação(1)")

            
    valor = float(valor)
    if valor != type(str):
        if valor < saldo or valor == saldo :
            saldo = saldo - valor
            print(f"Você retirou :{valor:.2f} \n Valor restante na conta: {saldo:.2f}")
        else:
            print("Não há saldo suficiente")
    else:
        print("Erro de digitação(2)")   


def repeticao():
    global ciclo
    x = input("Digite o 'sacar' para sacar novamente  ou 'sair' para encerrar:")

    if x.lower() == "sair":
        ciclo = False
        print("\n\n\t (Você saiu) \n\t  TENHA UM BOM DIA !!!")
    elif x.lower() == "sacar":
        print(("_")*30)
    else:
        print("Erro de digitação(3)")
        repeticao()
# função(s)
    
# programa

while ciclo:
    comparacao()
    repeticao()



# programa