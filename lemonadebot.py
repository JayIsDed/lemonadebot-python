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



bot.run("NDUzMjA4MTA0NTY2NTIxODU2.DfdPng.3SB1eTXDRviVzyaiPawy0GkbtiU")
