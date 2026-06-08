import os
import time

from boot import boot
from commands import handle_command

#why cant i do green=green
GREEN = "\033[92m"
RESET = "\033[om"

boot()


print(GREEN)
input("\nPRESS ENTER TO CONTINUE")
print(RESET)

while True:
    os.system("clear")

    print(GREEN)

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
    print()

    command = input("C:\\> ").strip().lower()

    print(RESET)

    handle_command(command)
