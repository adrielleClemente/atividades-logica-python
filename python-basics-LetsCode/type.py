#Tipo de dados python

#1.Retorna inteiro
idade = input('Informe sua Idade: ')
idade = int(idade)
print(idade, type(idade))

#2. Retorna string
idade = input('Informe sua idade: ')
print(idade,type(idade))

#3. Exemplos
print(float('123.25'))
print(str(123.25))
print(bool('')) #False
print(bool('abc')) #True
print(bool(0)) #False
print(bool(-2)) #True
print(int('258')) #Apesar de estar entre aspas, está convertido para inteiro
print(int(123.6)) #Por ser inteiro retorna '123'

#4.
