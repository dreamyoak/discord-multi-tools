from dhooks import Webhook, Embed
from pystyle import Colors, Colorate, Center
import os
import time
from colorama import Fore
import requests
author = 'dynasty'
github = 'https://github.com/j0taro/webhook-spammer-deleter'
wise = '"Invalid Webhook Token"'
haha = '"Unknown Webhook"'
fr = Center.XCenter(''' 
███████╗██████╗░  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
█████╗░░██████╔╝  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██╔══╝░░██╔══██╗  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██║░░░░░██║░░██║  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═╝░░░░░╚═╝░░╚═╝  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝ \n\n\n''')
shit = '''
[1] webhook spammer
[2] webhook deleter idc '''
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
      tree = requests.get(oak) #webhook checker -> https://github.com/j0taro/webhook-checker
      if wise in tree.text or haha in tree.text:
       print('invaild webhook fr')
       os.system("pause")
       main()
      else:
       print(f'{Fore.GREEN}vaild webhook fr')
       ong = input("Message >: ")
       while True:
        lmao = requests.post(webhook, json={'content': ong}, headers={'Content-Type': 'application/json'})
        if lmao.status_code == 204:
            print(f"{Fore.GREEN}[+] Sent {ong}")
     except:
      print('invaild webhook')
      os.system("pause")
      main()
            
    if ye == '2':
     webhook = input("webhook url >: ")
     oak = webhook
     try:
      tree = requests.get(oak)
      if wise in tree.text or haha in tree.text:
       print('invaild webhook fr')
       os.system("pause")
       main()
      else:
       print(f'{Fore.GREEN}vaild webhook fr')
       requests.delete(webhook)
       print(f"{Fore.GREEN}webhook deleted fr")
       time.sleep(3)
       main()
     except:
      print('invaild webhook')
      os.system("pause")
      main()
    else:
     print('invaild option please try again')
     time.sleep(3)
     main()
main()
