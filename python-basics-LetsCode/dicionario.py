#1. Demonstração do type e estrutura.
dado_cidade = {
    'nome':'Campo Grande',
    "estado": 'Ms',
    'area':1900,
    'populacao': 800000
}
print(type(dado_cidade)) #<class 'dict'>
print(dado_cidade) #{'nome': 'Campo Grande', 'estado': 'Ms', 'area': 1900, 'populacao': 800000}

#2. Maneira de adicionar.
dado_cidade['pais'] = 'Brasil'
print(dado_cidade)
#{'nome': 'Campo Grande', 'estado': 'Ms', 'area': 1900, 'populacao': 800000, 'pais': 'Brasil'}

#3. Alterar
dado_cidade['area'] = '1985'
print(dado_cidade)

#4. Copiar e alterar.
dado_cidade2=dado_cidade.copy()
dado_cidade2['pais']='Argentina'
#{'nome': 'Campo Grande', 'estado': 'Ms', 'area': 1900, 'populacao': 800000, 'pais': 'Argentina'}

#5. Upgrade da lista.
novo = {
    'populacao': 600000,
    'fundacao':'21/06/1872',
}
dado_cidade.update(novo)
print(dado_cidade)
#{'nome': 'Dourados', 'estado': 'Ms', 'area': '1985', 'populacao': 600000, 'pais': 'Brasil', 'fundacao': '21/06/1872'}

#6. Método get().
print(dado_cidade.get('prefeito')) #None
print(dado_cidade.get('area')) #1985

#7. Métodos keys(), values(), items().
print(dado_cidade.keys()) #retorna lista de chaves
print(dado_cidade.values()) #retorna lista de valores
print(dado_cidade.items()) #retorna lista de tuplas(chave,valor)
