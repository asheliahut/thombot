#basic imports
import discord
import asyncio
import re

#any bot resources to import
import commands

#make the client and log in
client = discord.Client()

@client.event
async def on_ready():
    print('logged in as: ')
    print(client.user.name)
    print(client.user.id)
    print('--------')
    await client.change_presence(game=discord.Game(name='Christmas Carols'))

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
        await getattr(commands, input_command.group(0)[1:])(client, message)
    for role_search in message.role_mentions:
        if role_search.name == 'Nickelback':
            await commands.nickelback(client, message)
            break
    if re.search('christmas', message.content):
        if message.author.bot == False:
            await client.send_message(message.channel, 'Merry Christmas!')

client.run('MjIwMzgwOTEzODExMzI0OTI5.CqfjnQ.Zyyg33qyveh6omw1RSlHqDUVXKg')
