number_magic = 77

while True:
    play_game = input("Play Game? (Y/n)")

    if play_game == "n":
        break

    number_input = int(input("Enter number:"))
    if number_input == number_magic:
        print("Oh Nice :D, You is amazing")
    elif number_magic - number_input in (1, -1):
        print("You were off by one ")
    else:
        print("OH no :( It's wrong")


