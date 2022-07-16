import os,time,sys
from cryptography.fernet import Fernet
from tkinter import filedialog as fd
key = None
class col:
    RED = "\u001b[31m"
    BLUE = "\u001b[34m"
    GREEN = "\u001b[38;5;77m"
    YELLOW = "\u001b[33m" # Yellow in Windows, Orange in Linux
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    ORANGE = "\u001b[38;5;208m"
    BOLD = "\u001b[1m"
    UNDERLINE = "\u001b[4m"
    RESET = "\u001b[0m"
os.system('color')

def loading():
   for i in range(0,100):
    time.sleep(0.05)
    sys.stdout.write("\r{:>3}%\u2502{:<98}\u2502".format("Decrypting " + str(i + 1), "\u2588" * i)),"\n"
    sys.stdout.flush()


def key_input():
    global key
    key = input(f"{col.GREEN}Enter Your Decryption Key :\n{col.BLUE}")
    if len(key) != 44 or key[-1] != '=':
        os.system('cls')
        print(f'{col.RED}Invalid Key')
        key_input()
key_input()

key = str(key).encode()
fernet_gen =Fernet(key)

print(f"{col.GREEN}Select The Zip(s) You Wish To Decrypt")
files_path = fd.askopenfilenames(filetypes=[("Archives",'.zip')])
if len(files_path) == 0:
    print(f'{col.RED}Operation Was Cancelled By User')
    time.sleep(1)
    exit()
for i in files_path:
    if 'All_Data' in i:
        file = open(i,"rb+")
        contents = file.read()
        loading()
        try:
            decrypting = fernet_gen.decrypt(contents)
            file.truncate(0)
            file.seek(0)
            file.write(decrypting)
        except Exception:
            print(f'{col.RED}An Error Occured Whne Attempting To Decrypt{col.YELLOW}[{i}]')
        file.close()
        print(f'{col.GREEN}\nSuccesfully Decrypted {col.YELLOW}[{i}]')
    else:
        print(f"{col.RED}Ignoring {col.YELLOW}[{i}]{col.CYAN}\nIf This Is The Right Archive Rename It To It's Original Name\n{col.RED}Otherwise Your Files Could Be Damaged")


