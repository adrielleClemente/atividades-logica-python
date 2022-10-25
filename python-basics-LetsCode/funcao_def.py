#Estrutura da função e sua invocação.
def hallo():
    print('Olá,mundo!')
hallo()

#Função com parâmetros. 2 maneiras de passar os parâmetros. E o print dos resultados.
def calculamedia(a,b,c):
    media = (a+b+c)/3
    return media
resultado=calculamedia(5,9,10)
print(resultado)
resultado2=calculamedia(a=6,b=8,c=9)
print(resultado2)

#Função com laço 'for in'.
lista=[1,2,3,4,5,6]
def somalista(lista):
    soma=0
    for i in lista:
        soma=soma+i
    print(soma)
somalista(lista) #21

#Nova lista para usar de parâmetro para a função.)
nova_lista= list(range(1,7))
somalista(nova_lista) #21

#Com 'if'.
def media (a,b,c):
    return (a+b+c)/3
def aprovacao(a,b,c):
    x = media(a,b,c)
    if x >= 6.0:
        print('Aprovade')
    else:
        print('Reprovade')

aprovacao(10,3,10) #Aprovade
aprovacao(6,5,6.5) #Reprovade



#FUNÇÃO COM ARGS E KWARGS

#Função exemplo.
def calcula(a,b,c):
    media=(a+b+c)/3
    return media

#O uso de 'args' é uma convenção, pois pode ser usado outras palavras.
def calcula(*args): #os parâmetros agora é '*args'
    print(args, type(args))
calcula(10,8,9)
#(10, 8, 9) <class 'tuple'>

#Usando sum() e len()
def calcula(*args):
    soma=sum(args) #soma o valor passados dos parâmetros
    media = soma/len(args) #len é o tamanho de args. A média ira dividir a soma pelo tamanho.
    return media
calcula(10,8,9) #9.0

#Novo parâmetro e adicionando ao return.
def calcula(*args,margem):
    soma=sum(args)
    media = soma/len(args)
    return media + margem
calcula(10,8,9,margem=0.4) #9.4

#O '**' transforma em dicionário. Chave e valor.
def info (**kwargs):
    print(kwargs, type(kwargs))

info(nome='Emma', sobrenome='Targaryen')
#{'nome': 'Adrielle', 'sobrenome': 'Karine'} <class 'dict'>