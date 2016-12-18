async def joinchannel(client,message):
    try:
        voice = await client.join_voice_channel(message.content[15:])
        return voice
    except:
        if message.author.voice.voice_channel != None:
            voice = await client.join_voice_channel(message.author.voice.voice_channel)
            return voice
        else:
            await client.send_message(message.channel, 'PLease either join a chnanel or specify a channel for me to join!')

async def leavechannel(client,message,voice):
    await voice.disconnect()

async def playsong(client,message,voice,):
    song_to_play = message.content[13:]
    try:
        player = await voice.create_ytdl_player(song_to_play)
        player.start()
    except:
        await client.send_message(message.channel, 'something went wrong!\nMake sure you gave me a valid youtube video to play!')



if message.content.startswith('!v '):
    voice_channel_service = None
    if message.content.startswith('!v joinchannel'):
        voice_channel_service = await voice.joinchannel(client,message)
    else:
        await getattr(voice, input_command.group(0)[2:])(client, message_channel_service, voice_channel_service)
    if message.content.startswith('!v leavechannel'):
        voice_channel_service = None

class voice:
    def __init__(self, client):
        self.client = client
        self.channel = ""
        self.v_level = 0.2
        self.playlist = asyncio.Queue()
        self.
        self.music_channel = client.get_channel("253409501716283402")

    async def joinchannel(self, message):
        if hasattr(self, 'voice'):
            if self.voice.is_connected():
                self.channel = message.author.voice_channel
                await self.voice.move_to(self.channel)
            else:
                self.channel = message.author.voice_channel
                self.voice = await self.client.join_voice_channel(self.channel)
        else:
            self.channel = message.author.voice_channel
            self.voice = await self.client.join_voice_channel(self.channel)

    async def leave(self):
        try:
            await self.voice.disconnect()
        except:
            pass

    async def playsong(self, url):
        if hasattr(self, 'player'):
            if self.player.is_playing():
                self.playlist.append(url)
                await self.client.send_message(self.music_channel, 'Added song to playlist!')
            else:
                self.player.stop()
                self.player = await self.voice.create_ytdl_player(url, after = self.aftersong())
                self.player.start()
                self.player.volume = self.v_level
        else:
            try:
                self.player = await self.voice.create_ytdl_player(url, after = self.aftersong())
                self.player.start()
                self.player.volume = self.v_level
            except:
                pass

    async def skip(self):
        if hasattr(self, 'player'):
            if self.player.is_playing():
                if self.playlist == []:
                    await self.client.send_message(self.music_channel, 'the playlist is empty!')
                else:
                    self.player.stop()
                    self.player = await self.voice.create_ytdl_player(self.playlist.pop(), after = self.aftersong())
                    self.player.start()
            else:
                await self.client.send_message(self.music_channel, 'not playing anything!')
        else:
            await self.client.send_message(self.music_channel, 'not playing anything!')

    def aftersong(self):
        if self.playlist == []:
            #await client.send_message(self.music_channel, "the playlist is empty!")
            pass
        else:
            self.player.stop()
            self.player = self.voice.create_ytdl_player(self.playlist.pop(), after = self.aftersong())
            self.player.start()

    def pause(self):
        self.player.pause()

    def resume(self):
        self.player.resume()

    def volume(self, v_input):
        self.v_level = v_input / 100
        self.player.volume = self.v_level
