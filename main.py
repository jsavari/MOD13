import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="/");

@client.event
async def on_ready():
  print('MOD6 moderating server')
  print("Bot" + client.user.name)
  print("MOD6 ID" + client.user.id)
  print('------')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount = 6):
	await ctx.channel.purge(limit = amount);

@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
	await member.ban(reason=reason)
	await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.mention}')
			return

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_member_join(member):
	print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
	print(f'{member} has left a server.')

#client.run("token");
