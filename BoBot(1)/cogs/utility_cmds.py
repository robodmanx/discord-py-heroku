import discord
from discord.ext import commands
from main import sendEmbed
from discord.utils import get
import time

class UtilCommands(commands.Cog):
  def __init__(self, client):
    self.client = client
    print('loaded utility commands cog')

  # commands
  
  @commands.command()
  @commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
  async def ping(self, ctx):
      await ctx.message.delete()
      await sendEmbed(ctx, f'Current client ping is {round(self.client.latency * 1000)} ms')

  @commands.command()
  @commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
  async def purge(self, ctx, num=-1):
      await ctx.message.delete()
      if num > 0:
          await ctx.channel.purge(limit = num)
          await sendEmbed(ctx, f'Successfully purged up to {num} messages in <#{ctx.channel.id}>')
      else:
        await sendEmbed(ctx, message = 'Parameter <num> must be an integer value higher or equal to 0')

  @commands.command()
  @commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
  async def slowmode(self, ctx, cid = -1, delay = -1):
      await ctx.message.delete()
      if isinstance(cid, int) and isinstance(delay, int):
          if cid > 0 and delay >= 0:
            channel = ctx.guild.get_channel(int(cid))
            if channel == None:
              await sendEmbed(ctx, f'Invalid channel ID "{cid}"')
              return
            await channel.edit(slowmode_delay = int(delay))
            await sendEmbed(ctx, f'Successfully set the slowmode delay in <#{cid}> to {delay} seconds')  
          else:
            await sendEmbed(ctx, 'Invalid syntax')
      else:
          await sendEmbed(ctx, 'Invalid syntax')

  @commands.command()
  @commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
  async def kick(self, ctx, member: discord.Member, *, reason: str):
    await ctx.message.delete()
    await member.kick(reason = reason)
    await sendEmbed(ctx, message = f'Successfully kicked {member.mention}')

  @commands.command()
  @commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
  async def ban(self, ctx, member: discord.Member, *, reason: str):
    await ctx.message.delete()
    await member.ban(reason = reason)
    await sendEmbed(ctx, message = f'Successfully banned {member.mention}')

  @commands.command()
  @commands.has_any_role(890275139676143648, 890225719974723686, 890228091958493214)
  async def unban(self, ctx, *, member: discord.Member):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for entry in banlist:
      banMember = entry.user
      if member == banMember:
        await ctx.guild.unban(banMember)
        await sendEmbed(ctx, message = f'Successfully unbanned {banMember.mention}')
        return
    await sendEmbed(ctx, message = f'Member {member.mention} is not banned')

  @commands.command()
  async def av(self, ctx, *, user: discord.Member = None):
      await ctx.message.delete()
      if not user:
          user = ctx.author
      await sendEmbed(ctx, title = f"{user.display_name}'s profile picture:", img = user.avatar_url)

  # error handlers

  @av.error
  async def avError(self, ctx, error):
      if isinstance(error, commands.CommandError):
          if ctx.message:
              await ctx.message.delete()
          await sendEmbed(ctx, 'User was not found')

  @slowmode.error
  async def smError(self, ctx, error):
      if isinstance(error, commands.CommandError):
          if ctx.message:
              await ctx.message.delete()
          await sendEmbed(ctx, message = 'One or more arguments is invalid', footer = str(error))

  @purge.error
  async def pgError(self, ctx, error):
    if isinstance(error, commands.CommandError):
      if ctx.message:
        await ctx.message.delete()
      await sendEmbed(ctx, message = 'Parameter <num> must be an integer value higher than or equal to 0', footer = str(error))

  @kick.error
  async def kickError(self, ctx, error):
    if isinstance(error, commands.CommandError):
      if ctx.message:
        await ctx.message.delete()
      await sendEmbed(ctx, message = 'Invalid member', footer = str(error))

  @ban.error
  async def banError(self, ctx, error):
    if isinstance(error, commands.CommandError):
      if ctx.message:
        await ctx.message.delete()
      await sendEmbed(ctx, message = 'Invalid member', footer = str(error))

  @unban.error
  async def unbanError(self, ctx, error):
    if isinstance(error, commands.CommandError):
      if ctx.message:
        await ctx.message.delete()
      await sendEmbed(ctx, message = 'Invalid member', footer = str(error))

def setup(client):
  client.add_cog(UtilCommands(client))