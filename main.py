from dhooks import Webhook, Embed
from pystyle import Colors, Colorate, Center
import os
import time
from datetime import datetime
from time import sleep
from colorama import Fore
from random import randint
import requests
__author__ = "dynasty"
__github__ = "https://github.com/j0taro/webhook-spammer-deleter"
wise = '"Invalid Webhook Token"'
haha = '"Unknown Webhook"'
fr = Center.XCenter(''' 
███████╗██████╗░  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
█████╗░░██████╔╝  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝ 
by: dynasty
github: https://github.com/j0taro/webhook-spammer-deleter \n\n''')
 

shit = '''
[1] webhook spammer
[2] webhook deleter idc 
[3] Token checker
[4] Token info
[5] webhook checker'''
def main():
    os.system('cls')
    print(Colorate.Vertical(Colors.blue_to_red,fr+shit))
    ye = input(Colors.blue + 'select >: ')
    if ye == '1':
     print(f"{Fore.RED}Press CTRL+C to Exit when finished with the Spammer!")
     time.sleep(1.3)
     webhook = input("webhook url >: ")
     oak = webhook
     try:
      tree = requests.get(oak)
      if wise in tree.text or haha in tree.text or 'discord.com/api/webhooks' not in webhook:
       print('invaild webhook fr')
       os.system("pause")
       main()
      else:
       print(f'{Fore.GREEN}vaild webhook fr')
       ong = input("Message >: ")
       count = 1
       while True:
        lmao = requests.post(webhook, json={'content': ong}, headers={'Content-Type': 'application/json'})
        if lmao.status_code == 204 or lmao.status_code == 200:
                print(f"{Fore.GREEN}[+] Sent {ong} [{count}]")
                count += 1
        elif lmao.status_code == 429:
                print(f"{Fore.RED}rate limited fr ({lmao.json()['retry_after'] / 1000}s){Fore.RESET}")
                sleep(lmao.json()["retry_after"] / 1000)

     except Exception as e:
       print(e)
       print('invaild webhook')
       os.system("pause")
       main()
            
    if ye == '2':
     webhook = input("webhook url >: ")
     oak = webhook
     try:
      tree = requests.get(oak)
      if wise in tree.text or haha in tree.text or 'discord.com/api/webhooks' not in webhook:
       print('invaild webhook fr')
       os.system("pause")
       main()
      else:
       print(f'{Fore.GREEN}vaild webhook fr')
       requests.delete(webhook)
       print(f"{Fore.GREEN}webhook deleted fr")
       time.sleep(3)
       main()
     except Exception as e:
      print('invaild webhook')
      os.system("pause")
      main()
    if ye == '3':
     token()
    if ye == '4':
      token2()
    if ye == '5':
     webhook = input('webhook url >:') #token checker by dynasty https://github.com/j0taro/webhook-checker
     wise = '"Invalid Webhook Token"'
     haha = '"Unknown Webhook"'
     oak = webhook
     try:
      tree = requests.get(oak)
      if wise in tree.text or haha in tree.text or 'discord.com/api/webhooks' not in webhook:
       os.system('cls')
       print('invaild webhook fr')
       input("Press Enter to continue...")
       main() 
      else:
       os.system('cls')
       print('vaild webhook fr')
       input("Press Enter to continue...")
       main() 
     except Exception as e:
      os.system('cls')
      print('invaild webhook')
      input("Press Enter to continue...")
      main() 

    
    else:
     print('invaild option please try again')
     time.sleep(3)
     main()
 

def token():
    a1 = input('Token >: ')
    f = a1
    token = f.replace('"','')
    print(f'{Fore.GREEN}Checking '+token)    
    headers = {'Authorization':token}
    r = requests.get(f"https://discord.com/api/v6/auth/login", headers=headers)
    status = r.status_code
    if r.status_code == 200:
                print(f'{Fore.WHITE}[{Fore.LIGHTGREEN_EX} SUCCESS {Fore.RESET}]: {Fore.RED} token vaild fr')
                time.sleep(5)
                main()
    if "You need to verify your account in order to perform this action." in r.text:
                print(f'{Fore.WHITE}[{Fore.LIGHTRED_EX} ERROR {Fore.RESET}]: {Fore.BLUE} token locked lol')    
                time.sleep(5)
                main()
    else:
                 
                print(f'{Fore.WHITE}[{Fore.LIGHTRED_EX} ERROR {Fore.RESET}]: {Fore.RED} token invaild ')    
                time.sleep(5)
                main()


