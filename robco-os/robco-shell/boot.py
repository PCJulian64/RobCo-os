import time
import os

GREEN = "\033[92m"
RESET = "\033[0m"

def boot():
    os.system("clear")

    print(GREEN)

    print("ROBCO INDUSTRIES (TM)")
    time.sleep(0.5)

    print("\nINITIALIZING SYSTEM...")
    time.sleep(1)

    print("MEMORY CHECK ........ OK")
    time.sleep(0.5)

    print("NETWORK ............. OK")
    time.sleep(0.5)

    print("GRAPHICS ............ OK")
    time.sleep(0.5)

    print("AUDIO ............... OK")
    time.sleep(0.5)

    print("\nWELCOME USER")

    print(RESET)

    time.sleep(1)
