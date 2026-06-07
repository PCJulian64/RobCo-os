import os
import time

os.system("clear")

print("ROBCO INDUSTRIES (TM)")
time.sleep(0.5)

print("INITIALIZING SYSTEM...")
time.sleep(1)

print("MEMORY CHECK ........ OK")
time.sleep(0.5)

print("NETWORK ............. OK")
time.sleep(0.5)

print("GRAPHICS ............ OK")
time.sleep(0.5)

print()
print("WELCOME USER")
time.sleep(1)

input("\nPRESS ENTER TO CONTINUE")
commands = {
    "1": "steam",
    "steam": "steam",

    "2": "heroic",
    "heroic": "heroic",

    "3": "files",
    "files": "dolphin",

    "4": "settings",
    "settings": None,

    "5": "shutdown",
    "shutdown": None
}

while True:
    os.system("clear")

    print("=" * 40)
    print("ROBCO INDUSTRIES (TM)")
    print("=" * 40)
    print()
    print("SYSTEM ONLINE")
    print()
    print("1. Steam")
    print("2. Heroic")
    print("3. Files")
    print("4. Settings")
    print("5. Shutdown")
    print()

    command = input("C:\\> ").strip().lower()

    if command in ["1", "steam"]:
        os.system("steam &")

    elif command in ["2", "heroic"]:
        os.system("heroic &")
