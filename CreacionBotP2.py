import discord
from discord.ext import commands

TOKEN = 

bot = commands.Bot(command_prefix = 'csw!')

@bot.event
async def on_ready():
	print('Esta Vivooooo')

@bot.event
async def on_message(message):
	autor = message.author
	contenido = message.content
	print('{}:{}'.format(autor,contenido))

@bot.event
async def on_message_delete(message):
	autor = message.author
	contenido = message.content
	await bot.send_message(message.channel,'{}:{}'.format(autor,contenido))
	
bot.run(TOKEN)
