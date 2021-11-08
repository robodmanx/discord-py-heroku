from main import accessConfig, sendEmbed
  
async def count(self, message):
  if message.channel.id == accessConfig(message.guild.id, 'count_channel') and message.author != self.client.user:
    cur_count = accessConfig(message.guild.id, 'count_num')
    prev_counter = accessConfig(message.guild.id, 'prev_counter')
    words = message.content.split()
    first_word = words[0]
    if first_word.isnumeric():
      if accessConfig(message.guild.id, 'no_double_counting'):
        if message.author.id == prev_counter:
          await sendEmbed(message.channel, 'You cannot count twice in a row!')
          return
      if first_word == str(cur_count):
        await message.add_reaction('✅')
        accessConfig(message.guild.id, 'prev_counter', 'write', message.author.id)
        accessConfig(message.guild.id, 'count_num', 'write', cur_count + 1)
      else:
        if cur_count != 1:
          await message.add_reaction('❌')
          await sendEmbed(message.channel, f'{message.author.mention} messed it up on **{cur_count}**!\nThe next number is **1**.')
          accessConfig(message.guild.id, 'count_num', 'write', 1)
        else:
          await sendEmbed(message.channel, 'The first number is **1**.')