def token2():
    a1 = input('Token >: ')
    f = a1
    token = f.replace('"','')
    os.system('cls')
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
    }

    cc_digits = {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

    try:
        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    except:
        input(f"""          [{Fore.RED }ERROR""")
        main()

    if res.status_code == 200:
        res_json = res.json()
        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
        user_id = res_json['id']
        avatar_id = res_json['avatar']
        avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
        phone_number = res_json['phone']
        email = res_json['email']
        mfa_enabled = res_json['mfa_enabled']
        flags = res_json['flags']
        locale = res_json['locale']
        verified = res_json['verified']
        
        language = languages.get(locale)
        from datetime import datetime
        creation_date = datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
        nitro_data = res.json()
        has_nitro = bool(len(nitro_data) > 0)

        if has_nitro:
            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
            days_left = abs((d2 - d1).days)
        billing_info = []

        for x in requests.get('https://discordapp.com/api/v6/users/@me/billing/payment-sources', headers=headers).json():
            yy = x['billing_address']
            name = yy['name']
            address_1 = yy['line_1']
            address_2 = yy['line_2']
            city = yy['city']
            postal_code = yy['postal_code']
            state = yy['state']
            country = yy['country']

            if x['type'] == 1:
                cc_brand = x['brand']
                cc_first = cc_digits.get(cc_brand)
                cc_last = x['last_4']
                cc_month = str(x['expires_month'])
                cc_year = str(x['expires_year'])
                
                data = {
                    'Payment Type': 'Credit Card',
                    'Valid': not x['invalid'],
                    'CC Holder Name': name,
                    'CC Brand': cc_brand.title(),
                    'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                    'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            elif x['type'] == 2:
                data = {
                    'Payment Type': 'PayPal',
                    'Valid': not x['invalid'],
                    'PayPal Name': name,
                    'PayPal Email': x['email'],
                    'Address 1': address_1,
                    'Address 2': address_2 if address_2 else '',
                    'City': city,
                    'Postal Code': postal_code,
                    'State': state if state else '',
                    'Country': country,
                    'Default Payment Method': x['default']
                }

            billing_info.append(data)

        print(f"""\nBasic Information:""")
        print(f"""          Username: {user_name}""")
        print(f"""          User ID: {user_id}""")
        print(f"""          Creation Date: {creation_date}""")
        print(f"""          Avatar URL: {avatar_url if avatar_id else ""}""")
        print(f"""          Token: {token}""")
        
        print(f"""Nitro Information:""")
        print(f"""           Nitro Status: {has_nitro}""")

        if has_nitro:
            print(f"""           Expires in: {days_left} day(s)""")
        else:
            print(f"""           Expires in: None day(s)""")

        print(f"""Contact Information:""")
        print(f"""           Phone Number: {phone_number if phone_number else ""}""")
        print(f"""           Email: {email if email else ""}""")

        if len(billing_info) > 0:
            print(f"""Billing Information:""")
            if len(billing_info) == 1:
                for x in billing_info:
                    for key, val in x.items():
                        if not val:
                            continue
                        print(Fore.RESET + '    {:<23}{}{}'.format(key, Fore.CYAN, val))

            else:
                for i, x in enumerate(billing_info):
                    title = f'Payment Method {i + 1} ({x["Payment Type"]})'
                    print('    ' + title)
                    print('    ' + ('=' * len(title)))
                    for j, (key, val) in enumerate(x.items()):
                        if not val or j == 0:
                            continue
                        print(Fore.RESET + '        {:<23}{}{}'.format(key, Fore.CYAN, val))

                    if i < len(billing_info) - 1:
                        print(' ')

            print(' ')

        print(f"""Account Security:""")
        print(f"""           2FA/MFA Enabled: {mfa_enabled}""")
        print(f"""           Flags: {flags}""")
        print(f"""           Other:""")
        print(f"""           Locale: {locale} ({language})""")
        print(f"""           Email Verified: {verified}""")

    elif res.status_code == 401:
        print(f"""{Fore.LIGHTRED_EX }Invalid token""")
        time.sleep(2)
        main()

    else:
        input(f"""[{Fore.LIGHTRED_EX }An error occurred while sending request""")
        main()
    
    input(f""" Press ENTER to exit""")
    main()


main()
