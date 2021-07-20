import os
import screens
from colorama import Fore as colour
from subprocess import call
from time import sleep as wait


def clear():
    _ = call('clear' if os.name =='posix' else 'cls')

print(screens.title)

def main():
	start = True
	while start:
		print(screens.titleScreen)
		choice = input(": ")
		if choice == "1":
			start = False
			clear()
			print("Working on it..")
		elif choice == "~":
			start = False
			clear()
			wait(0.07)
			print(screens.title)
			main()
		else:
			clear()
			print(colour.RED + "THAT WAS NOT A VALID INPUT" + colour.WHITE)

if __name__ == "__main__":
	main()