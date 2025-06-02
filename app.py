import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import MusicBeeUI
from youtube_handler import YouTubeHandler
from spotify_handler import SpotifyHandler
from twitch_handler import TwitchHandler
from lastfm_handler import LastFMHandler
from ai_agent import AIAgent

class MusicPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = Config()
        self.config.ask_for_variables()  # Ask for variable data at startup

        self.ui = MusicBeeUI(self)
        self.youtube = YouTubeHandler(self.config.get_variable("YouTube Download Path"))
        self.spotify = SpotifyHandler(self.config.get_variable("Spotify Download Path"))
        self.twitch = TwitchHandler(self.config.get_variable("Twitch Token"), 
                                    self.config.get_variable("Twitch Channel"))
        self.lastfm = LastFMHandler(
            self.config.get_variable("Last.fm API Key"),
            self.config.get_variable("Last.fm API Secret"),
            self.config.get_variable("Last.fm Username"),
            self.config.get_variable("Last.fm Password Hash")
        )
        self.ai_agent = AIAgent()

        # Connect UI buttons to respective functionality
        self.ui.play_button.clicked.connect(self.play_song)
        self.ui.download_button.clicked.connect(self.download_song)
        self.ui.queue_button.clicked.connect(self.add_to_queue)

    def play_song(self):
        song_url = self.ui.get_selected_song_url()
        if "youtube.com" in song_url:
            self.youtube.play(song_url)
        elif "spotify.com" in song_url:
            self.spotify.play(song_url)

    def download_song(self):
        song_url = self.ui.get_selected_song_url()
        if "youtube.com" in song_url:
            self.youtube.download(song_url)
        elif "spotify.com" in song_url:
            self.spotify.download(song_url)

    def add_to_queue(self):
        song_url = self.ui.get_selected_song_url()
        self.twitch.queue_song(song_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayerApp()
    window.show()
    sys.exit(app.exec_())
