import pylast

class LastFMHandler:
    def __init__(self, api_key, api_secret, username, password_hash):
        self.network = pylast.LastFMNetwork(
            api_key=api_key,
            api_secret=api_secret,
            username=username,
            password_hash=password_hash
        )

    def scrobble_track(self, artist, track, timestamp):
        self.network.scrobble(artist=artist, title=track, timestamp=timestamp)
