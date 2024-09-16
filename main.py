import platform
import psutil
import os
import time
import platform
import colorama
from colorama import Fore

osname = platform.system()
osv = platform.release()


def display():








def main():
    def asciiw():
        if  osname =='Windows':
            print(f""" 
                               .oodMMMM
                      .oodMMMMMMMMMMMMM
          ..oodMMM  MMMMMMMMMMMMMMMMMMM
    oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
    `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
          ````^^^^  ^^MMMMMMMMMMMMMMMMM
                         ````^^^^^^MMMM
    {Fore.RESET}""")
    def asciiw():
        if  osname =='Darwin':
            print(f"""
─────────▄────
───────▐█▌────
───▄▄▄─▀─▄▄▄──
─▄█████▄█████▄
▐███████████▀─
▐██████████───
─███████████▄─
──███████████▀
───▀██▀─▀██▀──
──────────────
    {Fore.RESET}""") 
    def asciiw():
        if  osname =='Windows':
            print(f"""
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' hjm
    {Fore.RESET}""")
    

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
    if cinp == "b":
        color = Fore.BLUE
    elif cinp == "c":
        color = Fore.CYAN
    elif cinp == "m":
        color = Fore.MAGENTA
    elif cinp == "r":
        color = Fore.RED
    elif cinp == "g":
        color = Fore.GREEN
    elif cinp == "y":
        color = Fore.YELLOW
    elif cinp == "w":
        color = Fore.WHITE
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







'''
import platform
import psutil
import os

# Function to display ASCII art (you can modify it as needed)
def display_ascii_art():
    art = """
     _____  _                 _   
    |  ___|| |               | |  
    | |__  | |_   __ _  _ __ | |_ 
    |  __| | __| / _` || '__|| __|
    | |___ | |_ | (_| || |   | |_ 
    \____/  \__| \__,_||_|    \__|
    """
    print(art)

# Function to display system information
def display_system_info():
    print("Fetching system info...\n")
    
    # OS Info
    os_info = platform.system()
    os_version = platform.release()
    print(f"OS: {os_info} {os_version}")
    
    # CPU Info
    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=True)
    print(f"CPU: {cpu_info} ({cpu_count} cores)")

    # Memory Info
    mem_info = psutil.virtual_memory()
    total_memory = round(mem_info.total / (1024**3), 2)  # Convert from bytes to GB
    available_memory = round(mem_info.available / (1024**3), 2)
    print(f"Memory: {available_memory} GB available / {total_memory} GB total")

    # Disk Usage Info
    disk_info = psutil.disk_usage('/')
    total_disk = round(disk_info.total / (1024**3), 2)
    used_disk = round(disk_info.used / (1024**3), 2)
    print(f"Disk: {used_disk} GB used / {total_disk} GB total")

    # Uptime
    uptime = psutil.boot_time()
    print(f"Uptime: {uptime:.2f} seconds")

def main():
    display_ascii_art()
    display_system_info()

if __name__ == "__main__":
    main()

'''
