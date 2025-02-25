# Sintaxe Básica de uma Função 

'''    
    def --> palabra reservada para a função``
'''

def nome_funcao(parametros):
    #`Código da função` 
    alguma_coisa = 0 
    return alguma_coisa # Pode ou nao ser usada para retornar algo






# Função sem retorno
def ola_mundo():
    print("Olá mundo!")


ola_mundo() # Invocando a função








# Função com parâmetros 
def saudacao(nome):
    print(f'Olá seja bem-vindo(a) {nome}')

saudacao("William")
saudacao("Ana")





# Função com parâmetros e retorno 
def somar(numere1, numere2):
    soma = numere1+numere2
    return soma

print(somar(10,20))
print(somar(1,2))
print(somar(210,320))



