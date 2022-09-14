from discord.colour import Colour
from discord.ext import tasks, commands
from datetime import datetime, timedelta
import discord
import time
import os
import datetime
import my_function as mf
import many_list
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
voice_faction = 888341603008270367
Voice_Channel_List = []
pretime_dict = {}


intents=discord.Intents.all()
client = discord.Client(intents=intents)
# 接続に必要なオブジェクトを生成
client = discord.Client()
print('接続中・・・')
# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
        print("succeeded v12")
        for channel in client.get_all_channels():
            Voice_Channel_List.append(channel.id)
        mf.start_text()
        send_message_every_5sec.start()
i = 0
@tasks.loop(seconds=5)
async def send_message_every_5sec():
    kiwi = ["🥝","🍉","🍊","🍋","🍌","🍍","🍎","🍏","🍐","🍑","🍒","🍓","🥥","🥭"]
    global i
    if i == 0:
        i = 1
        sel_f1 = random.choice(kiwi)
        sel_f2 = random.choice(kiwi)
        sel_kiwi = "🥝"+sel_f1+"🥝"+sel_f2+"🥝"+"_____________"
        activity = discord.Activity(name=sel_kiwi, type=discord.ActivityType.listening)
        await client.change_presence(activity=activity)
    elif i == 1:
        i = 2
        sel_f1 = random.choice(kiwi)
        sel_f2 = random.choice(kiwi)
        sel_f3 = random.choice(kiwi)
        sel_kiwi = sel_f1+"新機能追加予定"+sel_f2
        activity = discord.Activity(name=sel_kiwi, type=discord.ActivityType.listening)
        await client.change_presence(activity=activity)
    elif i == 2:
        i = 0
        sel_f1 = random.choice(kiwi)
        sel_f2 = random.choice(kiwi)
        sel_f3 = random.choice(kiwi)
        sel_kiwi = sel_f1+"ここの文字が変わるよ"+sel_f2
        activity = discord.Activity(name=sel_kiwi, type=discord.ActivityType.listening)
        await client.change_presence(activity=activity)
# メッセージ受信時に動作する処理
# メッセージ受信時に動作する処理

@tasks.loop(seconds=10)
async def send_message_every_10sec():
    print("10秒経ったよ")
    print(datetime.datetime.now())

@client.event
async def on_member_join(member):
    guild = bot.get_guild(client.get_guild.id)
    print(guild)

