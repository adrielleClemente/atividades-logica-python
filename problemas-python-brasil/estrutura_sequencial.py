#1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Hello world!")

#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = input("Digite um número: ")
print('O número informado foi {}'.format(numero))

#3. Faça um Programa que peça dois números e imprima a soma.
x = float(input("Digite um número: "))
y = float(input("Digite outro número: "))
soma = (x + y)
print('A soma entre os números é: {:.2f}'.format(soma))

#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input('Nota 3: '))
nota4=float(input("Nota 4: "))

notas=[nota1,nota2,nota3,nota4]
soma = sum(notas)
media_bimestral=(soma/4)
print('A média é: {}'.format(media_bimestral))

#5. Faça um Programa que converta metros para centímetros.
metro = float(input('Metros: '))
cm = (metro*100)
print('{0} mt são {1} centímetros'.format(metro,cm))

#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math as pi
raio=float(input("Digite o valor do raio: "))
pi = (pi.pi)
area=((raio**2)*pi)
print('O valor da área do círculo é: {:.2f}'.format(area))

#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre
# o dobro desta área para o usuário.
lado_quadrado = 9
area = lado_quadrado**2
print('O dobro da área do quadrado é:',(area*2))

#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_hora=float(input('Valor da Hora: '))
horas_mes=int(input('Total de horas trabalhadas no mês: '))
total_do_salario=(valor_hora * horas_mes)
print(total_do_salario)

#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e
#mostre a temperatura em graus Celsius. Fórmula: C = 5 * ((F-32) / 9).
fahr = float(input('Quantos Fahrenheit? '))
celsius = 5*((fahr-32)/9)
print(int(celsius), '°C')