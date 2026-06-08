import os

def handle_command(command):

    if command in ["1", "steam"]:
        os.system("steam &")

    elif command in ["2", "heroic"]:
        os.system("heroic &")

    elif command in ["3", "files"]:
        os.system("dolphin &")



    elif command == "help":
        print("""
AVAILABLE COMMANDS

steam      Launch Steam
heroic     Launch Heroic
files      Open File Manager
status     System Status
about      About RobCo-OS
power      Power Menu
version    Show Version
clear      Clear Screen
exit       Exit Shell
""")
        input("Press Enter...")

    elif command == "about":
        print("""
ROBCO-OS ALPHA

Built on:
- Arch Linux
- Hyprland
- Kitty

Project Founder: JPC
""")
        input("Press Enter...")

    elif command == "version":
        print("""
ROBCO-OS ALPHA 0.1

Base System : Arch Linux
Desktop     : Hyprland
Shell       : RobCo Shell
""")
        input("Press Enter...")

    elif command == "status":
        os.system("fastfetch")
        input("Press Enter...")

    elif command == "power":
        print("""
POWER OPTIONS

1. Shutdown
2. Reboot
3. Logout
""")

        choice = input("SELECT OPTION: ")

        if choice == "1":
            os.system("systemctl poweroff")

        elif choice == "2":
            os.system("systemctl reboot")

        elif choice == "3":
            os.system("hyprctl dispatch exit")

    elif command in ["clear", "cls"]:
        return

    elif command in ["exit", "quit"]:
        raise SystemExit

    else:
        print("COMMAND NOT RECOGNIZED")
        input("Press Enter...")
