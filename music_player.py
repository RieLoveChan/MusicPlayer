import os
import pygame
import configparser

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.config_file = 'music_player.ini'
        self.config = configparser.ConfigParser()
        self.music_dir = "."
        self.volume = 0.8
        self.load_config()

        pygame.mixer.music.set_volume(self.volume)
        self.music_files = self._scan_for_music()
        self.current_track = 0
        self.playing = False
        self.paused = False

    def _scan_for_music(self):
        """Scans the music directory for .mp3 files."""
        files = []
        for filename in os.listdir(self.music_dir):
            if filename.endswith(".mp3"):
                files.append(os.path.join(self.music_dir, filename))
        return files

    def display_playlist(self):
        """Displays the list of available tracks."""
        print("\n--- Playlist ---")
        if not self.music_files:
            print("No music files found in the current directory.")
            return
        for i, track in enumerate(self.music_files):
            print(f"{i + 1}. {os.path.basename(track)}")
        print("----------------\n")

    def play(self, track_number=None):
        """Plays a track from the playlist."""
        if not self.music_files:
            print("No music files to play.")
            return

        if track_number is not None:
            self.current_track = track_number - 1

        if 0 <= self.current_track < len(self.music_files):
            track_to_play = self.music_files[self.current_track]
            try:
                pygame.mixer.music.load(track_to_play)
                pygame.mixer.music.play()
                self.playing = True
                self.paused = False
                print(f"Now playing: {os.path.basename(track_to_play)}")
            except pygame.error as e:
                print(f"Error playing track: {e}")
        else:
            print("Invalid track number.")

    def stop(self):
        """Stops the music."""
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        print("Music stopped.")

    def pause(self):
        """Pauses or unpauses the music."""
        if self.playing:
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
                print("Resumed music.")
            else:
                pygame.mixer.music.pause()
                self.paused = True
                print("Paused music.")

    def next_track(self):
        """Plays the next track in the playlist."""
        if self.music_files:
            self.current_track = (self.current_track + 1) % len(self.music_files)
            self.play(self.current_track + 1)

    def prev_track(self):
        """Plays the previous track in the playlist."""
        if self.music_files:
            self.current_track = (self.current_track - 1) % len(self.music_files)
            self.play(self.current_track + 1)

    def set_volume(self, level):
        """Sets the volume (0.0 to 1.0)."""
        if 0.0 <= level <= 1.0:
            self.volume = level
            pygame.mixer.music.set_volume(self.volume)
            print(f"Volume set to {int(self.volume * 100)}%")
        else:
            print("Volume must be between 0.0 and 1.0.")

    def run(self):
        """Main loop for the music player."""
        print("Welcome to the Music Player!")
        self.display_playlist()

        while True:
            command_str = input("Enter a command (play [num], stop, pause, next, prev, vol [0-100], list, quit): ").strip().lower()
            parts = command_str.split()
            command = parts[0]

            if command == "quit":
                break
            elif command == "play":
                if len(parts) > 1 and parts[1].isdigit():
                    self.play(int(parts[1]))
                else:
                    self.play()
            elif command == "stop":
                self.stop()
            elif command == "pause":
                self.pause()
            elif command == "next":
                self.next_track()
            elif command == "prev":
                self.prev_track()
            elif command == "vol":
                if len(parts) > 1 and parts[1].isdigit():
                    self.set_volume(int(parts[1]) / 100.0)
                else:
                    print(f"Current volume: {int(self.volume * 100)}%")
            elif command == "list":
                self.display_playlist()
            else:
                print(f"Unknown command: {command}")

        self.save_config()

    def load_config(self):
        """Loads configuration from the .ini file."""
        if not os.path.exists(self.config_file):
            self.save_config()  # Create a default config if it doesn't exist
            return

        self.config.read(self.config_file)
        if 'Settings' in self.config:
            self.music_dir = self.config['Settings'].get('MusicDirectory', '.')
            self.volume = self.config['Settings'].getfloat('Volume', 0.8)

    def save_config(self):
        """Saves configuration to the .ini file."""
        self.config['Settings'] = {
            'MusicDirectory': self.music_dir,
            'Volume': str(self.volume)
        }
        with open(self.config_file, 'w') as configfile:
            self.config.write(configfile)
        print("Configuration saved.")


if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
