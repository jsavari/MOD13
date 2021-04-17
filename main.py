import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".");

@client.event
async def on_ready():
  print('MOD13 deployed')
  print(f'MOD13 ID: {client.user.id}')
  print('------')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=10):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = " "):
	await member.send("You are kicked from the server!")
	await member.kick(reason=reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason= ""):
	await ctx.send("Banned " + member.name)
	await member.ban(reason=reason)

@client.command(aliases=['u'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if(user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanned {user.mention}')
      return

@unban.error
async def unban_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("**Moderator permission required!**")

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("**Moderator permission required!**")

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.CheckFailure):
    await ctx.send("**Moderator permission required!**")

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run("ODMxNTk3ODA2MzkyOTY3MjUy.YHXjzw.l0o0MJh82-D46-eorEyqrMiTVG0");
