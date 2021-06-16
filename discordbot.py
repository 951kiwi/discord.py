from discord.ext import commands
import discord
import time
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


# 接続に必要なオブジェクトを生成
client = discord.Client()
print('接続中・・・')
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
        print('■■■■■■□□□□■■□□□■■■■□□□□□■■■■■□□□□■■■■□□□□■■■■■□□□■■■■■■□□')
        print('■□□□□■■□□□■■□□■□□□■■□□□■■□□□■□□□■■□□□■■□□■□□□□■□□■□□□□■■□')
        print('■□□□□□■■□□■■□□■□□□□□□□■■□□□□□□□■■□□□□□■□□■□□□□■■□■□□□□□■■')
        print('■□□□□□□■□□■■□□■■■□□□□□■□□□□□□□□■□□□□□□■■□■□□□□■□□■□□□□□□■')
        print('■□□□□□□■□□■■□□□□■■■□□□■□□□□□□□□■□□□□□□■■□■■■■■□□□■□□□□□□■')
        print('■□□□□□□■□□■■□□□□□□■■□□■□□□□□□□□■□□□□□□■■□■□□□■□□□■□□□□□□■')
        print('■□□□□□■■□□■■□□□□□□□■□□■■□□□□□□□■■□□□□□■□□■□□□□■□□■□□□□□■■')
        print('■□□□□■■□□□■■□□■□□□■■□□□■■□□□■□□□■■□□□■■□□■□□□□■■□■□□□□■■□')
        print('■■■■■■□□□□■□□□□■■■■□□□□□■■■■□□□□□■■■■□□□□■□□□□□■□■■■■■■□□')
        print(discord.__version__)
        print(discord.version_info)
        print('ログインしました')

# メッセージ受信時に動作する処理

@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーんｓ')

    elif message.content == '/checking':
        await message.channel.send('BOT起動確認[Py]')
        return

# /memzコマンド
    if message.content == '!memz':
        print(f'鯖:[{message.guild.name}({message.channel.name})]/プレイヤー:[{message.author.name}]')
        print("さんが !memz を実行！！猫ネコねこ")
        if message.author.voice is None: #もしメッセージを送った人がボイスチャンネルを使っていなかった場合
            await message.channel.send("あなたはボイスチャンネルに接続していません。")
            print(f"[{message.author.name}]ボイスチャンネルに接続していません")
            return  #終了
        elif message.guild.voice_client is None:                                        #もしサーバーのボイスちゃんねるにBOTが入ってなかった場合
            await message.author.voice.channel.connect()                            #接続
            print(f"[{message.author.name}]BOTを移動させます。")
        elif message.guild.voice_client.is_playing():   #もし音楽が流れていたら
            message.guild.voice_client.stop()       #音楽停止
            await message.guild.voice_client.move_to(message.author.voice.channel)  #移動
            print(f"[{message.author.name}]音楽を一時停止")
        print(f"[{message.author.name}]音楽を再生します。")
        message.guild.voice_client.play(discord.FFmpegPCMAudio("NyanCat.mp3")) #音楽再生
        await message.channel.send(file=discord.File("nyancat.gif")) #画像送信
        print("3.5秒クールタイム")
        time.sleep(3.5) #３．５秒待機
        print("クールタイム終了")
        await message.channel.send(file=discord.File("nyanCat_cat.gif")) #画像送信
        print(f"[{message.author.name}]memzコマンド実行完了")



    if message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("どこにも入っていません")
            return
        await message.guild.voice_client.disconnect()
        await message.channel.send("切断しました。")

# Botの起動とDiscordサーバーへの接続
client.run(token)

