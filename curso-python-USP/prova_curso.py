#PROVA
#1.
idade = int(input())

if idade < 18:
  print(idade,'tenra idade')
if idade >= 60:
  print(idade,'melhor idade')
if idade > 17 and idade <60:
  print(idade,'maioridade')

#2.
notas =int(input())
i = 0
soma = 0
while i < notas:
    valor=int(input())
    soma  = soma + valor
    i += 1
print(soma)

#3.
soma = 0
while True:
    valor = int(input())
    soma = soma + valor
    if valor == 0:
        print(soma)
