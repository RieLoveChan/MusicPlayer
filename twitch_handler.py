from TwitchIO.ext import commands

class TwitchHandler(commands.Bot):
    def __init__(self, token, channel):
        super().__init__(token=token, prefix="!", initial_channels=[channel])

    async def event_message(self, message):
        if message.content.startswith("!play"):
            song_url = message.content.split(" ")[1]
            # Add song to queue (implementation depends on UI)
            await message.channel.send(f"Added {song_url} to the queue!")
