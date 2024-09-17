import platform
import psutil
import os
import time
import platform
import colorama
from colorama import Fore
import sys

def animation():
    spinner = ['|', '/', '-', '\\']
    for anim in range(20): 
        for frame in spinner:
            sys.stdout.write(f'\r{frame}')
            sys.stdout.flush()
            time.sleep(0.1)                 

osname = platform.system()
osv = platform.release()
cpu = platform.processor()
cpucores = psutil.cpu_count(logical=True)
mem_info = psutil.virtual_memory()
total_memory = round(mem_info.total / (1024**3), 2) 
available_memory = round(mem_info.available / (1024**3), 2)
disk_info = psutil.disk_usage('/')
total_disk = round(disk_info.total / (1024**3), 2)
used_disk = round(disk_info.used / (1024**3), 2)
    




def main():
    print(f"""{color}
                          _,..,,,_
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
    {Fore.RESET}""")
    print(f"Fetching system info...", animation)
    print(f"OS: {osname} {osv}")
    print(f"CPU: {cpu}")
    print(f"CPU Cores: {cpucores}")
    print(f"Total Memory: {total_memory} GB")
    print(f"Available Memory: {available_memory} GB")
    print(f"Disk: {used_disk} GB used / {total_disk} GB total")
    print(f"Disk usage: {used_disk / total_disk * 100}%")
def colorset():
    os.system('cls && title PyFetch@>')
    print("PyFetch@> Choose a Color :")
    print(f"{Fore.BLUE}b")
    print(f"{Fore.CYAN}c")
    print(f"{Fore.MAGENTA}m")
    print(f"{Fore.RED}r")
    print(f"{Fore.GREEN}g")
    print(f"{Fore.YELLOW}y")
    print(f"{Fore.WHITE}w")
    cinp = input("PyFetch@User>")
    global color;
    if cinp == "b":
        color = Fore.BLUE
        boot()
    elif cinp == "c":
        color = Fore.CYAN
        boot()
    elif cinp == "m":
        color = Fore.MAGENTA
        boot()
    elif cinp == "r":
        color = Fore.RED
        boot()
    elif cinp == "g":
        color = Fore.GREEN
        boot()
    elif cinp == "y":
        color = Fore.YELLOW
        boot()
    elif cinp == "w":
        color = Fore.WHITE
        boot()
    else:
        color = "m" 
    if cinp not in ["b", "c", "m", "r", "g", "y", "w"]:
        print("PyFetch@Error> Invalid Color")
        os.system('cls && title PyFetch@>')
        input("Press Enter to Continue..")
        colorset()
  

def boot():
    os.system('cls && title PyFetch@>')
    main()

colorset()

