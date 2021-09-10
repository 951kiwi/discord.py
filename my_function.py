import discord
import many_list


#start_text
def start_text():
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
#hex_check(check_word)16進数かの判断
def hex_check(check_word): #check word に16進数か判断したい文字を入れる
    for word_list in list(str(check_word)):#listで文字列を1文字ずつ分解させている
        ords = ord(word_list) #文字を数字に変換する(ord)
        if 48 <= ords <= 57 or 97 <= ords <= 102 or 65 <= ords <= 70 :
        # 48~57[0~9] 65~70[a~f] 97~102[A~F] であるかを判断している
            continue #続ける
        else:
            print("16進数のみ取り扱い可能です。")
            return False #16進数以外の文字が入っていた場合Falseを返す
    return True #すべての処理が問題なく終わった場合Trueを返す

#make_enbed(titles,descriptions,colors)embedの作成関数
def make_enbed(titles=" ",descriptions="_",colors="a"):
    #colors_af = many_list.color(colors)
    if len(list(colors)) <=6:
        if colors == "a":
            colors = discord.Colour.default()
            print("カラーコードが未設定のため、defaultで設定します。")
        else:
            colors = many_list.color(colors)
            colorset = colors.strip("#")
            if hex_check(colorset) == True:
                colors = "0x"+colorset
                colors = int(colors,16)

            else:
                return "not_color"
        embet = discord.Embed(title=str(titles), description=str(descriptions),color=colors)
        return embet
    else:
        return "6text"