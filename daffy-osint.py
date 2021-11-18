#!/usr/bin/python

import os
import sys
d3 = os.system('curl http://ipinfo.io/ip')
os.system('clear && clear && clear')
logo = \
    '''
                   
███████╗ █████╗ ██████╗ ████████╗██╗  ██╗██╗   ██╗      ██████╗ ███████╗██╗███╗   ██╗████████╗
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██║  ██║╚██╗ ██╔╝     ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
█████╗  ███████║██████╔╝   ██║   ███████║ ╚████╔╝█████╗██║   ██║███████╗██║██╔██╗ ██║   ██║   
██╔══╝  ██╔══██║██╔══██╗   ██║   ██╔══██║  ╚██╔╝ ╚════╝██║   ██║╚════██║██║██║╚██╗██║   ██║   
███████╗██║  ██║██║  ██║   ██║   ██║  ██║   ██║        ╚██████╔╝███████║██║██║ ╚████║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝         ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝                                                                                                                                        
                    \033[0m  \033[92m    \033[1m 
        earthy-OSINT tool for Information Gathering
            Author By Sive
        Github: https://github.com/sivesa 
     '''
menu = \
    '''\033[0m
     (1) Whois
     (2) Traceroute
     (3) DNS
     (4) Reverse DNS
     (5) GeoIP Lookup
     (6) Port Scan
     (7) Reverse IP 
     (0) Exit                                                                                                                   
 '''
print(logo)
print(menu)


def quit():
    con = input('Continue [Y/n] -> ')
    if (con[0].upper() == 'N' or con[0] == 'n'):
        exit()
    else:
        os.system('clear')
        print (logo)
        print (menu)
        selection()


def selection():
    try:
        choice = int(input('[earthy-OSINT~]$ '))
        if choice == 0:
            os.system('clear')
            print('Good bye...')
        elif choice == 1:
            whois_lookup()
        elif choice == 2:
            tracroute()
        elif choice == 3:
            dnslookup()
        elif choice == 4:
            reverse_dns()
        elif choice == 5:
            geo_lookup()
        elif choice == 6:
            port_scan()
        elif choice == 7:
            reverse_ip()
    except KeyboardInterrupt:
        print ('')


def whois_lookup():
    d3 = input('Enter IP Or Domain (e.g. 127.0.0.1 or facebook.com) : ')
    print(d3)
    os.system('clear')
    print ("""
 __     __     __  __     ______     __     ______    
/\ \  _ \ \   /\ \_\ \   /\  __ \   /\ \   /\  ___\   
\ \ \/ ".\ \  \ \  __ \  \ \ \/\ \  \ \ \  \ \___  \  
 \ \__/".~\_\  \ \_\ \_\  \ \_____\  \ \_\  \/\_____\ 
  \/_/   \/_/   \/_/\/_/   \/_____/   \/_/   \/_____/ 
  """)
    os.system('whois -v ' + d3)
    print ('')
    quit()


def tracroute():
    d3 = input('Enter IP Or Domain : ')
    os.system('clear')
    print ("""
 ______   ______     ______     ______     ______     ______     ______     __  __     ______   ______    
/\__  _\ /\  == \   /\  __ \   /\  ___\   /\  ___\   /\  == \   /\  __ \   /\ \/\ \   /\__  _\ /\  ___\   
\/_/\ \/ \ \  __<   \ \  __ \  \ \ \____  \ \  __\   \ \  __<   \ \ \/\ \  \ \ \_\ \  \/_/\ \/ \ \  __\   
   \ \_\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\    \ \_\  \ \_____\ 
    \/_/   \/_/ /_/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/   \/_____/   \/_____/     \/_/   \/_____/ 
    """)
    os.system('traceroute -4 ' + d3)
    print ('')
    quit()

def dns_lookup():
    d3 = input('Enter Domain : ')
    os.system('clear')
    print ("""
 _____     __   __     ______     __         ______     ______     __  __     __  __     ______  
/\  __-.  /\ "-.\ \   /\  ___\   /\ \       /\  __ \   /\  __ \   /\ \/ /    /\ \/\ \   /\  == \ 
\ \ \/\ \ \ \ \-.  \  \ \___  \  \ \ \____  \ \ \/\ \  \ \ \/\ \  \ \  _"-.  \ \ \_\ \  \ \  _-/ 
 \ \____-  \ \_\\"\_\  \/\_____\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\   
  \/____/   \/_/ \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/   
  """)
    os.system('curl http://api.hackertarget.com/dnslookup/?q='+ d3)
    print ('')
    quit()

