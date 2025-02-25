# Criando Superclass Pessoa 
class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf 

    def exibir_dados(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Cpf: {self.cpf}'
    
# Criando a Subclass Aluno
class Aluno(Pessoa): 

    def __init__(self, nome, idade, cpf, matricula):
        super().__init__(nome, idade, cpf) # Herda atributos da classe pessoa
        self.matricula = matricula
        self.notas = [] # Lista para armazenar notas do alino



    def adicionar_notas(self, nota, nome):
        self.notas.append(nome,nota)



    def calcular_media(self):
        return sum(self.notas) / len(self.notas)
    

    def exibir_dados(self):
        return f'{super().exibir_dados()} | Matricula: {self.matricula}'
    


class Professor(Pessoa):

    def __init__(self, nome, idade, cpf, salario, materia ):
        super().__init__(nome, idade, cpf)
        self.salario = salario
        self.materia = materia

        def exibir_dados(self):
            return f'{super().exibir_dados()} |  Disciplina: {self.materia} | Salário: R${self.salario:.2f}'
        

aluno1 = Aluno("maria ",12,112312,123123)
professor1 = Professor("Carla ",12,112312,123123.078,6765)

print(aluno1.exibir_dados())
print(professor1.exibir_dados())