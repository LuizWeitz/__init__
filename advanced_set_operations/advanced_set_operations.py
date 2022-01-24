friends = {"Bob", "Michal", "Gustavo"}
travel = {"Bob", "Gustavo"}

#Tirando os amigos que estão viajando do conjuto de amigos
local_friends = friends.difference(travel)

print(local_friends)

#União de dois conjutos

local = {"Marina"}
travel = {"Joaquim", "Anne"}

#União do conjuto local com o conjuto travel
friends = local.union(travel)

print(friends)

#Interseção

math = {"Bob", "Vaitz", "Lucas"}
art = {"Bob", "Miguel", "Vaitz", "Gabriela"}

#Estamos vendo os alunos, os quais estuda as duas matérias
both = art.intersection(math)

print(both)


