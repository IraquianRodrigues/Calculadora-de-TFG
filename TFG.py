print('LABORATÓRIO DE ANÁLISES CLINÍCAS')
print('Biomédica Responsavél , Dr. Larissa Oliveira')


print('-'*20)
print('calculando o TFG')
print('-'*20)

idade = int(input('digite a idade do paciente: '))
peso = float(input('digite o peso do paciente: '))
numerofixo = 72

print()

calculo = (140-idade) * peso
print(f'O resutado do calculo foi: {calculo}')
print()

creatinina = float(input('resultado da creatinina: '))


print()

resultado_creatinina = numerofixo * creatinina
print(f'O resultado do calculo da creatinina sérica foi de: {resultado_creatinina:.1f}')
print()


import time
import sys
print("Calculando os Dados, Aguarde...")
#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()


print()


resultadofinal = calculo / resultado_creatinina
print()
print(f'* O resultado final foi de: {resultadofinal:.1f} mL/MIN/1,73m² *')
print()

if resultadofinal >=90:
    print('|Lesão renal com filtração glomerular normal|')

elif resultadofinal >= 60 and resultadofinal <= 89:
    print('|Lesão renal com insuficiência renal leve|')

elif resultadofinal >= 30 and resultadofinal <= 59:
    print('|Insuficiência renal moderada|')

elif resultadofinal >= 15 and resultadofinal <= 29:
    print('|Insuficiência renal avançada|')

else:
    print('|Insuficiência renal Crônica terminal:|')

print()
print('-'*25)
print('VALORES DE REFERENCIAS')
print('-'*25)
print()
print('GRAU1: Lesão renal com filtração normal: > 90 ')
print('GRAU2: Lesão renal com insuficência renal leve: 60-89 ')
print('GRAU3: Insuficiência renal moderada: 30-59')
print('GRAU4: Insuficiência renal avançada: 15-29')
print('GRAU5: Insuficiência renal crônica terminal: < 15 ou dialíse')



