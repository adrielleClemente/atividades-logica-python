#ALGUNS EXERCÍCIOS REALIZADOS NO CURSO MENINAS PROGRAMADORAS DA USP

#Printar nome e sobrenome
nome=input()
sobrenome=input()
print(nome,sobrenome)

#Vamos calcular a idade de alguém?  Seu programa deve ler 2 valores inteiros oferecidos no dispositivo de entrada
#primeira linha: o ano de nascimento de uma pessoa - segunda: o ano para o qual de deseja saber a idade da pessoa
#e informar, como resultado, a idade da pessoa
#Entrada:Duas linhas com um valor inteiro cada
#Saída:A idade calculada
nascimento=int(input('Ano de nacimento: '))
ano_atual=int(input('Digite o ano atual: '))
idade=ano_atual - nascimento
print(idade)


#O dobro
a = int(input())
print(a*2)


#Entrada:Três linhas: números de xícaras da receita; números de colheres de sopa da receita, números de colheres da chá
#da receita.
#Nota: se uma receita não utilizar alguma das medidas, o valor correspondente é dado como 0 (zero).
#uma xícara equivale a 240 ml;uma colher de sopa equivale a 15 ml;uma colher de chá equivale a 5 ml.
#Saída:O volume equivalente em ml para cada uma das porções necessárias à receita.
xicara=int(input())
colherS=int(input())
colherC=int(input())

print(xicara * 240,'ml')
print(colherS * 15,'ml')
print(colherC * 5,'ml')


#Entrada: Duas linhas - a primeira com uma string (nome) e a segunda com um inteiro (idade).
#Saída:Duas linhas: a primeira com a idade diminuída em dois anos, e a segunda com o nome.
nome=str(input())
idade=int(input())
print(idade-2)
print(nome)


#Que problema você tem que resolver>Seu programa deve ler um valor com casas decimais e apresentá-lo com 2, 4, 6, 8 e 10 casas decimais.
#Entrada:Um valor com casas decimais.
n = float(input())
print('%.2f'% n)
print('%.4f'% n)
print('%.6f'% n)
print('%.8f'% n)
print('%.10f'% n)


#Entrada: Duas linhas - cada uma contém um valor inteiro
#Saída:O resultado de sete operações matemáticas: soma, subtração, multiplicação, divisão, módulo, divisão inteira e potência, nessa ordem, entre os dois valores fornecidos. 
#Um valor em cada linha. Quando necessário, considere valores com  duas casas decimais.

x = int(input())
y = int(input())

print(x+y)
print(x-y)
print(x*y)
print('%.2f'%(x/y))
print(x%y)
print(x//y)
print(x**y)


#O que é fornecido como entrada?:Três linhas; a primeira com um valor inteiro, a segundo com o operador desejado, e a terceira com outro valor inteiro não nulo
#O que seu programa deve produzir?-->Uma linha com resultado. Quando necessário, utilize o resultado com uma casa decimal.
a = int(input())
op = str(input())
b = int(input())

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print('%.2f'%(a/b))
elif op == '%':
    print(a%b)
elif op == '//':
    print(a//b)
elif op == '**':
    print(a**b)


#Resolver ax + b = c - Três linhas com os valores inteiros a, b  e c,respectivamente (a != 0).
#Saída:O valor de x com duas casas decimais.
a = int(input())
b = int(input())
c = int(input())

x = (c-b)/a
print('%.2f'% x)


#Qual problema você tem que resolver?:Ler uma idade e, caso ela seja igual ou maior que 60, imprimir a idade seguida de Melhor idade!
#Independentemente da idade lida, o programa deve concluir com a mensagem Fim
idade = int(input())

if idade >= 60:
    print(idade, 'Melhor idade!')
print('Fim')


#O que seu programa deve produzir?-->Duas linhas, a primeira com os dados do primeiro time (nome e pontuação atual), e a segunda com os dados do segundo time.
#Caso nenhuma equipe tenha pontuado ainda, uma terceira linha informa que trata-se do início do jogo
time1=str(input())
time2=str(input())
p1=int(input())
p2=int(input())
    
print(time1,p1)
print(time2,p2)

if p1 + p2 == 0:
    print('início de jogo')