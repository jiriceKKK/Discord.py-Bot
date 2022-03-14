import discord 
from discord.ext import commands # Imports Modules From Library
import Bdiscord

client = commands.Bot(command_prefix = "YOUR PREFIX HERE")

@client.event
async def on_ready():
  print("YOUR TEXT AFTER THE BOT IS READY")
  
 
 
 client.run("YOUR TOKEN")
