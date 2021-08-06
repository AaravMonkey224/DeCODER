# imports
import os
import screens
import hashlib
from colorama import Fore as colour, Back, Style
from time import sleep as wait

# definitions
from subprocess import call

def clear():
    _ = call('clear' if os.name =='posix' else 'cls')


# screen functions
def encryptionProg():
	print(screens.encryptionScreen)
	encyr_input = input(": " + colour.GREEN)

	if encyr_input == "~":
		clear()
		main()
	else:
		result = hashlib.md5(encyr_input.encode())

		print(colour.WHITE + "\n The encrypted string is" + colour.CYAN + ": " + colour.RED + str(result.digest()))
		input(colour.BLACK + Back.WHITE + Style.BRIGHT + "\n[PRESS ENTER TO CONTINUE]	" + Style.RESET_ALL)

		clear()
		encryptionProg()
		
def main():
	start = True
	while start:
		print(screens.title)
		print(screens.titleScreen)
		choice = input(": " + colour.GREEN)

		if choice == "1":
			start = False
			clear()
			encryptionProg()
		elif
		elif choice == "~":
			start = False
			clear()
			wait(0.07)
			print("")
			print(colour.RED + "YOU ARE ALREADY AT THE HOME PAGE\n" + colour.WHITE)
			main()
		else:
			clear()
			print("")
			print(colour.RED + "THAT WAS NOT A VALID INPUT\n" + colour.WHITE)

if __name__ == "__main__":
	main()