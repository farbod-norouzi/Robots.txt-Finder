import requests
import sys

def robots():
    with open('1.txt','r') as f:
        search = f.read().split()

    try:
        print(" [!] Please Enter Target Site Address \n")
        URL = input("Enter Your Target : ")
        if 'http' not in URL:
            URL = ('http://'+URL)
        else:
            pass

        for i in search:
            url = (URL+"/"+i)
            reqs = requests.get(url)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(" [+] "+ url)
            else:
                print(" [-] "+url)
        try:
            input(" [!] Press Enter... ")
        except:
            print("")
            sys.exit()
    except:
        print("")
robots()