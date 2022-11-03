#Arquivos simples podem ser lidos com o modo de letitura 'r'
#Por segurança todo aquivo aberto precisa ser fechado referenciando a variável do arquivo .close()
arquivo = open('Desktop/exemplo.txt','r')
texto = arquivo.read()
print(texto)
arquivo.close()

#Desta maneira o resultado é omesmo, pois utilizando o 'while', o cursor passou de linha em linha.
arquivo = open('Desktop/exemplo.txt','r')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

#Mesmo resultado usando 'for in'.
arquivo = open('Desktop/exemplo.txt','r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

#Com 'with' não precisa fechar com o .close, pois o arquivo é lido e fechado.
with open('Desktop/exemplo.txt','r') as arquivo:
    texto = arquivo.read()
    print(texto)

#Caso queira lê o mesmo arquivo.
arquivo.read() #Erro de arquio fechado.

#O 'w' para escrever no arquivo.
with open('Desktop/exemplo.txt','w') as arquivo:
    arquivo.write('Linha escrita em python\n')
    arquivo.write('Segunda linha escrita em python\n')

#O print da escrita/modificação.
with open('Desktop/exemplo.txt','r') as arquivo:
    print(arquivo.read())
#Linha escrita em python
#Segunda linha escrita em python

#Já o 'a' usa-se para adicionar.
with open('Desktop/exemplo.txt','a') as arquivo:
    arquivo.write('Linha adicionada em python\n')
#Linha escrita em python
#Segunda linha escrita em python
#Linha adicionada em python



