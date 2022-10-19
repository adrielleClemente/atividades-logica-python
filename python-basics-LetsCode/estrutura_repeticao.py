#1. Impressão da primeira posição de cada item da lista.
paises = ['Brasil','Argentina','Holanda','Japão','Espanha']
for i in paises:
    print(i[0])

#2. Impressão de cada item da lista usando 'for in'.
paises = ['Brasil','Argentina','Holanda','Japão','Espanha']
for i in paises:
    print(i)

#3. Impressão de item da lista 'paises'.
paises = ['Brasil','Argentina','Holanda','Japão','Espanha']
print(paises[0])

#4. Listagem de 'paises' com 'while'.
contador = 0
paises = ['Brasil','Argentina','Holanda','Japão','Espanha']
while contador < len(paises): #Enquanto o valor de 'contador' for menor que o tamanho de 'paises'.
    print(paises) #irá printar o conteúdo de 'paises'.
    contador+=1

#5. Impressão de tupla usando 'for in'.
paises ='Brasil','Argentina','Holanda','Japão','Espanha'
for i in paises:
    print(i)

#6. Criação de dicionário. Print tipo string.
dados = {
    'Cidade':'Campo Grande',
    'Estado':'Mato Grosso do Sul',
    'Populacao':800000
}
for chave in dados:
    print(f'{chave}:{dados[chave]}') #print da chave e seguida busca dentro do dicionário o valor da chave.

#7. O 'range' recupera o tamanho (len) da lista e printa o valor do index 'i'.
dados = {
    'Cidade':'Campo Grande',
    'Estado':'Mato Grosso do Sul',
    'Populacao':800000
}
for i in range(len(dados)):
    print(i) 

#8. Print do tamanho da tupla.
paises ='Brasil','Argentina','Holanda','Japão','Espanha'
for i in range(len(paises)):
    print(i)

#9. Recuperação da lista com 'range' e atribuição de valor para posição.
paises =['Brasil','Argentina','Holanda','Japão','Espanha']
for i in range(len(paises)): #Recupera o tamanho da lista 'paises'.
    paises[i]='Bogotá' #Reatibui o valor a cada index da lista.
print(paises)