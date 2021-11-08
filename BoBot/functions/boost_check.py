from discord.utils import get
import discord
import time

async def check_boost_member(og, new):
    if new.premium_subscriber_count > og.premium_subscriber_count:
      for member in new.premium_subscribers:
        if member in og.premium_subscribers:
          embed = discord.Embed(title = 'Boost Alert', description = f'{member.mention} has boosted the server at <t:{time.time()}:R>', color = discord.Color.gold())
          channel = get(new.channels, id = 863792978749292544)
          await channel.send(embed = embed)
          break
    elif new.premium_subscriber_count < og.premium_subscriber_count:
      for member in og.premium_subscribers:
        if not member in new.premium_subscribers:
          embed = discord.Embed(title = 'Boost Alert', description = f'{member.mention} has removed their server boost at <t:{time.time()}:R>', color = discord.Color.gold())
          channel = get(new.channels, id = 863792978749292544)
          await channel.send(embed = embed)
          break