#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def __init__(self, client):
        self.client = client
        self.v_level = 0.2

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
        if hasattr(self, 'player'):
            try:
                self.player.stop()
            except:
                pass
            try:
                self.player = await self.voice.create_ytdl_player(url)
                self.player.start()
                self.player.volume = self.v_level
            except:
                pass
        else:
            try:
                self.player = await self.voice.create_ytdl_player(url)
                self.player.start()
                self.player.volume = self.v_level
            except:
                pass

    async def stop(self):
        self.player.stop()

    async def pause(self):
        self.player.pause()

    async def resume(self):
        self.player.resume()

    async def volume(self, v_input):
        self.v_level = v_input / 100
        self.player.volume = self.v_level
