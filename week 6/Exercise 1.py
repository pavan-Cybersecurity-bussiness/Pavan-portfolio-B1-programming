#Create Empty Data Structures
songs = []
genre_count = {}
for i in range(5):
    Song_name = str(input("Song name : "))
    Genre = str(input(" Genre : "))
    song = (Song_name , Genre )
    songs.append(song)
    if Genre in genre_count :
        genre_count[Genre] +=1
    else:
        genre_count[Genre] = 1
print("=== YOUR MUSIC LIBRARY ===")
for song, genre in songs :
    print(song,"(",genre , ")")
print("=== GENRE STATISTICS ===")
for genre,count in genre_count.items() :
    print(genre,":",count,"song(S)")
