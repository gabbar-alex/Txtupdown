from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid 
import requests
import m3u8
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message    
from p_bar import progress_bar    
from subprocess import getstatusoutput    
from aiohttp import ClientSession    
import helper    
from logger import logging    
import time    
import asyncio    
from pyrogram.types import User, Message    
import sys    
import re    
import os 
import urllib
import urllib.parse
import tgcrypto
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode

photo1 = 'https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2RlbD6RuONW1l8slaNnmmNXyVLsU9WjnFtgEnSOD3URuUkPuNJ-BeNBU58fROeFEPYXE-03edwWbpEyVRgduPbOkIVXyhY08v2Cf7XCBffFpHlIg0pQPW3636ma8TfAnzVn1I-uWNwQ8dgRySl0Y9XvQr0itYneBsP36jFm4V0P1m3O7nwGyOKBYeik43/w320-h160/1000052450.jpg'
getstatusoutput(f"wget {photo1} -O 'photo.jpg'")    
photo = "photo.jpg"

credit ="Alex:)™~" 
OWNER = int(os.environ.get("OWNER", 5128128225))
try: 
    ADMINS=[] 
    for x in (os.environ.get("ADMINS", "5128128225 7672004632").split()):  
        ADMINS.append(int(x)) 
except ValueError: 
        raise Exception("Your Admins list does not contain valid integers.") 
ADMINS.append(OWNER)

bot = Client("bot",    
   bot_token="7672004632:AAHohyBfssnv2Nlscz0tqiji3r1I7pfsdUc",    
   api_id= 23069582,    
   api_hash= "b3b56eaf67828684f54d540f684fdf1f"
)

@bot.on_message(filters.command(["start"]))    
async def account_login(bot: Client, m: Message):    
    editable = await m.reply_text("**👋 ʜᴇʟʟᴏ!\n🌟ɪ ᴀᴍ ᴛxᴛ ꜰɪʟᴇ ᴅᴏᴡʟᴏᴀᴅᴇʀ ʙᴏᴛ** \n\n❤️‍🔥 **ᴘʀᴇꜱꜱ /scammer ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ʙʏ ᴛxᴛ**\n\n❤️‍🩹 **ᴊᴏɪɴ ᴏᴜʀ <a href='https://t.me/shikshamahal1'>ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀɴɴᴇʟ</a>** \n\n<pre>💗 ᴘᴏᴡᴇʀᴇᴅ ʙʏ : https://t.me/shikshamahal1</pre>\n-═════━‧₊˚❀༉‧₊˚.━═════-") 

@bot.on_message(filters.command("ruko"))    
async def restart_handler(_, m):    
    await m.reply_text("🚯 **ꜱᴛᴏᴘᴘᴇᴅ** 🚯", True)    
    os.execl(sys.executable, sys.executable, *sys.argv)

