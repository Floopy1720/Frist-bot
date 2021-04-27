import os
import discord
from discord.ext import commands

################################
my_secret = os.environ['token']
################################
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = ".", intents=intents)

@client.event
async def on_ready():
  print('All ok')
@client.event
async def on_member_join(member):
  print(f'{member} has joined')

@client.event
async def on_member_remove(member):
  print(f'{member} has left a server')

client.run(my_secret)