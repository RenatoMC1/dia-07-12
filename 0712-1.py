class Aluno:
    def __init__(self):
        self.matricula = 1234
        self.nome = "Luiz"
        self.notas = 8.5

aluno01 = Aluno()
print(aluno01.matricula)
print(aluno01.nome)
print(aluno01.notas)
print(aluno01.__dict__)