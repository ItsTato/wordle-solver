import json
import os
from time import sleep
import colorama
from colorama import Fore, Back, Style

colorama.just_fix_windows_console()

alphabet:list[str] = [
	"a","b","c","d","e",
	"f","g","h","i","j",
	"k","l","m","n","o",
	"p","q","r","s","t",
	"u","v","w","x","y",
	"z"
]

def getLetterFrequency(word_list:list[str]) -> dict[str,int]:
	letterFrequency:dict[str,int] = {}

	for letter in alphabet:
		letterFrequency[letter] = 0

	for letter in alphabet:
		for word in word_list:
			if letter in word: letterFrequency[letter] += 1

	return letterFrequency

def getWordWeighs(word_list:list[str],letter_frequency:dict[str,int]) -> dict[str,int]:
	weighedWords:dict[str,int] = {}

	for word in word_list:
		weighedWords[word] = 0
	
	for word in word_list:
		for letter in word:
			weighedWords[word] += letter_frequency[letter]

	return weighedWords

def findHeaviestAllowedWord(word_list:list[str],weighed_word_list:dict[str,int],banned_letters:list[str]) -> str:
	heaviest_allowed_word:str = "ERROR"
	heaviest_word_weight:int = 0

	for word in word_list:
		for letter in word:
			if letter in banned_letters:
				continue
		if weighed_word_list[word] > heaviest_word_weight:
			heaviest_allowed_word = word

	return heaviest_allowed_word

if __name__ != "__main__":
	exit()

os.system("cls" if os.name in ["nt","win"] else "clear")
print("wordle-solver by ItsTato")
print(" [---] Generating/Fetching runtime data...",end="\r")

with open("./words.json","r") as file:
	words:list[str] = json.load(file)["words"]
print(" [#--] Generating/Fetching runtime data...",end="\r")

if not os.path.exists("./letter_frequency.json"):
	letterFrequency:dict[str,int] = getLetterFrequency(words)
	with open("./letter_frequency.json","w") as file:
		json.dump(letterFrequency,file)
else:
	with open("./letter_frequency.json","r") as file:
		letterFrequency:dict[str,int] = json.load(file)
print(" [##-] Generating/Fetching runtime data...",end="\r")

if not os.path.exists("./weighed_words.json"):
	weighedWords:dict[str,int] = getWordWeighs(words,letterFrequency)
	with open("./word_weighs.json","w") as file:
		json.dump(weighedWords,file)
else:
	with open("./word_weighs.json","r") as file:
		weighedWords = json.load(file)
print(" [###] Generating/Fetching runtime data...",end="\r\n")

print(" [ ✔ ] All runtime data ready!")

for i in range(3):
	print(f"Program starting in {3-i}s... Thanks for using!",end="\r")
	sleep(1)

os.system("cls" if os.name in ["nt","win"] else "clear")
print("           wordle-solver by ItsTato")
print("                [INSTRUCTIONS] ")
print(" > You will be prompted with a word to input")
print("   into your Wordle game. After you type it,")
print("   you will be asked to type in a 'result'")
print("   string. This will be formatted like so:")
print(f"   word: edify, result: {Back.LIGHTBLACK_EX}e{Back.LIGHTGREEN_EX}D{Back.LIGHTRED_EX}i{Back.LIGHTBLACK_EX}fy{Back.RESET},{Back.LIGHTYELLOW_EX}i{Back.RESET}")
print(f" > {Back.LIGHTGREEN_EX}Green letters{Back.RESET} are marked with a capital letter.")
print(f" > {Back.LIGHTYELLOW_EX}Yellow letters{Back.RESET} are appended at the end after a ','")
print(f" > Multiple yellows would look like: 'edify,{Style.BRIGHT}eiy{Style.RESET_ALL}'.")
print(f" > ALL other letters are {Style.BRIGHT}DISREGARDED AS GRAYS{Style.RESET_ALL}.")
print(f" > {Style.BRIGHT}EVEN IF THERE ARE NO YELLOWS, ADD A ,{Style.RESET_ALL}")
beginInput:str = input("Press ENTER to acknowledge and begin a game: ")
if beginInput != "":
	print("Key other than ENTER entered as well, game closing.")
	exit()

os.system("cls" if os.name in ["nt","win"] else "clear")
print("wordle-solver by ItsTato")

for index in range(int(input("How many guesses do you have (i.e., 6)? "))):
	lockedLetters:dict[int,str] = {
		1: "",
		2: "",
		3: "",
		4: "",
		5: ""
	}
	yellowLetters:list[str] = []
	grayLetters:list[str] = []
	unknownLetters:list[str] = [*alphabet]

	nextWord:str = findHeaviestAllowedWord(words,weighedWords,grayLetters)
	print(nextWord)
