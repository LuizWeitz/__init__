friends = ["Miguel", "Robson", "Vaitz"]

#Verifica se Robson é um elemento da lista friends
print("Robson" in friends)

movies_watched = {"Matrix", "Homem aranha", "Casa gucci"}

user_movie = input("Enter something you've watched recently: ")

print(user_movie in movies_watched)

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too :D")
else:
    print("I add the movie in my wish list")    