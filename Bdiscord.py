from xmlrpc import client
import discord
import random
from discord.ext import commands
import time

# CreateChannel Command

client = commands.Bot(command_prefix="?")

async def createChannel(ctx, channel):
    if ctx.author.guild_permissions.manage_channels:
        if channel != None:
            guild = ctx.guild
            existing_channel = discord.utils.get(guild.channels, name=channel)
            new_channel = await guild.create_text_channel(channel)
            await ctx.send(f'Channel "{channel}", Was Created')
        else:
            ctx.send("Missing Arguments.")
    else:
        ctx.send("Missing Premissions")


# DeleteChannel Command

async def deleteChannel(ctx, channel):
  if ctx.author.guild_permissions.manage_channels:

    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel)


    if existing_channel is not None:
      await existing_channel.delete()
      await ctx.send(f'Channel "{channel}" Deleted')
        

    else:
      await ctx.send(f'No Channel Named, "{channel}", Was Found.')
  else:
    await ctx.send(f"You Dont Have Permissions To Manage Channels {ctx.author}.")
# Kick Module
async def kick(ctx, member: discord.Member):
  await member.kick(reason=None)

# Kick Command

async def kickCommand(ctx, member: discord.Member, reason):
  if ctx.author.guild_permissions.kick_members:
    try:
      await member.kick(reason=reason)
      await ctx.send(f'User "{member.mention}", Has Been Kicked, Reason: {reason}.')
    except:
      await ctx.send(f"I Cant Do That.")
  else:
    await ("You Dont Have Permissions To Use This Command")

# Ban Modul
async def ban(member: discord.Member):
  await member.ban()

# Ban Command

async def banCommand(ctx, member: discord.Member, reason):
  if ctx.author.guild_permissions.ban_members:
    try:
      await member.ban(reason=reason)
      await ctx.send(f'User "{member.mention}", Has Been Banned.')
    except:
      await ctx.send(f"I Cant Do That.")
  else:
    await ("You Dont Have Permissions To Use This Command")

# Unban Command

async def unban(ctx, member):
    banned_users = await ctx.guild.bans()

    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.channel.send(f"Unbanned: {user.mention}")         
# 8ball Command

async def _8ball(ctx, question):
  responses = ["It is certain.",
                  "It is decidedly so.",
                  "Without a doubt.",
                  "Yes definitely.",
                  "You may rely on it.",
                  "As I see it, yes.",
                  "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                  "Reply hazy, try again.",
                  "Ask again later.",
                  "Better not tell you now.",
                  "Cannot predict now.",
                  "Concentrate and ask again.",
                  "Don't count on it.",
                  "My reply is no.",
                  "My sources say no.",
                  "Outlook not so good.",
                  "Very doubtful."]
  await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")



# Pong
async def ping(ctx):
  await ctx.send(f"Pong! {ctx.author.mention}")

# Send Commands
async def send(message):
  await message.send(message)

# Clear Command
async def clear(ctx, amount=None):
  if ctx.author.guild_permissions.manage_messages:
    if amount != None:
        amount = int(amount)
        await ctx.channel.purge(limit=amount+1)
    else:
      await ctx.send("Enter The Amount.")
  else:
      await ctx.send(f"You Dont Have Permissions To Manage Messages {ctx.author}.")

# Dm Command
async def dm(ctx, user:discord.Member, message=None):
  if message == None:
    await ctx.send("Please Enter The Message")
  else:
    try:
      await user.send(message)
      time.sleep(0.1)
      await ctx.channel.purge(limit=1)
    except:
      await ctx.send("I Cant Do This")

# Dm user
async def dmUser(ctx, user:discord.Member, message=None):
  await user.send(message)

# Delete Message

async def deleteMessage(ctx, limit):
  await ctx.channel.purge(limit=limit)

# Send Message In Channel

async def sendToChannel(ctx, channel: discord.TextChannel, message):
  if channel == None: 
      await ctx.send("You did not mention a channel!")
      return

  new_channel = discord.TextChannel(channel)

  await new_channel.send(message)
  await ctx.send("Nuked the Channel sucessfully!")

async def createText(ctx, channel_name):
  guild = ctx.guild
  await guild.create_text_channel(channel_name)

async def createVoice(ctx, channel_name):
  guild = ctx.guild
  await guild.create_voice_channel(channel_name)
