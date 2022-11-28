## a discord music bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
import os
import youtube_dl
import requests
import json
import urllib.request
import urllib.parse
import urllib.error


# bot prefix
Client = discord.Client()
client = commands.Bot(command_prefix = "r!")

# bot status
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='r!help'))
    print("The bot is ready!")

# bot commands
@client.event
async def on_message(message):
    if message.content.upper().startswith('R!HELP'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Check your DMs!" % (userID))
        await client.send_message(message.author, "```r!help - Displays this message\nr!ping - Pong!\nr!8ball - Ask the magic 8ball a question\nr!roll - Roll a dice\nr!say - Make the bot say something\nr!kick - Kick a user\nr!ban - Ban a user\nr!purge - Delete a certain amount of messages\nr!invite - Invite the bot to your server\nr!info - Get info about the bot\nr!serverinfo - Get info about the server\nr!userinfo - Get info about a user\nr!avatar - Get a user's avatar\nr!play - Play a song from YouTube\nr!skip - Skip the current song\nr!stop - Stop the music and clear the queue\nr!queue - Show the music queue\nr!pause - Pause the music\nr!resume - Resume the music\nr!np - Show the current song\nr!volume - Change the volume of the music\nr!leave - Make the bot leave the voice channel```")

    if message.content.upper().startswith('R!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))

    if message.content.upper().startswith('R!play'):
        if message.author.voice_channel:
            channel = message.author.voice_channel
            await client.join_voice_channel(channel)
        else:
            await client.say("You are not in a voice channel.")
        
        url = message.content.split(" ", 1)[1]
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        players[server.id] = player
        player.start()

    if message.content.upper().startswith('R!skip'):
        id = message.server.id
        players[id].stop()

    if message.content.upper().startswith('R!stop'):
        server = message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()

    if message.content.upper().startswith('R!queue'):
        await client.say("The queue is empty.")

    if message.content.upper().startswith('R!pause'):
        id = message.server.id
        players[id].pause()

    if message.content.upper().startswith('R!resume'):
        id = message.server.id
        players[id].resume()
    
    if message.content.upper().startswith('R!np'):
        await client.say("There is nothing playing.")

    if message.content.upper().startswith('R!volume'):
        volume = message.content.split(" ", 1)[1]
        id = message.server.id
        players[id].volume = volume

    if message.content.upper().startswith('R!leave'):
        server = message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()

    if message.content.upper().startswith('R!loop'):
        id = message.server.id
        players[id].loop = True

    if message.content.upper().startswith('R!24/7'):
        id = message.server.id
        players[id].loop = True

    

    