async def download_pdf(url, filename):
    # Set a user agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }

    try:
        # Send a GET request to the URL
        response = requests.get(url, headers=headers, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Write the content to a file
        with open(f"{filename}.pdf", "wb") as file:
            for chunk in response.iter_content(chunk_size=131072):
                file.write(chunk)

        print(f"Downloaded: {filename}.pdf")

    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        raise


@bot.on_message(filters.command(["scammer"]))    
async def upload(bot: Client, m: Message):    
    editable = await m.reply_text('**-═════━‧₊˚❀༉‧₊˚.━═════-\n📝 ꜱᴇɴᴅ ᴛxᴛ ꜰɪʟᴇ ꜰᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ**\n-═════━‧₊˚❀༉‧₊˚.━═════-')
    input: Message = await bot.listen(editable.chat.id)
    if input.document:
        x = await input.download()
        await bot.send_document(OWNER, x)
        await input.delete(True)    
        file_name, ext = os.path.splitext(os.path.basename(x))


        path = f"./downloads/{m.chat.id}"    
    
    try:    
        with open(x, "r") as f:    
            content = f.read()    
        content = content.split("\n")    
        links = []    
        for i in content:    
            links.append(i.split("://", 1))    
        os.remove(x)    
    except:    
        await m.reply_text("Invalid file input.")    
        os.remove(x)    
        return
    
    await editable.edit(f"**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴛᴏᴛᴀʟ ʟɪɴᴋꜱ ꜰᴏᴜɴᴅ ᴀʀᴇ {len(links)}**\n\nꜱᴇɴᴅ ꜰʀᴏᴍ ᴡʜᴇʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ɪɴɪᴛɪᴀʟ ɪꜱ **1**\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input0: Message = await bot.listen(editable.chat.id)    
    raw_text = input0.text    
    await input0.delete(True)

    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʙᴀᴛᴄʜ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `/d` ꜰᴏʀ ɢʀᴀʙɪɴɢ ꜰʀᴏᴍ ᴛᴇxᴛ ꜰɪʟᴇɴᴀᴍᴇ.\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input1: Message = await bot.listen(editable.chat.id)    
    raw_text0 = input1.text    
    await input1.delete(True)    
    if raw_text0 == '/d':    
        b_name = file_name    
    else:    
        b_name = raw_text0



    await editable.edit("**╭━━━━❰ᴇɴᴛᴇʀ ʀᴇꜱᴏʟᴜᴛɪᴏɴ❱━➣\n┣⪼ 144\n┣⪼ 240\n┣⪼ 360\n┣⪼ 480\n┣⪼ 720\n┣⪼ 1080\n╰━━⌈⚡[♛𝕸𝖆𝖓𝖔𝖏 𝕸𝖊𝖊𝖓𝖆♛™~]⚡⌋━━➣ **")   
    input2: Message = await bot.listen(editable.chat.id)    
    raw_text2 = input2.text    
    await input2.delete(True)    
    try:    
        if raw_text2 == "144":    
            res = "144x256"    
        elif raw_text2 == "240":    
            res = "240x426"    
        elif raw_text2 == "360":    
            res = "360x640"    
        elif raw_text2 == "480":    
            res = "480x854"    
        elif raw_text2 == "720":    
            res = "720x1280"    
        elif raw_text2 == "1080":    
            res = "1080x1920"     
        else:     
            res = "UN"    
    except Exception:    
            res = "UN"  



    await editable.edit("**-═════━‧₊˚❀༉‧₊˚.━═════-\nᴇɴᴛᴇʀ ʏᴏᴜʀ ɴᴀᴍᴇ ᴏʀ ꜱᴇɴᴅ `de` ꜰᴏʀ ᴜꜱᴇ ᴅᴇꜰᴀᴜʟᴛ\n-═════━‧₊˚❀༉‧₊˚.━═════-**")    
    input3: Message = await bot.listen(editable.chat.id)    
    raw_text3 = input3.text    
    await input3.delete(True)    
    if raw_text3 == 'de':    
        MR = credit    
    else:    
        MR = raw_text3


    await editable.edit("-═════━‧₊˚❀༉‧₊˚.━═════-\nɴᴏᴡ ꜱᴇɴᴅ ᴛʜᴇ **ᴛʜᴜᴍʙ ᴜʀʟ**\nᴇɢ : `https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2RlbD6RuONW1l8slaNnmmNXyVLsU9WjnFtgEnSOD3URuUkPuNJ-BeNBU58fROeFEPYXE-03edwWbpEyVRgduPbOkIVXyhY08v2Cf7XCBffFpHlIg0pQPW3636ma8TfAnzVn1I-uWNwQ8dgRySl0Y9XvQr0itYneBsP36jFm4V0P1m3O7nwGyOKBYeik43/w320-h160/1000052450.jpg` ᴏʀ ꜱᴇɴᴅ [`no`]\n-═════━‧₊˚❀༉‧₊˚.━═════-")    
    input6 = message = await bot.listen(editable.chat.id)    
    raw_text6 = input6.text
    thumb = input6.text    
    if thumb.startswith("http://") or thumb.startswith("https://"):    
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")    
        thumb = "thumb.jpg"    
    else:    
        thumb == "no"    
    await input6.delete(True)    
    await editable.delete()



    if len(links) == 1:    
        count = 1    
    else:    
        count = int(raw_text)    
    
    try:    
        for i in range(count - 1, len(links)):
            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","m3u8") # .replace("mpd","m3u8")    
            url = "https://" + V
            
            if "visionias" in url:    
                async with ClientSession() as session:    
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                                                         'Accept-Language': 'en-US,en;q=0.9', 
                                                         'Cache-Control': 'no-cache', 
                                                         'Connection': 'keep-alive', 
                                                         'Pragma': 'no-cache', 
                                                         'Referer': 'http://www.visionias.in/', 
                                                         'Sec-Fetch-Dest': 'iframe', 
                                                         'Sec-Fetch-Mode': 'navigate', 
                                                         'Sec-Fetch-Site': 'cross-site', 
                                                         'Upgrade-Insecure-Requests': '1', 
                                                         'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
                                                         'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 
                                                         'sec-ch-ua-mobile': '?1', 
                                                         'sec-ch-ua-platform': '"Android"',}) as resp:    
                        text = await resp.text()    
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
                tokencp ='eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTMxNzkyNDE3LCJvcmdJZCI6NzYxOCwidHlwZSI6MSwibW9iaWxlIjoiOTE2Mzc1MjgyNjY3IiwibmFtZSI6IkphaSBTaHJlZSBSYW0iLCJlbWFpbCI6InBhbmtham1lZW5hNzA2MjQyMzUzNkBnbWFpbC5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOnRydWUsImxvZ2luVmlhIjoiT3RwIiwiZmluZ2VycHJpbnRJZCI6ImRmODRjMGVjOTk5YjliZDE4ZTUwOTA3MTM2MDg5ZWQ3IiwiaWF0IjoxNzM3MTkyMTA5LCJleHAiOjE3Mzc3OTY5MDl9.k6TiHDMn_YdXEv14fvr1Fuy3gVcMOu_o05SEOOZg8fLEsGZXG0A7NRNrHMIeArLs'
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': tokencp}).json()['url']
            
            elif 'media-cdn.classplusapp.com' in url:
                tokencp ='eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MTMxNzkyNDE3LCJvcmdJZCI6NzYxOCwidHlwZSI6MSwibW9iaWxlIjoiOTE2Mzc1MjgyNjY3IiwibmFtZSI6IkphaSBTaHJlZSBSYW0iLCJlbWFpbCI6InBhbmtham1lZW5hNzA2MjQyMzUzNkBnbWFpbC5jb20iLCJpc0ZpcnN0TG9naW4iOnRydWUsImRlZmF1bHRMYW5ndWFnZSI6IkVOIiwiY291bnRyeUNvZGUiOiJJTiIsImlzSW50ZXJuYXRpb25hbCI6MCwiaXNEaXkiOnRydWUsImxvZ2luVmlhIjoiT3RwIiwiZmluZ2VycHJpbnRJZCI6ImRmODRjMGVjOTk5YjliZDE4ZTUwOTA3MTM2MDg5ZWQ3IiwiaWF0IjoxNzM3MTkyMTA5LCJleHAiOjE3Mzc3OTY5MDl9.k6TiHDMn_YdXEv14fvr1Fuy3gVcMOu_o05SEOOZg8fLEsGZXG0A7NRNrHMIeArLs'
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': tokencp}).json()['url']
            
            
            elif "apps-s3-jw-prod.utkarshapp.com" in url:
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
                
                
            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
            
            elif ".pdf" in url:
                url = url.replace(" ","%20")


            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()    
            name = f'{str(count).zfill(3)}) Caption:)™~{name1[:60]}' 
            ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba" 

    
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
  
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'


            try:
  
                cc = f'**[ 🎥 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}\n**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res}):)**.mp4\n\n**<pre>⭐️𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** » **{b_name} </pre>**\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'    
                ccyt = f'**[ 🎥 ] 𝗩𝗜𝗗 𝗜𝗗 : {str(count).zfill(3)}\n**\n**𝐕𝐢𝐝𝐞𝐨 𝐓𝐢𝐭𝐥𝐞** : {name1}**({res}):)**.mp4\n\n**𝐕𝐢𝐝𝐞𝐨 𝐥𝐢𝐧𝐤** -  {url}\n\n**<pre>⭐️𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘** »  **{b_name} </pre>**\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n\n'
                cc1 = f'**[ 📕 ] 𝗣𝗗𝗙 𝗜𝗗 : {str(count).zfill(3)}\n**\n**𝐏𝐝𝐟 𝐓𝐢𝐭𝐥𝐞** : {name1} **:)**.pdf \n\n**<pre>⭐️𝗕𝗔𝗧𝗖𝗛 𝗡𝗔𝗠𝗘:** » **{b_name} </pre>**\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤ {MR}**\n'    
                if "drive" in url:    
                    try:    
                        ka = await helper.download(url, name)    
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)    
                        count+=1    
                        os.remove(ka)    
                        time.sleep(5)    
                    except FloodWait as e:    
                        await m.reply_text(str(e))    
                        time.sleep(e.x)    
                        continue

                elif ".pdf" in url:
                  
                    try:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        os.system(download_cmd)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        count +=1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        os.remove(f'{name}.pdf')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                    except FloodWait as e:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        await m.reply_text(str(e))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        time.sleep(e.x)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
                        continue

                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=photo, caption=ccyt)
                        count +=1
                    except Exception as e:
                        await m.reply_text(str(e))    
                        time.sleep(1)    
                        continue
                     
                else:
                    Show = f"**⚡Dᴏᴡɴʟᴏᴀᴅ Sᴛᴀʀᴛᴇᴅ....**\n\n**📚❰Name❱** `{name}\n🍁𝐐𝐮𝐚𝐥𝐢𝐭𝐲 » {raw_text2}`\n🌿**Url**» ᴘᴀᴅʜᴀɪ ᴋᴀʀ ʟᴇ ʙʀᴏ🧐\n\n **ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ [♛𝕸𝖆𝖓𝖔𝖏 𝕸𝖊𝖊𝖓𝖆♛™]**\n**═════━‧₊˚❀༉‧₊˚.━═════ **"    
                    prog = await m.reply_text(Show)    
                    res_file = await helper.download_video(url, cmd, name)    
                    filename = res_file    
                    await prog.delete(True)    
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)    
                    count += 1    
                    time.sleep(10)
                    
                    
            except Exception as e:
                await m.reply_text(
                    f"**downloading failed [Caption:)™]**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n═════━‧₊˚❀༉‧₊˚.━═════"
                    )
                
    except Exception as e:
        await m.reply_text(e)
        
bot.run()
