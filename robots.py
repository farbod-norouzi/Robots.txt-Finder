import os
from os import system
import requests
import sys
from colorama import Fore
import time
import random
from tqdm import tqdm
import platform 

# Start APP
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

def robots():
    with open('1.txt','r') as f:
        search = f.read().split()

    try:
        print('\n'," [!] Please Enter Target Site Address \n")
        URL = input(" [~>] Enter Your Target : ")
        if 'http' not in URL:
            URL = ('http://'+URL)
        else:
            pass

        time.sleep(5)
        print('\n',"Sacanning URL...")
        time.sleep(15)
        for i in tqdm(range(10)):
    
            pass

        time.sleep(5)
        print('\n',"Search For Robots.txt or robots.txt Files...")
        time.sleep(15)
        for i in tqdm(range(10)):
    
            pass

        for i in search:
            url = (URL+"/"+i)
            reqs = requests.get(url)
            if reqs.status_code == 200 or reqs.status_code == 405:
                time.sleep(5)
                print('\n',"Result:",'\n')
                time.sleep(10)
                print(Fore.GREEN+" [+] "+ url+Fore.RESET)
            else:
                print(Fore.RED+" [-] "+url+Fore.RESET)
        try:
            input(" [!] Press Enter... ")
        except:
            print("")
            sys.exit()
    except:
        print("")
robots()