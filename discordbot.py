import discord
import datetime
import logging
import asyncio
import time
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

BOT_LOG = 698047351985668109
GLOBAL_CH_NAME = "rk-global"
now = datetime.datetime.now()
client = discord.Client()

async def reply(message):
    reply = f'{message.author.mention} メンションしたね？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信
    
async def greet():
    channel = client.get_channel(BOT_LOG)
    await channel.send('RK Botが起動しました')
  
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await greet() # 挨拶する非同期関数を実行
    
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('RKBOT自己紹介'):
        await message.channel.send('こんにちは！\私はRK氏によって作成されたBOTです。\nRK氏のチャンネルはこちらです\nhttps://www.youtube.com/channel/UC4x1TrGXD0V07dzFjCqYYrg')

    if message.content.startswith('誰'):
        await message.channel.send('俺')

    if message.content.startswith('草'):
        await message.channel.send('草')

    if message.content.startswith('無能'):
        await message.channel.send('いや有能だろ')

    if message.content.startswith('seek'):
        await message.channel.send('=prisma3d')

    if message.content.startswith('ドキスポ'):
        await message.channel.send('臭いイケメン')

    if message.content.startswith('frln'):
        await message.channel.send('新型ヒカマニウイルス感染者')

    if message.content.startswith('FRLN'):
        await message.channel.send('新型ヒカマニウイルス感染者')

    if message.content.startswith('ふぇる'):
        await message.channel.send('新型ヒカマニウイルス感染者')

    if message.content.startswith('FLLOX'):
        await message.channel.send('神')

    if message.content.startswith('ひっちえ'):
        await message.channel.send('ふぇるに並ぶヒカマニ')

    if message.content.startswith('hittie'):
        await message.channel.send('ふぇるに並ぶヒカマニ')

    if message.content.startswith('Hittie'):
        await message.channel.send('ふぇるに並ぶヒカマニ')

    if message.content.startswith('とりくん'):
        await message.channel.send('神')

    if message.content.startswith('X25'):
        await message.channel.send('=れんだー')

    if message.content.startswith('nitro'):
        await message.channel.send('nitro誰かくれ')

    if message.content.startswith('臭'):
        await message.channel.send('臭')
        
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行
   
    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

        embed = discord.Embed(title="rk-global",
            description=message.content, color=0xffc0cb)

        embed.set_author(name=f"{message.author.display_name} #{message.author.discriminator} (ID:{message.author.id})", 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} ",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)

    if message.content == '!rk checkadmin':
        if message.author.guild_permissions.administrator:
            await message.channel.send('あなたは管理者です')
        else:
            await message.channel.send('あなたは管理者ではありません')       
  
    if message.content.startswith('!rk time'):
        await message.channel.send('現在の時刻は{0:%H}時{0:%M}分{0:%S}秒です。'.format(now))
    
client.run('DISCORD_BOT_TOKEN')
