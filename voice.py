#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def init(self, client, message):
        self.server = ""

    def joinchannel(client,message):
        voice = await client.join_voice_channel(message.author.voice_channel)

    def leave():
        await self.voice.disconnect()

    def playsong(url):
        player = await voice.create_ytdl_player(url)
        player.start()
