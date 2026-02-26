notas = []

while True:

    try:
        for i in range(3):
            nota = float(input('Quais as notas: '))
            notas.append(nota)
        break
    except:
        print("Nota invalida.")

def ler():
    ler = len(notas)
    print('Número de notas: ',ler)

def soma():
    soma = sum(notas)
    print('A soma das notas é: ',soma)

def media():
    media = sum(notas) / len(notas)
    print('A média é: ',media)

print(notas)
ler()
soma()
media()

print("")
print(f"{' BOLETIM ':=^30}")
print("")

media()

media = sum(notas) / len(notas)

if media >= 6:
    print(f"Status: \033[32mAPROVADO\033[m")

else:
    print(f"Status: \033[31mREPROVADO\033[m")