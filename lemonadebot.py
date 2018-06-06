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
#event triggers for any keywords
@bot.event
async def on_message(message):
#trigger commands
    if message.content.upper() == "ALEX":
        emb1 = discord.Embed(title='Alex Can not FUCKING boil hotDOGS', colour=0xF37373)
        await bot.send_message(message.channel, embed=emb1)

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

    if message.content.upper() == "JOE":
        await bot.send_message(message.channel, "Is taken by Gigi")

    if message.content.upper() == "GIGI":
        await bot.send_message(message.channel, "Is taken by Joe")

    if message.content.upper() == "JACOB":
        await bot.send_message(message.channel, "Is Jewish")
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
            emb1 = discord.Embed(title='8Ball', description='Indeedidly nOPE.', colour=0xff0000)
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
        await bot.send_message(message.author, embed=emb1)
#Trigger command
    if message.content.upper().startswith('!TRIGGER'):
        emb1 = discord.Embed(title='Triggers', colour=0x00ff00)
        emb1.add_field(name='Alex', value='Is an Octa-Cosa **Bitch**', inline=False)
        emb1.add_field(name='Jason', value='Is Paddle Daddy', inline=False)
        emb1.add_field(name='Sky', value='Kicked someone in the balls', inline=False)
        emb1.add_field(name='Kevin', value='Is the pokemon Sugar Daddy', inline=False)
        emb1.add_field(name='Paddle', value='You have been McPaddled by Paddle Daddy', inline=False)
        emb1.add_field(name='Patricia', value= 'Boiling hotdogs the travis g money way since 2017', inline=False)
        emb1.add_field(name='Joe', value='Taken by Gigi', inline=False)
        emb1.add_field(name='Gigi', value='Taken by Joe', inline=False)
        emb1.add_field(name='Jacob', value='Is Jewish', inline=False)
        await bot.send_message(message.channel, embed=emb1)
#A test for array usage for 8ball
    if message.content.upper().startswith('!9BALL'):
        ran5 = random.randint(1,12)
        resp = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10", "test11", "test12"]
        emb1 = discord.Embed(colour=0x00ff00)
        emb1.add_field(name='9Ball', value=resp[ran5])
        await bot.send_message(message.channel, embed=emb1)
    if message.content.upper().startswith('!COIN'):
        ran6 = random.randint(1,3)
        coin = ["It's McHeads!", "It's McTails", "It's neither cause Fuck you"]
        emb1 = discord.Embed(colour=0x00ff00)
        emb1.add_field(name='CoinFLip', value=coin[ran6])
        await bot.send_message(message.channel, embed=emb1)
#Dev option
    if message.content.upper().startswith('!GAME'):
        args = message.content.split(' ')
        emb1 = discord.Embed(colour=0x800080)
        await bot.change_presence(game=discord.Game(name="%s" % (" ".join(args[1:]))))
        emb1.add_field(name='Indeedidly', value='I am now playing %s' % (" ".join(args[1:])))
        await bot.send_message(message.channel, embed=emb1)
#choose command
    if message.content.upper().startswith('!CHOOSE'):
        args = message.content.split(' ;')
        emb1 = discord.Embed(colour=0x00ff00)
        ran6 = random.randint(1, (len(args) - 1))
        emb1.add_field(name='I choose', value='%s' % (" ".join(args[ran6])))
        await bot.send_message(message.channel, embed=emb1)
                       
bot.run("NDUzMzk0NTM4MjA4NDI4MDQz.DfeQGQ.utRGRTjtFxqaLWCqMZSuj7gzpqE")
