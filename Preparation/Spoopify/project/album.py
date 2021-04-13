from project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.songs = [song for song in args]
        self.published = False

    def add_song(self, song):
        if self.published == True:
            return f'Cannot add songs. Album is published.'
        if song.single == True:
            return f'Cannot add {song.name}. It\'s a single'
        if song not in self.songs:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'
        else:
            return f'Song is already in the album.'

    def remove_song(self, song_name: str):
        filter_song = [s for s in self.songs if s == song_name]
        if song_name not in self.name:
            return "Song is not in the album."
        elif not self.published:
            return "Cannot remove songs. Album is published."

        self.songs.remuve(song_name)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published is not self.published:
            self.published = False
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_data = f'Album {self.name}\n'
        for song in self.songs:
            album_data += f'== {song.get_info()}\n'
        return album_data
