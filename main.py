import discord
import asyncio
import s_token
 
client = discord.Client()

token = s_token.tokenA
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        s=input()
        await message.channel.send(s)
 
    # elif message.content.startswith('!say'):
    #     await message.channel.send(message.channel, 'leave message')
    #     msg = await client.wait_for_message(timeout=15.0, author=message.author)
 
    #     if msg is None:
    #         await message.channel.send(message.channel, '15초내로 입력해주세요. 다시시도: !say')
    #         return
    #     else:
    #         await message.channel.send(message.channel, msg.content)
 
client.run(token)