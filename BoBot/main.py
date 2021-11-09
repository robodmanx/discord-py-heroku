# imports

import discord
from discord.ext import commands
import os
import json

# setup

for i in os.listdir():
  if i == 'BoBot':
    os.chdir(i)

# config

def accessConfig(server: int = 890220889688408074, param: str = '', mode: str = 'read', to_write = None): 
  with open('config.json', 'r') as config:
    config_data = json.load(config)
  if mode == 'read':
    return config_data[str(server)][0][param]
  elif mode == 'write':
    with open('config.json', 'w') as output:
      if to_write:
        config_data[str(server)][0][param] = to_write
        json.dump(config_data, output)

# settings

client = commands.Bot(command_prefix = '!!')

# functions

def roleCheck(ctx, member: discord.Member, roles: list):
  toReturn = False
  for v in roles:
    role = discord.utils.find(lambda r: r.id == v, ctx.guild.roles)
    if role in member.roles:
      toReturn = True
  return toReturn


async def sendEmbed(ctx, message = '', title = '', img = '', attach = None, footer = 'BoBot Version 1.0.3', fields = {}):
    embed = discord.Embed(title = title, description = message, color = discord.Color.gold())
    embed.set_author(name = client.user.display_name, icon_url = client.user.avatar_url)
    embed.set_footer(text = footer)
    embed.set_image(url = img)
    for title in fields:
      text = fields[title]
      embed.add_field(name = title, value = text, inline = False)
    return await ctx.send(embed = embed, file = attach)

# cogs

for file in os.listdir('./cogs'):
  if file.endswith('.py'):
    client.load_extension(f'cogs.{file[:-3]}')

@client.command()
@commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
async def reload(ctx, filename):
  await ctx.message.delete()
  try:
    client.unload_extension(f'cogs.{filename}')
    client.load_extension(f'cogs.{filename}')
  except commands.ExtensionNotLoaded:
    client.load_extension(f'cogs.{filename}')
    await sendEmbed(ctx, f"Cog '{filename}.py' has been loaded")
  except commands.ExtensionNotFound:
    await sendEmbed(ctx, f"Cog '{filename}.py' does not exist")

@reload.error
async def rcError(ctx, error: commands.CommandError):
  await ctx.message.delete()
  if isinstance(error, commands.MissingRequiredArgument):
    await sendEmbed(ctx, 'You have not entered a cog to reload', footer = f'*{str(error)}*')  

# run

client.run(os.getenv('DISCORD_TOKEN'))
