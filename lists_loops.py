#Q1
songs =["ROCKSTAR", "Do It", "For the Night"]

print(songs[1])

#Q2
print(songs[0:3])

print(songs[1:3])

#Q3
songs[0] = "Dynamite"
print(songs)

songs[2] = "Everything I Wanted"
print(songs)

#Q4
songs.append("Roman Holiday")

songs.extend(["Do What I Want"])

songs.insert(3, "3:15")

print(songs)

songs.pop(0)
del songs[1]
print(songs)

#Q5
for song in songs:
    print(song)
#Option 1, prints out the whole list, as is.

for i in range(len(songs)):
    print(songs[i])
#Option 2, prints out a range within the list of songs. Eg: it's possible to print out the third and fourth songs, specificially.

