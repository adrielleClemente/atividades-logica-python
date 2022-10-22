# EXEMPLOS DE COMO USAR RECURSOS PARA STRINGS.

#Caracter de escape para frase que teria aspas simples e duplas.
citacao = " O teórico Pitro N'apollo disse:\"Hoje tem pizza\""
print(citacao) #O teórico Pitro N'apollo disse:"Hoje tem pizza"

#Posição.
empresa = 'Google'
print(empresa[0]) #G

#Posição.
empresa = 'Google'
print(empresa[:3]) #Goo

#
cidade = "cg, rio, brasília, salvador, paris"
cidade = cidade.split(', ')
print(cidade)

# 'strip' remove caracter em branco.
cabecalho = '               menu principal            '
print(cabecalho)
print(cabecalho.strip())

#Estilo do caracter.
mycity = 'cAmPo gRanDE'
print(mycity.title())
print(mycity.capitalize())
print(mycity.lower())
print(mycity.upper())

#Como usar métodos com 'string'.
cidade = input('Que cidade é conhecida como cidade Morena? ')
cidade = cidade.strip()
while cidade.lower()!= 'campo grande':
    print('Tenta de novo')
    cidade = input('Que cidade é conhecida como cidade Morena? ')
print('Booa, você acertou!')

#
mensagem = 'Você viu o que o Pietro disse?'
citado = 'Pietro' in mensagem
nome = 'Cae' in mensagem
print(citado) #True
print(nome) #False

#Multuplicar string
nome = 'Drika '
print(nome*3)

#Print
idade = 27
pets = 3
print(nome + 'tem ' + str(idade)+ ' anos e '+ str(pets) +' pets')

#Método format
print('{} tem {} anos e {} pets'.format(nome,idade,pets))
print(f'{nome} tem {idade} anos e {pets} pets.') #outra sintaxe

#Imprimir duas casas decimais com format
gasolina = 3.476
print('O preço da gasolina está R$ {:.2f}'.format(gasolina)) #3.48



