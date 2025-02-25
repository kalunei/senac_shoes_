"""
 Exercício Bônus 💡​
Simulação de Senha de Banco 🔐​
💡 Enunciado:
Crie um sistema que peça para o usuário digitar uma senha para acessar sua conta bancária. Ele tem apenas 3 tentativas para acertar a senha correta. Se ele errar as 3 vezes, o sistema bloqueia a conta.
📝 Regras:
A senha correta é "1234".
O usuário tem até 3 tentativas para acertar.
Se errar as 3 vezes, exiba "🚫 Conta bloqueada!".
🔍 Exemplo esperado:
Digite sua senha: 1111
❌ Senha incorreta! Tentativas restantes: 2
Digite sua senha: 2222
❌ Senha incorreta! Tentativas restantes: 1
Digite sua senha: 3333
🚫 Conta bloqueada!
"""

# var
import random as rd
senha = 1234
# var

# função(s) 
def capcha():
    seta =["⬅","➡","⬆","⬇"] #"↗","↘","↙","↖"para incrementar depois
    seta_l =["esquerda","direita","cima","baixo"]

    while True:
        numero_random = rd.randint(0,3)
        print(f"\n\n\t\t{seta[numero_random]}")


        seta_usuario=input(f"Digite a seta correta para provar que você não é robo \n Opções: {seta_l}\n\t :")

        if seta_l[numero_random].upper() == seta_usuario.upper(): 
            break
        else:
            print("Erro no capcha")



def test_senha():
    tentantivas = 3
    acesso = True
    while acesso:
       capcha()

       senha_test = int(input(f"Digite sua senha ({tentantivas} Restantes): "))
       if senha_test == senha:
           print("Acesso liberado")
           break
       elif senha_test != senha:
           print("Senha incorreta")
           tentantivas-=1
           if tentantivas >= 1:
               continue
           else:
               print("🚫 Conta bloqueada!")
               break
        
# função(s)

# programa
test_senha()
# programa