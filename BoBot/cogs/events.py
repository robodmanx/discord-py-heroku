import os

for i in os.listdir():
  if i == 'BoBot':
    os.chdir(i)

from discord.ext import commands
from discord.utils import get

from main import sendEmbed
from functions import counting

import time
import discord

class Events(commands.Cog):
  def __init__(self, client):
    self.client = client 
    print('loaded events cog')

  @commands.Cog.listener()
  async def on_message(self, message):
    await counting.count(self, message)
    if message.content == 'boi you built like a':
      await message.channel.send(file = discord.File('panjabi.mp3'))

  @commands.Cog.listener()
  async def on_message_delete(self, message):
    if message.author != self.client and not message.content.startswith('!!'):
      await sendEmbed(get(message.guild.channels, id = 891685583137697913), message = f"*{message.author.mention}'s message was deleted in {message.channel.mention}*", fields = {'Message:': message.content}, footer = str(time.asctime(time.localtime())))

  @commands.Cog.listener()
  async def on_message_edit(self, og, edit):
    if edit.author != self.client:
      await sendEmbed(get(edit.guild.channels, id = 891685583137697913), message = f"*{edit.author.mention} has edited their message in {edit.channel.mention}*", fields = {'Original Message': og.content, 'Edited Message': edit.content}, footer = str(time.asctime(time.localtime())))

  @commands.Cog.listener()
  async def on_ready(self):
    print(f'Bot is up: {time.asctime(time.localtime())}')

  @commands.Cog.listener()
  async def on_member_update(self, og, update):
    print('a')
    if og.id == self.client.user.id:
      print('b')
      if update.status == discord.Status.offline:
        print('c')
        status_channel = get(update.guild.voice_channels, name = 'BOBOT IS: ONLINE')
        print(status_channel.id)

def setup(client):
  client.add_cog(Events(client))
