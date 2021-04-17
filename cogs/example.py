import discord 
from discord.ext import commands

class Example(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print('MOD13 Cog Extension Unloaded')
		print('-----')
	
	#@commands.command()
        #add custom command here

def setup(client):
	client.add_cog(Example(client))
