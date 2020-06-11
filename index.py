#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
import subprocess
from subprocess import PIPE

# DiscordToken
TOKEN = 'Your Token'

# 接続に必要なオブジェクトを生成
client = discord.Client()

############################################################################################################################################

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ready...')
    channel = client.get_channel(ChannelID)

    await channel.send("起動しました")


############################################################################################################################################
# 自分
me_id = "myID"

############################################################################################################################################
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    global isPlaying
    
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

####################################################################################################
    # DMリジェクト
    if not isinstance(message.channel, discord.TextChannel):
        await message.channel.send('DMでの操作はできません')#DM操作禁止
            
####################################################################################################

    # 照明スイッチ  
    if message.content == 'on light':
        # ユーザ選別
        if (str)(message.author) == me_id:
            subprocess.run("絶対パス/lightOn.sh",shell=True,text=True)# ONコマンド
            time.sleep(1)
            await message.channel.send('照明をONにセットしました'+rasp)
        else:
            await message.channel.send(f'{message.author.mention} 命令権が付与されていませんよ〜？')

    if message.content == 'off light':
        # ユーザ選別
        if (str)(message.author) == me_id:
            subprocess.run("絶対パス/lightOff.sh",shell=True,text=True)# Offコマンド
            await message.channel.send("照明をOFFにセットしました"+rasp)
        else:
            await message.channel.send(f'{message.author.mention} 命令権が付与されていませんよ〜？')

####################################################################################################
    # 冷房スイッチ
    if message.content == 'on air':
        if (str)(message.author) == me_id:
            subprocess.run("絶対パス/airconOn.sh",shell=True,text=True)# ONコマンド
            await message.channel.send("冷房をONにセットしました"+rasp)
        else:
            await message.channel.send(f'{message.author.mention} 命令権が付与されていませんよ〜？')

    if message.content == 'off air':
        if (str)(message.author) == me_id:
            subprocess.run("絶対パス/airconOff.sh",shell=True,text=True)# Offコマンド
            await message.channel.send("冷房をOFFにセットしました"+rasp)
        else:
            await message.channel.send(f'{message.author.mention} 命令権が付与されていませんよ〜？')
    
####################################################################################################
    # コマンド一覧
    if message.content == 'Help iotbot':
        await message.channel.send("```コマンド一覧ですー\non light: 照明ON\noff light: 照明OFF\non air: 冷房ON\noff air: 冷房OFF\nHelp iotbot: これ```")

####################################################################################################


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)