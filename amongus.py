from discord.ext.commands import Bot
from discord.ext.commands import *
import discord
BOTPREFIX = ("++")
token = 'your token here'
client = Bot(command_prefix=BOTPREFIX, case_insensitive=True)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')    

@client.command(name = "s")
async def deceit(ctx):
    memberr = ctx.author
    for channel in ctx.guild.voice_channels:
        members = channel.members
        if ctx.author in members:
            for member in members:
                await member.edit(mute=True)
            await ctx.send('all users in ur channel have been muted')

@client.command(name = "e")
async def mutee(ctx):
    k = 0
    memberr = ctx.author
    for channel in ctx.guild.voice_channels:
        members = channel.members
        if ctx.author in members:
            for member in members:
                await member.edit(mute=False)
            await ctx.send('Users are unmuted')

@client.command(name = "troll")
async def marmad(ctx, arg1):
    memberr = ctx.author
    if ctx.author.display_name not in banned:
        for channel in ctx.guild.voice_channels:
            members = channel.members
            for member in members:
                if member.display_name == arg1:
                    for channel2 in ctx.guild.voice_channels:
                        if channel2 != channel:
                            await member.move_to(channel2)
                    await member.move_to(channel)
                    break                    

@client.command(name = "user")
async def users(ctx):
    for channel in ctx.guild.voice_channels:
        members = channel.members
        for member in members:
            await ctx.send(member.display_name)

@client.event
async def on_raw_reaction_add(payload):
    msgID = payload.message_id
    print(payload.message_id)
    print(payload.channel_id)
    #change the msgID and the channel_ID to the proper ids
    if msgID==757620278380593324 and payload.channel_id==757597587346948218:
        memberr = payload.member
        for channel in client.guilds[0].voice_channels:
            members = channel.members
            if memberr in members:
                for member in members:
                    await member.edit(mute=True)

@client.event
async def on_raw_reaction_remove(payload):
    msgID = payload.message_id
    userID = payload.user_id
    print(payload.message_id)
    print(payload.channel_id)
    #change the msgID and the channel_ID to the proper ids
    if msgID==757620278380593324 and payload.channel_id==757597587346948218:
        for channel in client.guilds[0].voice_channels:
            members = channel.members
            ids = []
            for t in range (len(members)):
                ids.append(members[t].id)
            if userID in ids:
                for member in members:
                    await member.edit(mute=False)
client.run(token)
