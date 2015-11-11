__author__ = 'Leria'

from random import shuffle

class Song:
    def __init__(self, artist, name, album, albumid, year, time):
        self.artist = artist
        self.name = name
        self.album = album
        self.albumid = albumid
        self.year = year
        self.time = time

    def __repr__(self):
        # song = "Song \"%s\" by %s" % (self.name, self.artist)
        song = "Song \"" + self.name + "\" by " + self.artist + self.album + self.albumid + self.year + self.time
        return song

def import_songs(file_name):
    input_file = open(file_name, "r")
    songs_list = []
    for line in input_file:
        line = line.rstrip()
        artist, name, album, albumid, year, time = line.split("\t")
        x = (Song(artist, name, album, albumid, year, time))
        songs_list.append(x)
    return songs_list

def export_songs(songlist, export_filename):
    with open(export_filename, 'w') as export_place:
        for obj in songlist:
            temp_obj = [obj.artist, obj.name, obj.album, obj.albumid, obj.year, obj.time + '\n']
            export_place.write('\t'.join(temp_obj))

# def frequent_artist(sl):
#     artists = [char.artist for char in sl]
#     m = max(artists, key=artists.count)
#     print(m)

# def longest_song(sl):
#     times = [int(char.time) for char in sl]
#     print(max(times))

# def biggest_album(sl):
#     albums_dict = {}
#     for char in sl:
#         if

# ___________no-goddamn-idea-why-this-doesn't-work_____________ [songs.artist for songs.artist in songs]
def shuffle_songs(songs):
    random.shuffle(songs)
    return songs
#_______________________________

#     def __lt__(self, other):
#         if self.artist < other.artist:
#             return True
#         if self.artist == other.artist and self.name < other.name:
#             return True
#         return False

# song1 = Song("Queen", "Bohemian Rhapsody")
# song2 = Song("Metallica", "Die, Die, Die my Darling")

# print(song1 < song2)

songs_list = import_songs("songs1.txt")

export_songs_res = export_songs(songs_list, 'exported_songs.txt')
# __________________________________
shuffle_songs_res = shuffle_songs(songs_list)
#___________________________________

#print(frequent_artist(songs_list))

#print(longest_song(songs_list))





# def filter_songs(songs, word):
#     good_songs = []
#     word = word.lower()
#     for song in songs:
#         if word in song.artist.lower() or word in song.name.lower():
#             good_songs.append(song)
#     return good_songs
#
# for song in sorted(filter_songs(songs, "of")):
#     print(song)