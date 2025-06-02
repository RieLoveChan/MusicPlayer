from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget

class MusicBeeUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # UI Elements
        self.song_list = QListWidget()
        self.play_button = QPushButton("Play")
        self.download_button = QPushButton("Download")
        self.queue_button = QPushButton("Add to Queue")

        # Add elements to layout
        self.layout.addWidget(self.song_list)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.download_button)
        self.layout.addWidget(self.queue_button)

    def get_selected_song_url(self):
        # Retrieve the selected song URL
        return self.song_list.currentItem().text() if self.song_list.currentItem() else ""
