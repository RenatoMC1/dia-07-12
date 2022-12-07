import datetime
class Turma:
    def __init__(self):
        self.turno = "Manhã"
        self.quantidade_de_alunos = 25
        self.horario = datetime.time(9,30,0)

turma01 = Turma()
turma02 = Turma()

print("Turma 01")
print(turma01.turno)
print(turma01.quantidade_de_alunos)
print(turma01.horario)
print("-="*50)
print("Turma 02")
print(turma02.turno)
print(turma02.quantidade_de_alunos)
print(turma02.horario)