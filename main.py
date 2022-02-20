import time
import webbrowser

print ("LyricArch by JavaPlanes v.0.1: Just An Idea")
time.sleep(2)
print("Not associated with MusixMatch, all rights of lyrics to them.")
time.sleep(1)
print("")
songName = raw_input("Hello! What song would you want lyrics for today? (Song name only, and if the song has 2+ words, please add a '-' between each word!) ")
time.sleep(1)
songArtist = raw_input("Who made this song? (If they have 2+ words in their name, please add a '-' between each word!) ")
webbrowser.open("https://www.musixmatch.com/lyrics/" + songArtist + "/" + songName + "/")