from project.song import Song


class Album:
    def __init__(self, name, songs):
        self.name = name
        self.songs = []
        self.attribute_published = False

    def add_song(self, song: Song):
        if song == self.single:
            return
        self.songs.append(song)







    def remove_song(self, song_name: str):
        pass

    def publish(self):
        if self.attribute_published != True:
            return f"Album {self.name} is already published."

        self.attribute_published = True
        return f"Album {self.name} has been published."

    def details(self):
        pass


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
