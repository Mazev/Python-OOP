from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album}."

    def remove_album(self, album_name: str):
        if album_name not in self.albums:
            return f"Album {album_name} is not found."
        elif Album.publish:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_name)
        return f"Album {album_name} has been removed."

    def details(self):
        band_data = f'Band {self.name}\n'
        for album in self.albums:
            band_data += f'{album.details()}\n'
        return band_data


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())