@client.event
async def on_voice_state_update(member, before, after):
    global Voice_Channel_List
    global pretime_dict
    voice_server = client.get_channel(voice_faction)
    if before.channel != after.channel:
        now = datetime.datetime.utcnow() + timedelta(hours=9)
        if before.channel is not None and before.channel.id in Voice_Channel_List:
            duration_time = pretime_dict[before.channel.id] - datetime.datetime.now()
            duration_time_adjust = int(duration_time.total_seconds()) * -1
            total_sec = 0
            total_min = 0
            total_hou = 0
            total_sec = duration_time_adjust % 60 #あまり
            total_min = (duration_time_adjust // 60) % 60
            total_hou = (duration_time_adjust // 60) //60
            title = f"退出通知:// {member.name} // 通話時間：{total_hou}時間{total_min}分{total_sec}秒"
            descriptions = f"{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。  通話時間：{total_hou}時間{total_min}分{total_sec}秒"
            if total_hou == 0:
                title = f"退出通知:// {member.name} // 通話時間：{total_min}分{total_sec}秒"
                descriptions = f"{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。  通話時間：{total_min}分{total_sec}秒"
                if total_min == 0:
                    title = f"退出通知:// {member.name} // 通話時間：{total_sec}秒"
                    descriptions = f"{now:%m/%d-%H:%M} に {member.name} が {before.channel.name} から退出しました。  通話時間：{total_sec}秒"
            color = str("red")
            embet = mf.make_enbed( str(title) , str(descriptions) , color )
            await voice_server.send(embed=embet)
        if after.channel is not None and after.channel.id in Voice_Channel_List:
            pretime_dict[after.channel.id] = datetime.datetime.now()

            title = f"参加通知:// {member.name} // 開始時間：{now:%m/%d-%H:%M}"
            descriptions = f"{now:%m/%d-%H:%M} に {member.name} が {after.channel.name} に参加しました。"
            color = str("green")
            embet = mf.make_enbed( str(title) , str(descriptions) , color )
            await voice_server.send(embed=embet)

@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーんｓ')

    elif message.content == '!mov':
        await message.channel.send(file=discord.file("join/1.mp4"))
        return
    #embeds作成定義
    if message.content.startswith("!embeds"):
        tmp = message.content.split("///")
        tmp_Element_count = len(tmp)
        if tmp_Element_count == 1:
            await message.channel.send("!embedsコマンドの使い方\n!embeds///[タイトル]///[内容]///[カラーコード(16進数)]\nカラーコードは[red,gereen]などでも選択可、もし設定されない場合defaultになります")
            return
        if tmp_Element_count == 2:
            title = tmp[1]
            descriptions = "_"
            color = "a"
        if tmp_Element_count == 3:
           title = tmp[1]
           descriptions = tmp[2]
           color = "a"
        if tmp_Element_count == 4:
            title = tmp[1]
            descriptions = tmp[2]
            color = tmp[3]
        enbet = mf.make_enbed( str(title) , str(descriptions) , color )
        if enbet == "not_color":
            await message.channel.send("色コードの取得に失敗しました。\n色コードを16進数もしくは英単語[red.pinkなど]で入力してね")
        elif enbet == "6text":
            await message.channel.send("色コードの取得に失敗しました。\n色コードの桁数は最大6桁までです。")
            return
        else:    
            await message.channel.send(embed=enbet)

# /memzコマン
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
        message.guild.voice_client.play  (discord.FFmpegPCMAudio  ("NCAT/NyanCat.mp3"))  #音楽再生
        await message.channel.send(file=discord.File("NCAT/Nyancat.gif")) #画像送信
        print("3.5秒クールタイム")
        time.sleep(3.5) #３．５秒待機
        print("クールタイム終了")
        await message.channel.send(file=discord.File("NCAT/NyanCat_cat.gif")) #画像送信
        print(f"[{message.author.name}]memzコマンド実行完了")



    if message.content == "!leave":
        if message.guild.voice_client is None:
            await message.channel.send("どこにも入っていません")
            return
        await message.guild.voice_client.disconnect()
        await message.channel.send("切断しました。")
    if message.content.startswith("!a"):
        user = message.guild.get_role(833728710543933521)
        user_list = user.members
        for user in user_list:
            print(user.id)
#DMコマンド
    if message.content.startswith("!dm"):
        tmp = message.content.split("///")
        if len(tmp) == 1:
            await message.channel.send("HELPを表示します。\n!dm///@[ユーザ||ロール]///[内容]\nって感じで使ってね。")
        if len(tmp) == 2:
            await message.channel.send("内容が確定していないため送信できません")
        if len(tmp) == 3:
            if "<@" in tmp[1] and ">" in tmp[1]:
                if "&" in tmp[1]:#ロール
                    role = str(tmp[1])
                    role = role.replace('<@&','')
                    role = role.replace(' ','')
                    role = role.replace('>','')
                    
                    if len(role) != 18:
                        await message.channel.send("ロール取得時に何らかのエラーが発生しました。")
                        return
                    role = message.guild.get_role(int(role))
                    names = []
                    for user_list in role.members:
                        user = await client.fetch_user(user_list.id)
                        await user.send(str(tmp[2]))
                        names.append(f"{user_list.name}[NickName:{user_list.nick}]")
                    #下メッセージ作成用
                    names = (str(names).replace(",","\n").replace("'","").replace(" ",""))[1:][:-1]
                    msg = (f"-----[情報]-----\nロール名:\t{role.name}\nロール内人数:\t{len(role.members)}\n送信内容:\t{tmp[2]}\n-----[メンバー]-----\n{names}\n-----\n{len(role.members)}人のユーザーにDMを送信しました。")
                    await message.channel.send(msg)
                else:#ユーザー
                    user = str(tmp[1])
                    user = user.replace('<@','')
                    user = user.replace(' ','')
                    user = user.replace('>','')
                    if len(user) == 18:
                        user = await client.fetch_user(user)
                        await user.send(tmp[2])
                        msg = (f"-----[情報]-----\nユーザー名:\t{user.name}\n送信内容:\t{tmp[2]}\nユーザーにDMを送信しました。")
                        await message.channel.send(msg)
                    else:
                        await message.channel.send("ユーザ取得時に何らかのエラーが発生しました。")
        
            

# Botの起動とDiscordサーバーへの接続
client.run(token)
