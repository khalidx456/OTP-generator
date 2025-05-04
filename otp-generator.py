from termcolor import colored
import random
import time
print(colored('''
		  ___ _____ ____
		 / _ \_   _|  _ \\
		| | | || | | |_) |
		| |_| || | |  __/
		 \___/ |_| |_|        [ by: Khalidx456 ]
      ''',"red"))
while True:
    print(colored("[*] do you want to generate OTP","green"))
    user = input(colored("[~] Continue for [y/n] : ", "yellow"))
    if user == "y" or user =="Y":
        #otp generating
        print(colored("[o] your OTP generating...","cyan"))
        print(colored("[~] Waiting for some time...","light_magenta"))
        for b in range(1):
            otp = colored(random.randrange(100000,999999), "yellow")
            time.sleep(5)
            pt = colored(" [●] Your OTP ", "blue", "on_green")
            print(pt," => ", otp)
            print()
    elif user == "n" or user == "N":
        print(colored("[!] OTP generating cancelled...", "red"))
        break
    else:
        print(colored("[!] Enter Valid Character...", "magenta"))
        print()
    
                
            
            
            
            
        
            