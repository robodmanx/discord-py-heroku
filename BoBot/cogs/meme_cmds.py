for i in os.listdir():
  if i == 'BoBot':
    os.chdir(i)

import discord
import random
from discord.ext import commands
from main import roleCheck, sendEmbed

sizes = [
  'Negative',
  'Nonexistent',
  'Microscopic',
  'Tiny',
  'Small',
  'Average',
  'Above Average',
  'Large',
  'Huge',
  'Excessive',
  'Gargantuan',
  'Interplanetary',
  'Interdimensional'
  ]

adminRoles = [
  890275139676143648,
  890228091958493214,
  890225719974723686
  ]

class MemeCommands(commands.Cog):
  def __init__(self, client):
    self.client = client  
    print('loaded meme commands cog')

  # commands

  @commands.command()
  async def pingSexOffender(self, ctx):
    await ctx.message.delete()
    for i in range(5):
      await ctx.send('<@&890234427626631208> press alt + f4')

  @commands.command()
  async def doaflip(self, ctx):
      await ctx.message.delete()
      await sendEmbed(ctx, img = 'https://c.tenor.com/SXuNqd9ILMUAAAAC/backflip-back.gif')

  @commands.command()
  async def jesus(self, ctx):
      await ctx.message.delete()
      await sendEmbed(ctx, img = 'https://upload.wikimedia.org/wikipedia/en/thumb/2/2c/Buc-ee%27s_beaver.svg/1200px-Buc-ee%27s_beaver.svg.png')

  @commands.command()
  async def revealyourself(self, ctx):
      await ctx.message.delete()
      await sendEmbed(ctx, img = 'https://i.makeagif.com/media/7-22-2015/46UFUv.gif')

  @commands.command()
  async def panjabi(self, ctx):
      await ctx.message.delete()
      await ctx.send(file = discord.File('panjabi.mp3'))

  @commands.command()
  async def ppsize(self, ctx):
      await ctx.message.delete()

      if roleCheck(ctx, ctx.author, [890237792976769074]): #discord moderator role
        size = sizes[random.randint(0,3)]
      elif roleCheck(ctx, member = ctx.author, roles = adminRoles):
        size = sizes[random.randint(7,12)]
      else: #normal people
        size = random.choice(sizes)
          
      await sendEmbed(ctx, message = f'{ctx.author.display_name}, your pp is {size}.')

def setup(client):
  client.add_cog(MemeCommands(client))
