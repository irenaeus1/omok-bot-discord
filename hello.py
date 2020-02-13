import discord
import asyncio
 
client = discord.Client()

token = "Njc3NDM5NDIzNDQwMzU1MzU4.XkUi9A.BPqCeiBDkLMAaLd3-vXJ4XLfytM"
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await message.channel.send('test!!!!')
 
    # elif message.content.startswith('!say'):
    #     await message.channel.send(message.channel, 'leave message')
    #     msg = await client.wait_for_message(timeout=15.0, author=message.author)
 
    #     if msg is None:
    #         await message.channel.send(message.channel, '15초내로 입력해주세요. 다시시도: !say')
    #         return
    #     else:
    #         await message.channel.send(message.channel, msg.content)
 
client.run(token)