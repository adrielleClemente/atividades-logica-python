#Importar biblioteca
import csv

#SOBRE: abre o arquivo 'csv', informa o objetivo('r'), cria uma variável (leitor)
#informa a biblioteca importada(csv) e função .reader(),
#assim, navegar por cada linha por laço 'For' e imprimir a variável criada 'linha'.
#imprime-se em forma de Lista.
with open('exemplo.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

#Exemplo com if.
with open('exemplo.csv','r') as arquivo:
    leitor = csv.reader(arquivo)
    header = next(leitor)#Pula o cabeçalho, pois a leitura começa na 1° linha.
    for linha in leitor:
        if linha[0]=='texto dentro do exemplo':
            print(linha)

#Abrir arquivo sem biblioteca.
with open('exemplo.csv','r') as file:
    linhas = file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha=linha.split(',')
        print(linha)

#Criar um arquivo csv. O python fez quebra de linha com esse código.
import csv
with open('userscv','w') as arquivousers:
    escritor = csv.writer(arquivousers)
    escritor.writerow(['nome','sobrenome','idade','genero'])
    escritor.writerow(['Adrielle','Karine','27','Feminino'])

#Para não ter quebra de linha uso -> newline=''
with open('userscv','w',newline='') as arquivousers:
    escritor = csv.writer(arquivousers)
    escritor.writerow(['nome','sobrenome','idade','genero'])
    escritor.writerow(['Adrielle','Karine','27','Femenino'])


########################################################################################

# Programa que recebe informações e tranforma em um arquivo csv.
header = ['Nome', 'Sobrenome']
dados=[]
opc = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opc !='0':
    nome = input("Qual seu nome?")
    sobrenome = input ('Qual seu sobrenome?')
    dados.append([nome,sobrenome])#dentro da lista dados é adicionado os valores de nome e sobrenome
    opc = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

print(dados) 

with open('userscv.csv','w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerow(dados)
with open('userscv.csv','r') as file_leitura: #leitura do arquivo
    csv_leitor=csv.reader(file_leitura, delimiter=',')
    for row in csv_leitor:
        print(row)

#O que deseja fazer?
# 1 - Cadastrar      
# 0 - Sair
# 1
# Qual seu nome?Adrielle
# Qual seu sobrenome?Clemente
# O que deseja fazer?
# 1 - Cadastrar      
# 0 - Sair
# 0
# [['Adrielle', 'Clemente']]
# ['Nome', 'Sobrenome']
# ["['Adrielle', 'Clemente']"]