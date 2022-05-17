# Check the requirements

try:
    import requests
    from os import system
    import sys
    from colorama import Fore
    import os
    import time
    import random
    from tqdm import tqdm
except ImportError:
    system("pip install os ")
    system("pip install colorama ")
    system("pip install time ")
    system("pip install random ")
    system("pip install tqdm ")
    system("pip install sys ")
    system("pip install requests ")
    
#Start APP

os.system("cls")
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