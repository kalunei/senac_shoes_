# aluno --> nome, idade, endereço, cpf 

barra = ("-")*40

class Aluno: # utilizamos por padrão PascalCase para classes.

    def __init__(self, nome, idade, endereco, cpf) :
        self.nome = nome # Ana 
        self.idade = idade # 22 
        self.endereco =  endereco # Rua 1 
        self.cpf = cpf # 123
        self.matriculado = True # toda vez que um aluno for matriculado esse campo será True (default), toda cópia da classe Aluno terá essa característica
    # atributos -> dentro de um construtor
    # métodos -> 


    def situacao(self):
        if self.matriculado == True:
            self.matriculado = False

        elif self.matriculado == False:
            self.matriculado = True
        
        

    # Método que exibe as informações do aluno
    def exibir_info(self):
        print( f'''
        {barra}
         DADOS DO ESTUDANTE
        {barra}
        👩‍🎓👨‍🎓O nome do(a) aluno(a) é {self.nome}
        e o CPF é {self.cpf}
        {barra}
        
        ''')




# Criando cópias da classe Aluno (instânciação)
a1 = Aluno("Ana", 22, "Rua 1", "123456")
a2 = Aluno("Bia", 20, "Rua 16", "234567")

print(a1)
a1.exibir_info()
