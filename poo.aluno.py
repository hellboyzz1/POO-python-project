"""15/04/2026"""

class Aluno:
    nome = str
    idade = int
    matricula = int

    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = []

    def adicionar_nota(self, nota):
            self.notas.append(nota)

    def calcular_media(self):
            if len (self.notas) == 0:
                return 0
            return sum(self.notas)/ len(self.notas)

    def verificar_aprovacao(self):
            media = self.calcular_media()
            if media >= 5:
                return "Aprovado"
            else:
                return "Reprovado"

    def apresentar(self):
            print(f"Nome: {self.nome}")
            print(f"Idade: {self.idade}")
            print(f"Matricula: {self.matricula}")
            print(f"Notas: {self.notas}")
            print(f"Media: {self.calcular_media()}")
            print(f"Situação: {self.verificar_aprovacao()}")
