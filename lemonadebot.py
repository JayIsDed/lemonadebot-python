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
            await bot.send_message(message.channel, "Fuck you, No.")
        if ran1 == 2:
            await bot.send_message(message.channel, "Get rEKT, NO.")
        if ran1 == 3:
            await bot.send_message(message.channel, "Hm.. That's a solid fucking no from me.")
        if ran1 == 4:
            await bot.send_message(message.channel, "Indeedidly nOPE.")
        if ran1 == 5:
            await bot.send_message(message.channel, "Why are you asking me these questions, I have no clue.")
        if ran1 == 6:
            await bot.send_message(message.channel, "Im not a fucking psychic, Ask someone else.")
        if ran1 == 7:
            await bot.send_message(message.channel, "Go ask another person and leave me the fuck alone.")
        if ran1 == 8:
            await bot.send_message(message.channel, "I honestly have no fucking idea.")
        if ran1 == 9:
            await bot.send_message(message.channel, "Fuck yes, All the way!")
        if ran1 == 10:
            await bot.send_message(message.channel, "That's a solid cucking n- I mean yes.")
        if ran1 == 11:
            await bot.send_message(message.channel, "Hmm.. Yes.. Now can you leave me alone? I'm trying to do nothing.")
        if ran1 == 12:
            await bot.send_message(message.channel, "Yis")
#ship command 
    if message.content.upper().startswith('!SHIP'):
        ran2 = random.randint(0,100)
        emb1 = discord.Embed(title='Ship', description='I ship you two '+str(ran2)+'%', colour=0x00ff00)
        await bot.send_message(message.channel, embed=emb1)



bot.run("NDUzMjA4MTA0NTY2NTIxODU2.DfdPng.3SB1eTXDRviVzyaiPawy0GkbtiU")
