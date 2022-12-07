
def criarLista(elemento):
    lista = []
    for i in range(elemento+1):
        lista.append(i)
    return lista

numero = int(input("Informe o  número: "))
lista_nova = criarLista(numero)
print(lista_nova)

def quadrado(lista):
    quadrados = []
    for i in lista:
        quadrados.append(i**2)
    print(quadrados)

quadrado(lista_nova)