class DevPlaylist:
    max_songs = 50

    def __init__(self, name, songs=None):
        self.name = name

        if songs is None:
            self.songs = []
        else:
            self.songs = songs[:]

    def add_song(self, title):
        if len(self.songs) >= DevPlaylist.max_songs:
            return "Playlist is full"

        self.songs.append(title)
        return f"Added: {title}"

    def remove_song(self, title):
        if title not in self.songs:
            return False

        self.songs.remove(title)
        return True

    def get_songs_by_prefix(self, prefix):
        prefix = prefix.lower()
        return [song for song in self.songs if song.lower().startswith(prefix)]

    def __repr__(self):
        sorted_songs = sorted(self.songs)
        songs_str = ", ".join(sorted_songs)

        return f"DevPlaylist {self.name} (songs: {len(self.songs)}): {songs_str}"