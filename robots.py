# Start (Import libraries)

import os
from os import system
import time
import platform 
import sys
try:
    import requests
    from colorama import Fore
    import random
    from tqdm import tqdm
except:
   print("Installing prerequisites")
   system("pip install colorama ")
   system("pip install requests")
   system("pip install ipapi")
   system("pip install datetime")
   exit('\n',"Run script Again")

# End (Import libraries)

# Start (Banner & Clearing)

def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED +"""
######                                                           
#     #  ####  #####   ####  #####  ####      ##### #    # ##### 
#     # #    # #    # #    #   #   #            #    #  #    #   
######  #    # #####  #    #   #    ####        #     ##     #   
#   #   #    # #    # #    #   #        # ###   #     ##     #   
#    #  #    # #    # #    #   #   #    # ###   #    #  #    #   
#     #  ####  #####   ####    #    ####  ###   #   #    #   # """+Fore.RESET)

# End (Banner & Clearing)

# Start (Search For URL & 1.txt file)

def robots():
    with open('1.txt','r') as f:
        search = f.read().split()

    try:
        print('\n',"[*] Please Enter Target Site Address \n")
        URL = input(" [>] Enter Your Target : ")
        if 'http' not in URL:
            URL = ('http://'+URL)
        else:
            pass

# End (Search For URL & 1.txt file)

# Start (Progress bar)

        time.sleep(3)
        print('\n',"Scanning URL...")
        time.sleep(7)
        for i in tqdm(range(10)):
    
            pass

        time.sleep(3)
        print('\n',"Search For Robots.txt or robots.txt Files...")
        time.sleep(7)
        for i in tqdm(range(10)):

            pass

        time.sleep(3)
        print('\n',"Search For Directory's...")
        time.sleep(7)
        for i in tqdm(range(10)):

            pass

# End (Progress bar)

# Start (Search Directory)

        for i in search:
            url = (URL+"/"+i)
            reqs = requests.get(url)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(Fore.GREEN+'\n'," [+] "+ url+Fore.RESET)
            else:
                print(Fore.RED+'\n'," [-] "+url+Fore.RESET)
        try:
            print('\n',"All files and directories were checked!")
            input(" [!] Press Enter... ")
        except:
            print("Someting Went Wrong")
            sys.exit()
    except:
        print("")
robots()

# End (Search Directory)