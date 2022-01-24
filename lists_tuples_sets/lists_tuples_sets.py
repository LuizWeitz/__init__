#List, é um conjuto de elementos, como o próprio nome diz, Lista, pode ser removidos e adicionado elementos
list = ["Luiz", "Miguel", "Nicholas", "Lucas"]

#Tuple, é parecido com uma lista, só que é formatado em () e seus elementos não podem ser removidos ou adicionados
tuple = ("Maria", "Lara", "Gustavo")

#Uma tuple, com um elemento somente
tuple_single_value = 15,

#Conjuto, pode remover e adicionar elementos, mas nenhum elemento pode ser duplicado
#Obs: quando imprimido, não segue as ordens dos elementos, é aleatório
set = {"Bob", "Fernando", "Joaquina"}

#Imprimindo a posição 1 da list, lembrando uma lista inicia com a posição 0
print(list[1])

#Alterado a posição 2 da list
list[2] = "Gustavo"

print(list)

#Adicionando um elemento ao final de uma lista
list.append("Smith")

print(list)

#Remoção de um elemento da lista
list.remove("Miguel")
print(list)

#Acionando um elemento no set
set.add("João")
print(set)

