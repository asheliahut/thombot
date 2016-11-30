#basic imports
import discord
import asyncio
import re

#any bot resources to import
import commands
import voice

#make the client and log in
client = discord.Client()

if not discord.opus.is_loaded():
    discord.opus.load_opus('/usr/lib/libopus.so')

@client.event
async def on_ready():
    print('logged in as: ')
    print(client.user.name)
    print(client.user.id)
    print('--------')
    await client.change_presence(game=discord.Game(name='with dreidels'))

#welcome new members to the server
@client.event
async def on_member_join(member):
     for channel in member.server.channels:
        if channel.id == '85228383054594048':
            await asyncio.sleep(3)
            await client.send_message(channel,'{} welcome {} to the server!'.format(member.roles[0].mention, member.mention))

#takes care of all the commands sent using messages
@client.event
async def on_message(message):
    if message.content.startswith('!'):
        input_command = re.match(r"!(\w+)", message.content)
        try:
            await getattr(commands, input_command.group(0)[1:])(client, message)
        except:
            pass
    if message.content.startswith('!v '):
        if message.content.startswith('!v joinchannel'):
            voice_channel = voice.voice(client, message)
            await voice_channel.joinchannel()
        if message.content.startswith('!v leave'):
            voice_channel.leave()
        if message.content.startswith('!v playsong'):
            song_to_play = message.content[13:]
            voice_channel.playsong(song_to_play)
    for role_search in message.role_mentions:
        if role_search.name == 'Nickelback':
            await commands.nickelback(client, message)
    if re.search(r'[Cc]hristmas', message.content):
        if message.author.bot == False:
            await client.send_message(message.channel, 'Merry Christmas, {}!'.format(message.author.mention))
    for mention_search in message.mentions:
        if mention_search.name == 'Christmas Bird':
            if message.author.bot == False:
                await client.send_message(message.channel, 'Merry Christmas, ' + mention_search.mention + '!')


client.run('MjQwOTMyNTAwNzI4MzE1OTA0.CvKq3Q.Rk_7Pllbu3humowD4uYp0gxJ7rM')
