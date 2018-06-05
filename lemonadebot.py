#Lemonade Bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Bot is ready!")
    await bot.change_presence(game=discord.Game(name="with your emotions")) 
#event triggers for any keywords
@bot.event
async def on_message(message):
#trigger commands
    if message.content.upper() == "ALEX":
        await bot.send_message(message.channel, "Is an Octa-Cosa **Bitch**")

    if message.content.upper() == "SKY":
        await bot.send_message(message.channel, "Kicked someone in the balls")

    if message.content.upper() == "JASON":
        await bot.send_message(message.channel, "Is Paddle Daddy")

    if message.content.upper() == "KEVIN":
        await bot.send_message(message.channel, "Is the pokemon sugar Daddy")

    if message.content.upper() == "PADDLE":
        await bot.send_message(message.channel, "You have been McPaddled By Paddle Daddy")

    if message.content.upper() == "PATRICIA":
        await bot.send_message(message.channel, "Boiling hotdogs the travis g money way since 2017.")
#ping command
    if message.content.upper().startswith('!PING'):
        await bot.send_message(message.channel, "Pong")
#8ball command
    if message.content.upper().startswith('!8BALL'):
        ran1 = random.randint(1,13)
        if ran1 == 1:
            emb1 = discord.Embed(title='8Ball', description='Fuck you, No', colour=0xff0000)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 2:
            emb1 = discord.Embed(title='8Ball', description='Get rEKT, NO!', colour=0xff0000)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 3:
            emb1 = discord.Embed(title='8Ball', description='Hm.. Thats a solid fucking no from me.', colour=0xff0000)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 4:
            emb1 = discord.Embed(title='8Ball', description='"Indeedidly nOPE.', colour=0xff0000)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 5:
            emb1 = discord.Embed(title='8Ball', description='Why are you asking me these questions, I have no clue.', colour=0x0000ff)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 6:
            emb1 = discord.Embed(title='8Ball', description='Im not a fucking psychic, Ask someone else.', colour=0x0000ff)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 7:
            emb1 = discord.Embed(title='8Ball', description='Go ask another person and leave me the fuck alone.', colour=0x0000ff)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 8:
            emb1 = discord.Embed(title='8Ball', description='I honestly have no fucking idea.', colour=0x0000ff)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 9:
            emb1 = discord.Embed(title='8Ball', description='Fuck yes, All the way!', colour=0x00ff00)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 10:
            emb1 = discord.Embed(title='8Ball', description='Thats a solid cucking n- I mean yes.', colour=0x00ff00)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 11:
            emb1 = discord.Embed(title='8Ball', description='Hmm.. Yes.. Now can you leave me alone? Im trying to do nothing.', colour=0x00ff00)
            await bot.send_message(message.channel, embed=emb1)
        if ran1 == 12:
            emb1 = discord.Embed(title='8Ball', description='Yis', colour=0x00ff00)
            await bot.send_message(message.channel, embed=emb1)
#ship command 
    if message.content.upper().startswith('!SHIP'):
        ran2 = random.randint(0,100)
        emb1 = discord.Embed(title='Ship', description='I ship you two '+str(ran2)+'%', colour=0x00ff00)
        await bot.send_message(message.channel, embed=emb1)
#Gay command
    if message.content.upper().startswith('!GAY'):
        ran3 = random.randint(0,100)
        emb1 = discord.Embed(title='Gay Meter', description='The Gay Meter says '+str(ran3)+'%', colour=0x800080)
        await bot.send_message(message.channel, embed=emb1)
#Hate command    
    if message.content.upper().startswith('!HATE'):
        ran4 = random.randint(0,100)
        emb1 = discord.Embed(title='Hatred', description='Id have to say the pure hatred between these two fuckers is about.. '+str(ran4)+'%')
        await bot.send_message(message.channel, embed=emb1)
#Help command
    if message.content.upper().startswith('!HELP'):
        emb1 = discord.Embed(title='Help', Description='commands', colour=0x00ff00)
        emb1.add_field(name='!ship [user1] [user2]', value='Use this command to fucking ship people', inline=False)
        emb1.add_field(name='!hate [user1] [user2]', value='Use this command to calculate pure Hate', inline=False)
        emb1.add_field(name='!gay [user1]', value='Use this command to calculate gayness', inline=False)
        emb1.add_field(name='!8ball [question]', value='This is the 8Ball command, ask it questions', inline=False)
        await bot.send_message(message.channel, embed=emb1)


bot.run("NDUzMzk0NTM4MjA4NDI4MDQz.DfeQGQ.utRGRTjtFxqaLWCqMZSuj7gzpqE")