def reverse_dns():
    d3 = input('Enter IP Address - IP Range Or Domain  : ')
    os.system('clear')
    print ("""
 ______     ______     __   __   ______     ______     ______     ______        _____     __   __     ______    
/\  == \   /\  ___\   /\ \ / /  /\  ___\   /\  == \   /\  ___\   /\  ___\      /\  __-.  /\ "-.\ \   /\  ___\   
\ \  __<   \ \  __\   \ \ \'/   \ \  __\   \ \  __<   \ \___  \  \ \  __\      \ \ \/\ \ \ \ \-.  \  \ \___  \  
 \ \_\ \_\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\     \ \____-  \ \_\\"\_\  \/\_____\ 
  \/_/ /_/   \/_____/   \/_/      \/_____/   \/_/ /_/   \/_____/   \/_____/      \/____/   \/_/ \/_/   \/_____/ 
  """)
    os.system('curl https://api.hackertarget.com/reversedns/?q='+ d3)
    print ('')
    quit()

def geo_lookup():
    d3 = input('Enter IP Or Domain : ')
    os.system('clear')
    print ("""
 ______     ______     ______     __     ______      __         ______     ______     __  __     __  __     ______  
/\  ___\   /\  ___\   /\  __ \   /\ \   /\  == \    /\ \       /\  __ \   /\  __ \   /\ \/ /    /\ \/\ \   /\  == \ 
\ \ \__ \  \ \  __\   \ \ \/\ \  \ \ \  \ \  _-/    \ \ \____  \ \ \/\ \  \ \ \/\ \  \ \  _"-.  \ \ \_\ \  \ \  _-/ 
 \ \_____\  \ \_____\  \ \_____\  \ \_\  \ \_\       \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\   
  \/_____/   \/_____/   \/_____/   \/_/   \/_/        \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/   
  """)
    os.system('curl http://api.hackertarget.com/geoip/?q=' + d3)
    print ('')
    print ('')
    quit()

def port_scan():
    d3 = input('Enter IP Or Domain : ')
    os.system('clear')
    print ("""
 ______   ______     ______     ______      ______     ______     ______     __   __    
/\  == \ /\  __ \   /\  == \   /\__  _\    /\  ___\   /\  ___\   /\  __ \   /\ "-.\ \   
\ \  _-/ \ \ \/\ \  \ \  __<   \/_/\ \/    \ \___  \  \ \ \____  \ \  __ \  \ \ \-.  \  
 \ \_\    \ \_____\  \ \_\ \_\    \ \_\     \/\_____\  \ \_____\  \ \_\ \_\  \ \_\\"\_\ 
  \/_/     \/_____/   \/_/ /_/     \/_/      \/_____/   \/_____/   \/_/\/_/   \/_/ \/_/ 
  """)
    os.system('curl http://api.hackertarget.com/nmap/?q=' + d3)
    print ('')
    quit()

def reverse_ip():
    d3 = input('Enter IP Or Domain : ')
    os.system('clear')
    print ("""
 ______     ______     __   __   ______     ______     ______     ______        __     ______  
/\  == \   /\  ___\   /\ \ / /  /\  ___\   /\  == \   /\  ___\   /\  ___\      /\ \   /\  == \ 
\ \  __<   \ \  __\   \ \ \'/   \ \  __\   \ \  __<   \ \___  \  \ \  __\      \ \ \  \ \  _-/ 
 \ \_\ \_\  \ \_____\  \ \__|    \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\     \ \_\  \ \_\   
  \/_/ /_/   \/_____/   \/_/      \/_____/   \/_/ /_/   \/_____/   \/_____/      \/_/   \/_/   
  """)
    os.system('wget http://api.hackertarget.com/reverseiplookup/?q='
                + d3)
    os.system('clear')
    os.system('curl http://api.hackertarget.com/reverseiplookup/?q='
                + d3)
    print ('')
    print ("\033[91m\033[1mFile Saved On : ")
    os.system('pwd')
    print ('File : index.html?q=' + d3)
    print ("\033[0m")
    quit()

selection()
