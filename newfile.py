import requests
import telebot
from telebot import types
from gatet import Tele 
token = '7097192708:AAEABr3ozy3rG75wOJaIWVcByXyZhkWPmnI'
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,"𝙎𝙀𝙉𝘿 𝘾𝘾 𝘾𝙊𝙈𝘽𝙊 𝙁𝙄𝙇𝙀")
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "𝘾𝙃𝙀𝘾𝙆𝙄𝙉𝙂 𝙔𝙊𝙐𝙍 𝘾𝘼𝙍𝘿❜𝙎...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"• 𝗖𝗛𝗔𝗥𝗚𝗘𝗗 💲: [ {ch} ] •", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"• 𝗟𝗜𝗩𝗘 ✅ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗔𝗗 ❌ : [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 : [ {total} ] •", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm5)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝙒𝘼𝙄𝙏 𝘾𝘼𝙍𝘿❜𝙎 𝘼𝙍𝙀 𝙋𝙍𝙊𝘾𝙀𝙎𝙎𝙄𝙉𝙂, 𝙈𝘼𝘿𝙀 𝘽𝙔 ➜ @f79XmO3MKtYZUW5 ''', reply_markup=mes)
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						last = "YOUR CARD WAS DECLINED."
				
				msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ #LIVE
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 13$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @f79XmO3MKtYZUW5
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				print(last)
				if "cvc" in last:
					bot.reply_to(message, msg)
					live += 1
				elif "funds" in last:
					live += 1
					bot.reply_to(message, msg)
				elif "live" in last:
					ch += 1
					msg1 = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc}
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑈𝑪𝑪𝐸𝑆𝑆
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 13$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @f79XmO3MKtYZUW5
◆ 𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
					bot.reply_to(message, msg)
				else:
					dd += 1
	except:
		pass
print("تم تشغيل البوت")
bot.polling()
