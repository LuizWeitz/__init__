grades = [100, 100, 100, 100, 100]
total = 0

#Calcula o número total de elementos presente na lista
amount = len(grades)


for grade in grades:

    #Adiciona o valor do grade no total
    total += grade

#Imprimos uma média normal
print(total / amount)

#Utilizando a função sum

grades = [100, 100, 100, 100, 100]
total = sum(grades)

#Calcula o número total de elementos presente na lista
amount = len(grades)

print(total / amount)