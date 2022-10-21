#TRABALHANDO COM lISTA.
nome_paises = ['Brasil', 'Argentina','China', 'Canadá','Japão']
print('Tamnhao', len(nome_paises)) #Imprime o tamanho.

print('País', nome_paises[4]) #Imprime o elemento que está na posição[4].

#A posição '-1' de uma lista ou tupla sempre será o último elemento.
print( 'País', nome_paises[-1])

#Maneira de substituir um elemento de uma posição.
nome_paises[4]='Colômbia' #Antes era Japão. Agora é Colômbia.
print(nome_paises[4])
print(nome_paises)

#É possível fazer o fatiamento acessando a posição do index na lista. [início:final:salto]
print(nome_paises[0:]) #Imprime a posição [0] até o que falta na lista.Ou seja, tudo.
print(nome_paises[:-1]) #['Brasil', 'Argentina', 'China', 'Canadá']
print(nome_paises[0:-4]) #['Brasil']
print(nome_paises[:]) #['Brasil', 'Argentina', 'China', 'Canadá', 'Colômbia']
print(nome_paises[::1]) #['Brasil', 'Argentina', 'China', 'Canadá', 'Colômbia']
print(nome_paises[::2]) #['Brasil', 'China', 'Colômbia']
#Assim inverte os elementos da lista.
print(nome_paises[::-1]) #['Colômbia', 'Canadá', 'China', 'Argentina', 'Brasil']

#Procura na lista a string 'Brasil' e retorna um valor booleano.
print('Brasil' in nome_paises)

#Coloca elementos na lista.
capitais = []
capitais.append('CG')
capitais.append('PoA')
capitais.append('SP')
capitais.append('RJ')
capitais.append('Salvador')
print(capitais)

#Insere na lista em posicção indicada.
capitais.insert(2,'Paris')
print(capitais)

#Remover da lista.
capitais.remove('SP')
print(capitais)


#TRABALHANDO COM TUPLAS.
#A diferença é a flexibilidade, não é possível realizar alteração do valor dentro dela.

#Sintaxe da tupla.
paises=('Brasil','Argentina','China','Japão')
print(paises,type(paises)) #('Brasil', 'Argentina', 'China', 'Japão') <class 'tuple'>
estado='Ms',
print(estado,type(estado)) #('Ms',) <class 'tuple'>

#unpack da tupla
a,b,c,d = paises
print(a,b,d) # Brasil Argentina Japão



