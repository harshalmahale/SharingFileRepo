user = {}
name, age, fav_movie, fav_songs = input ("Enter the name : age : fav_movie :fav_songs").split(",")
print(f"Name is {name} & Age is {age}" )  
print(f"Fav movie is {fav_movie} Fav song is {fav_songs}")

user['name'] = name
user['age'] = age
user['fav_movie'] = fav_movie
user['fav_song'] = fav_songs

for key,value in user.items():
    print(f"{key} : {value}")