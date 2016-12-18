#this contains all of the voice channel commands

import discord
import asyncio

if not discord.opus.is_loaded():
    discord.opus.load_opus('/usr/lib/libopus.so')

class VoiceEntry:
    def __init__(self, message, player):
        self.channel = message.channel
        self.player = player

class VoiceState:
    def __init__(self, bot):
        self.current = None
        self.voice = None
        self.bot = bot
        self.songs = asyncio.Queue()
        self.play_next_song = asyncio.Event()
        self.audio_player = self.bot.loop.create_task(self.audio_player_task())

    def is_playing(self):
        if self.voice is None or self.current is None:
            return False

        player = self.current.player
        return not player.is_done()

    def player(self):
        return self.current.player

    def skip(self):
        if self.is_playing():
            self.player.stop()

    def toggle_next(self):
        self.bot.loop.call_soon_threadsafe(self.play_next_song.set)

    async def audio_player_task(self):
        while True:
            self.play_next_song.clear()
            self.current = await self.songs.get()
            await self.bot.send_message(self.current.channel, 'Now playing ' + str(self.current))
            self.current.player.start()
            await self.play_next_song.wait()


class Music:
    def __init__(self, bot):
        self.bot = bot
        self.voice_state = VoiceState(bot)

    def create_voice_client(self, channel):
        self.voice_state.voice = self.bot.join_voice_channel(channel)

    async def join(self, message):
        join_channel = message.author.voice_channel
        if join_channel is None:
            await self.bot.say('you\'re not in a voice channel!')
            return False

        if self.voice_state.voice is None:
            self.create_voice_client(join_channel)
        else:
            await self.voice_state.voice.move_to(join_channel)

        return True

    async def play(self, song, message):
        if self.voice_state.voice is None:
            await self.bot.say('I need to be in a channel to play a song!')
        try:
            player = await self.voice_state.voice.create_ytdl_player(song, after=self.voice_state.toggle_next)
        except Exception as e:
            fmt = 'An error occurred while processing this request: ```py\n{}: {}\n```'
            await self.bot.say(fmt.format(type(e).__name__, e))
        else:
            entry = VoiceEntry(message, player)
            await self.bot.say('added to queue!')
            await self.voice_state.songs.put(entry)

    async def volume(self, level):
        if self.voice_state.is_playing():
            player = self.voice_state.player
            player.volume = level / 100
            await self.bot.say('Set the volume to {:.0%}'.format(player.volume))

    async def pause(self):
        if self.voice_state.is_playing():
            self.voice_state.player.pause()

    async def resume(self):
        if self.voice_state.is_playing():
            self.voice_state.player.resume()

    async def skip(self):
        self.voice_state.skip()
