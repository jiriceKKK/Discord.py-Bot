import discord 
import Bdiscord
from discord.ext import commands # Imports Modules From Library

client = commands.Bot(command_prefix = "YOUR PREFIX")

@client.event
async def on_ready(): # Function After The Bot Is Ready
  print("YOUR TEXT AFTER THE BOT IS READY") # This Showing The Message After Funcion Started


# First Command With Bdiscord

@client.command() # Shows This As A Command
async def ping(ctx): # Creating The Function Named ping | ctx = The Command (?ping) ? Is My Prefix
  await Bdiscord.send(ctx, f"Pong {ctx.author.mention}!") # Sending The Response Pong And Username


@client.command() # Shows This As A Command
async def createchannel(ctx, channel_name): # Creating The Function Named createchannel What Asks For channel_name
  await Bdiscord.createText(ctx, channel_name) # Creating The Text Channel Named Variable channel_name
  await Bdiscord.send(ctx, f"Channel {channel_name} Was Created.") # Sending Message That Channel Was Been Created


client.run("OTUyOTQxODM5MTY4NzA4Njc4.Yi9WPw.zy904zGwXHgw64dp8N2OffDSgFw")
