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
        self.player = await self.voice.create_ytdl_player(url)
        await self.player.start()
