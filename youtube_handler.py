import youtube_dl

class YouTubeHandler:
    def __init__(self, download_path):
        self.download_path = download_path

    def play(self, url):
        print(f"Playing YouTube song: {url}")
        # Use ffplay or other tools for playback

    def download(self, url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.download_path}/%(title)s.%(ext)s',
            'noplaylist': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
