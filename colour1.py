from urllib import response
import mechanize
import os
import datetime
import getpass
import time
import sys, requests
from time import sleep
browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36')]
browser.set_handle_refresh(False)



url = 'https://m.facebook.com/login'



def clear():

    if os.name == 'nt':

        os.system('cls')

    else:

        os.system('xdg-open https://www.facebook.com/100087513362848')



def sp(stri):

    for letter in stri:

        print(letter, end = "")

        sys.stdout.flush()

        sleep(0.03)


os.system('clear')
logo ="""             \033[1;32m𝗪𝗘𝗟𝗖𝗢𝗠𝗘 \033[1;32m𝗧𝗢 \033[1;32m𝗦𝗔𝗧𝗜𝗦𝗛 \033[1;32m𝗧𝗢𝗢𝗟𝗦


\033[1;36m _       __________    __________  __  _________
\033[1;31m| |     / / ____/ /   / ____/ __ \/  |/  / ____/
\033[1;32m| | /| / / __/ / /   / /   / / / / /|_/ / __/   
\033[1;31m| |/ |/ / /___/ /___/ /___/ /_/ / /  / / /___   
\033[1;36m|__/|__/_____/_____/\____/\____/_/  /_/_____/   
                                                
                           
             \033[1;31m𝗛𝗔𝗧𝗘𝗥𝗦 \033[1;32m𝗖𝗔𝗟𝗟 \033[1;33m𝗠𝗘 \033[1;34m𝗣𝗔𝗣𝗔

\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0;92m
 \033[1;31m███████╗ █████╗ ████████╗██╗███████╗██╗  ██╗
 \033[1;32m██╔════╝██╔══██╗╚══██╔══╝██║██╔════╝██║  ██║
 \033[1;33m███████╗███████║   ██║   ██║███████╗███████║
 \033[1;34m╚════██║██╔══██║   ██║   ██║╚════██║██╔══██║
 \033[1;35m███████║██║  ██║   ██║   ██║███████║██║  ██║
 \033[1;36m╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝╚══════╝╚═╝  ╚═╝
\033[0;92m
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[1;39m━▷ \033[0;91m𝙊𝙒𝙉𝙀𝙍     \033[1;39m◈✙◈  \033[1;33m𝐌𝐫.𝐒𝐀𝐓𝐈𝐒𝐇
\033[1;39m━▷ \033[0;91m𝙔𝙊𝙐𝙏𝙐𝘽𝙀   \033[1;39m◈✙◈  \033[1;32mSatish 62 Channel
\033[1;39m━▷ \033[0;91m𝙎𝘼𝙏𝙐𝙏𝘼𝙎   \033[1;39m◈✙◈  \033[0;92mFree And Enjoy
\033[1;39m━▷ \033[0;91m𝙑𝙀𝙍𝙎𝙄𝙊𝙉   \033[1;39m◈✙◈  \033[1;37m4.0
\033[1;39m━▷ \033[0;91m𝗪𝗔𝗧𝗦𝗔𝗣𝗣   \033[1;39m◈✙◈  \033[1;31m62687*****
\033[1;39m━▷ \033[1;36m𝗠𝗔𝗭𝗔 𝗡𝗔 𝗔𝗔𝗬𝗘 𝗧𝗢 𝗣𝗔𝗜𝗦𝗘 𝗩𝗔𝗣𝗔𝗦
\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[1;37m๑۩♡۩๑\033[0;95m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●"""
os.system('clear')
logo2 ="""\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑
\033[1;37mWELCOME TO SATISH TOOL

\033[1;31m
 _       __________    __________  __  _________
| |     / / ____/ /   / ____/ __ \/  |/  / ____/
| | /| / / __/ / /   / /   / / / / /|_/ / __/   
| |/ |/ / /___/ /___/ /___/ /_/ / /  / / /___   
|__/|__/_____/_____/\____/\____/_/  /_/_____/   
                                                



\033[1;32m
  __________ 
 /_  __/ __ \
  / / / / / /
 / / / /_/ / 
/_/  \____/  
             

 
 
\033[1;33m   _____ ___  _______________ __  __
  / ___//   |/_  __/  _/ ___// / / /
  \__ \/ /| | / /  / / \__ \/ /_/ / 
 ___/ / ___ |/ / _/ / ___/ / __  /  
/____/_/  |_/_/ /___//____/_/ /_/   
                                    


\033[1;35m
  __________  ____  __   _____
 /_  __/ __ \/ __ \/ /  / ___/
  / / / / / / / / / /   \__ \ 
 / / / /_/ / /_/ / /______/ / 
/_/  \____/\____/_____/____/  
                              

 
 \033[1;31mOWNER \033[1;32mTOOL \033[1;33mOF \033[1;37mMr. \033[1;35mSATISH

\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑"""
def approval():
  os.system('git pull')
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = "SATISH-TOOLS:-"+"".join(uuid)
  os.system('clear')

  print(logo)
  sp("\033[1;39m━▷ You Get Approved for Using Command  Paid Tool 350 Per month \033[1;37m")
  print("\n\033[1;39m━▷ Your Key :\u001b[36m "+id)
  print ("""\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑""")

  try:
    httpCaht = requests.get('https://github.com/satishboss/boss/blob/main/satish.txt').text
    if id in httpCaht:
      sp("\n\033[1;39m━▷ Congrats You get approved successful And Enjoy")
      msg = str(os.geteuid())     
      pass
    else: 
      sp("\n\033[1;39m━▷ Your Key Not approved please  Say to Admin");    
      input('\n\nWHEN YOU BUY TOOL THEN ENTER PRESS')
      tks = ('Hello%20Satish%20Sir%20!%20Please%20Approve%20My%20Key%20This%20My%20Key%20:%20'+id);os.system('am start https://wa.me/+916268781574?text='+tks),approval()
      time.sleep(2)
      exit()
  except Exception as e:
     print(e)
     sp(" >> Unable Data From Server ")
     time.sleep(2)
     approval()
  except:
    sys.exit()
    
approval()

os.system('clear')




# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "🔴🔴"
    else:
        return "🟢🟢"

# Get three different numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Calculate the sum, product, and maximum of the three numbers
total = num1 + num2 - num3 % num1 * num2
product = num1 + num2 - num3 % num1 * num2
maximum = max(num1, num2, num3)

# Determine the color based on the sum
color = check_even_odd(total)

# Print the heading
print("\nCOLOR SCRIPT BY PARTH")
print("=" * 20)

# Print the results
print(f"THIS SCRIPT IS NOT 100% SURE")
print(f"PLAY AT OWN RISK")
print(f"ONLY PLAY 3-5 PERIOD AT A TIME")

# Display the color based on the sum
print(f"The color is {color}")

# Display the note
print("\nTHIS SCRIPT IS NOT 100% SURE. PLAY WITH AT LEAST 7 LEVELS OF FUNDS")