name = input("Enter your name: ")

print(name)

size_input = input("How big is your house (in square feet) :")

#Input sempre retorna string, para trabalharmos com número, precisamos converter
square_feet = int(size_input)

square_metres = square_feet / 10.8

print(f"{square_feet} square feet is {square_metres} square metres.")

#Para termos um número mais preciso, exemplo com duas casas decimais
print(f"{square_feet} square feet is {square_metres:.2f} square metres.")

#Obs: caso queremos recer um int direto da pergunta, escrever o seguinte código
size_input = (int(input("How big is yout house (in square feet) :")))


