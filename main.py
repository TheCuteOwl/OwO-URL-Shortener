import requests as rewest
import json

import colorama as UwU
from colorama import Fore, init
UwU.init()
import sys as OxO
import shutil as UnU
import subprocess as subpwocess
import time as timwe


Yellow = Fore.YELLOW
Reset = Fore.RESET

def clear_console():
    if OxO.platform.startswith('win'):
        _ = subpwocess.call('cls', shell=True)
    elif OxO.platform.startswith('linux') or OxO.platform.startswith('darwin'):
        _ = subpwocess.call('clear', shell=True)
    else:
        print('Unsupported platform. Cannot clear console.')

def print_centered(text):
    console_width, _ = UnU.get_terminal_size()
    padding = (console_width - len(text)) // 2
    print(' ' * padding + text)

def input_centered(prompt):
    console_width, _ = UnU.get_terminal_size()
    prompt_lines = prompt.split('\n')
    padding = (console_width - max(len(line) for line in prompt_lines)) // 2
    centered_prompt = '\n'.join(' ' * padding + line for line in prompt_lines)
    user_input = input(centered_prompt)
    return user_input

def Baka():
    url = 'https://owo.vc/generate'
    print_centered(f'Welcome to {Yellow}https://owo.vc/{Reset} link shortener an {Yellow}unoffical{Reset} tool to make {Yellow}URL{Reset} a little bit different')
    choice = input_centered(f'{Yellow}URL{Reset} : {Yellow}->{Reset} ')
    clear_console()
    while True:
        print(f'''Which generator you want to use for the URL?\n
        [{Yellow}1{Reset}] {Yellow}UwU{Reset} {Yellow}Generator{Reset} (Will make the URL like that : {Yellow}https://uwu.owo.vc/ {Reset}
        [{Yellow}2{Reset}] {Yellow}Gay{Reset} {Yellow}Generator{Reset} (Will make the URL like that : {Yellow}https://homosexual.owo.gay/(Some sexuality)/(SomeOtherStuff){Reset}
        [{Yellow}3{Reset}] {Yellow}Sketchy{Reset} {Yellow}Generator{Reset} (Will make the URL like an Scam like {Yellow}https://hzeiofizeh233.net/{Reset}''')
        Generator = input_centered(f'{Yellow}->{Reset}')
        if Generator == '1':
            Generator = 'owo'
        elif Generator == '2':
            Generator = 'gay'
        elif Generator == '3':
            Generator = 'Sketchy'
        else:
            clear_console()
            print(f'{Yellow}Why{Reset}, Choose an {Yellow}real{Reset} thing {Yellow}OnO{Reset}')
            timwe.sleep(1)
            clear_console()
            continue
        
        clear_console()
        while True:
            clear_console()
            print(f'URL : {Yellow}{choice}{Reset}')
            print(f'''
            {Yellow}Do{Reset} you want to {Yellow}prevent{Reset} Scrape ? (Will{Yellow} remove{Reset} embed if set to {Yellow}True{Reset})
            [{Yellow}1{Reset}] {Yellow}True{Reset}
            [{Yellow}2{Reset}] {Yellow}False{Reset}''')
            Scraped = input(f'{Yellow}->{Reset} ')
            if Scraped == '1':
                Scraped = True
            elif Scraped == '2':
                Scraped = False
            else:
                clear_console()
                print(f'{Yellow}Why{Reset}, Choose an {Yellow}real{Reset} thing {Yellow}OnO{Reset}')
                timwe.sleep(1)
                clear_console()
                continue
            while True:
                clear_console()
                print(f'URL : {Yellow}{choice}{Reset}')
                print(f'{Yellow}Prevent{Reset} Scrape : {Yellow}{Scraped}{Reset}')
                
                print(f'''\n{Yellow}Do{Reset} you want to {Yellow}owoify{Reset}
                If set to true {Yellow}embed{Reset} will {Yellow}change{Reset}
                [{Yellow}1{Reset}] - {Yellow}Original{Reset} ({Yellow}False{Reset}) Embed : {Yellow}GitHub{Reset} is where over 100 {Yellow}million{Reset} developers shape the future of software, together.
                [{Yellow}2{Reset}] - {Yellow}Owoify{Reset} ({Yellow}True{Reset}) Embed : {Yellow}GitHub{Reset} is whewe uvw 100 {Yellow}miwwion{Reset} devewopews shape the futuwe of softwawe, togethew.''')
                Owo = input('-> ')
                if Owo == '1':
                    Owo = False
                elif Owo == '2':
                    Owo = True
                else:
                    clear_console()
                    print(f'{Yellow}Why{Reset}, Choose an {Yellow}real{Reset} thing {Yellow}OnO{Reset}')
                    timwe.sleep(1)
                    clear_console()
                    continue
                data = {
                    'link': choice,
                    'generator': Generator,
                    'preventScrape': Scraped,
                    'owoify': Owo
                }

                response = rewest.post(url, json=data)

                if response.status_code == 200:
                    info = response.json()
                    clear_console()
                    print(f'{Yellow}URL{Reset} Generated')
                    print(f'{Reset}https://' + info['result'])
                    input(f'\nPress Any {Yellow}Key{Reset} to {Yellow}leave{Reset} UwU')
                    quit()
                else:
                    clear_console()
                    print(f'{Fore.RED}Error:{Reset}', response.status_code, response.reason)
                    input(f'{Yellow}Error{Reset} may occure when you try to make {Yellow}URL{Reset} shortened when they are already {Yellow}shortened{Reset}, Or if the URL is invalid, Or if you send to {Yellow}many{Reset} rewest')
                    timwe.sleep(3)
                    Baka()


Baka()
