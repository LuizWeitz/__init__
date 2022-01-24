name = "Luiz"
greeting = "Hi, {}"

#.format vai colocar a variável name dentro das {} no greeting.
with_name = greeting.format(name)

#Também podemos passar o nome direto, reutilizando o template greeting.
with_name_two = greeting.format("Fernando")

print(with_name)
print(with_name_two)

#Benenífio de usar .format() é que podemos ter uma frase grande com mais de um campo.
longer_phrase = "Good Morning {}, today is {}."

with_goodmorning = longer_phrase.format("Fernando", "Saturday")

print(with_goodmorning)