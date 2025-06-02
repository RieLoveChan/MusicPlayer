# MusicPlayer

**MusicPlayer** is a feature-rich and customizable application designed for music enthusiasts, streamers, and developers. It integrates seamlessly with popular platforms like Twitch, YouTube, Spotify, and Last.fm, allowing you to enjoy and manage your music with ease.

## 🚀 Features

- **Customizable Music Player**: Play and manage songs with a sleek interface inspired by MusicBee.
- **Song Library**: Organize your favorite tracks and playlists efficiently.
- **YouTube Offline Caching**: Download songs from YouTube for offline playback.
- **Spotify Integration**: Stream and cache songs from Spotify.
- **Twitch Integration**: Allow viewers to request songs during live streams.
- **Last.fm Integration**: Scrobble tracks to Last.fm for tracking your listening habits.
- **AI-Powered Playlist Generator**: Get personalized recommendations based on your mood or preferences.
- **Dynamic Configuration**: Easily update API keys, paths, and other settings within the app.

## 📦 Installation

### Prerequisites
- Python 3.8+
- Required Libraries:
  ```bash
  pip install PyQt5 youtube-dl spotipy TwitchIO pylast openai ffmpeg-python
  ```

### Clone the Repository
```bash
git clone https://github.com/RieLoveChan/MusicPlayer.git
cd MusicPlayer
```

### Run the Application
```bash
python app.py
```

## 🛠 Configuration

The app dynamically asks for configuration variables like API keys, download paths, and Twitch details upon startup. You can modify these settings later through the configuration module.

## 🎮 Twitch Integration

Enable your viewers to request songs during live streams:
1. Add your Twitch token and channel name in the configuration.
2. Start streaming, and let viewers request songs using `!play <song_url>`.

## 🎵 Last.fm Integration

Track your listening habits by connecting your Last.fm account:
1. Provide your Last.fm API Key, API Secret, username, and password hash.
2. The app will automatically scrobble tracks as you play them.

## 🌟 AI Playlist Generator

Generate personalized playlists:
1. Enter your preferences or mood in the app.
2. The AI agent will recommend songs or create a themed playlist.

## 🤝 Contributing

We welcome contributions to improve MusicPlayer! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with detailed information about your changes.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 💬 Feedback and Support

For any issues or suggestions, feel free to open an [issue](https://github.com/RieLoveChan/MusicPlayer/issues) or contact us directly.

---

Feel free to modify this template to suit your repository's needs. Let me know if you'd like help adding more details or refining the structure!
