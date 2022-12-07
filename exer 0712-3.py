import datetime
class Turma:
    def __init__(self, turno, quantidade_de_alunos, horario):
        self.turno = turno
        self.quantidade_de_alunos = quantidade_de_alunos
        self.horario = horario

turma01 = Turma("Manhã", 25, "9h")
turma02 = Turma("Noite", 20,"19h")

print("Turma 01")
print(turma01.turno)
print(turma01.quantidade_de_alunos)
print(turma01.horario)
print("-="*50)
print("Turma 02")
print(turma02.turno)
print(turma02.quantidade_de_alunos)
print(turma02.horario)