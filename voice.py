#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def __init__(self, client):
        self.client = client

    async def joinchannel(self, message):
        try:
            self.voice = await self.client.join_voice_channel(message.author.voice_channel)
        except:
            pass

    async def leave(self):
        try:
            await self.voice.disconnect()
        except:
            pass

    async def playsong(self, url):
        if self.player.is_playing():
            try:
                player.stop()
            except:
                pass
        else:
            try:
                self.player = await self.voice.create_ytdl_player(url)
                self.player.start()
            except:
                pass

    async def pause(self):
        self.player.pause()

    async def resume(self):
        self.player.resume()

    async def volume(self, v_level):
        if v_level < 200:
            self.player.volume = v_level / 100
