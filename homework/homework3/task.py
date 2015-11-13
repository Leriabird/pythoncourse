__author__ = 'Leria'

from random import shuffle
import collections
import itertools
from itertools import groupby
import string

class Song:
    def __init__(self, name, artist, album, albumid, year, time):
        self.name  = name
        self.artist = artist
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

def shuffle_songs(sl):
    shuffle(sl)
    return sl
#___________________________________________________________________________

def frequent_artist(sl):
    artists = [char.artist for char in sl]
    m = max(artists, key=artists.count)
    return m

def longest_song(sl):
    dict = {char.time:(char.name, char.artist) for char in sl}
    times = [int(char.time) for char in sl]
    res = dict[str(max(times))][0] + '    ' + dict[str(max(times))][1]
    return res


# def biggest_album(sl):
#     lst = [char.artist + '    ' + char.album for char in sl]
#     freq = collections.Counter(lst)
#     print(freq)
#     a = freq.most_common(1)
#     print(a[0][0])
    # dict_name_artist_album = {char.name:char.artist + char.album for char in sl}
    # frequency_tuple = collections.Counter(dict_name_artist_album.values()).most_common()
    # print(frequency_tuple)
    # res = frequency_tuple[0][0][0] + '    ' + frequency_tuple[0][0][1]
    # return res

def longest_album(sl):
    dict = {}
    for char in sl:
        if (char.artist, char.album) in dict:
            dict[(char.artist, char.album)] += int(char.time)
        else:
            dict[(char.artist, char.album)] = int(char.time)
    longest = max(dict, key=lambda i: dict[i])
    res = (longest[0] + '    ' + longest[1])
    return res


def ten_words(sl):
    exclude = set(string.punctuation)
    names_lst_p = [char.name for char in sl]
    for i in range(0, (len(names_lst_p)-1)):
        if "'" in names_lst_p[i]:
            names_lst_p[i] = names_lst_p[i].replace("'", " ")
    names_lst = [''.join(ch for ch in char if ch not in exclude) for char in names_lst_p]
    names_string = ' '.join(names_lst)
    words_lst_unreg = names_string.strip().split()
    words_lst = [word.lower() for word in words_lst_unreg]
    counted_words = collections.Counter(words_lst)
    # counted_words = dict((key, len(list(group))) for key, group in groupby(sorted(words_lst)))
    # print(counted_words)
    if len(counted_words) < 10:
        m_common = counted_words.most_common(len(counted_words))
    else:
        m_common = counted_words.most_common(10)
    for char, ch in m_common:
        print(char, end='\t')


def super_productive_artist(sl):
    dict_album_artist = {char.album:char.artist for char in sl}
    frequency_tuple = collections.Counter(dict_album_artist.values()).most_common()
    print(frequency_tuple[0][0])


songs_list = import_songs("songs1.txt")

#export_songs_res = export_songs(songs_list, 'exported_songs.txt')

#shuffle_songs_res = shuffle_songs(songs_list)

print(frequent_artist(songs_list))

print(longest_song(songs_list))

print(longest_album(songs_list))

p = ten_words(songs_list)

print(super_productive_artist(songs_list))


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

#     def __lt__(self, other):
#         if self.artist < other.artist:
#             return True
#         if self.artist == other.artist and self.name < other.name:
#             return True
#         return False

# song1 = Song("Queen", "Bohemian Rhapsody")
# song2 = Song("Metallica", "Die, Die, Die my Darling")

