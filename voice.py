#this contains all of the voice channel commands

import discord
import asyncio


class voice:
    def init(self, client, message):
        self.server = ""

    def joinchannel(client,message):
        self.voice = client.join_voice_channel(message.author.voice_channel)

    def leave():
        self.voice.disconnect()

    def playsong(url):
        self.player = voice.create_ytdl_player(url)
        self.player.start()
