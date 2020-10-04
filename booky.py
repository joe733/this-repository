import discord, datetime, schedule
from discord.ext import commands

TOKEN = open('token.txt','r').readline()
client = commands.Bot(command_prefix = '.')

channel_id = '759708291160604707'
now = datetime.datetime.now()
print(now.hour)

@client.event
async def on_ready():
    print(f'logged in as {client.user}')
    await message()

async def message(): 
    channel = client.get_channel(759708291160604707)
    await channel.send('hello')

@client.command()
async def hello(ctx):
    await ctx.send('Hey. How can I help?')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'{error}')

client.run(TOKEN)