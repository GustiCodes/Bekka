

# ANSI escape codes for text colors
class TextColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Reset color to the default


answer_1 = "WISCONSIN"
guess = ""
guess_count = 0
guess_limit = 2

print("\n Dearest Bekka, my sweetest, I've crafted a delightful puzzle game that unfolds a tiny piece of art I created, just for you.")
print(" I hope it brings a smile to your heart as you uncover the special moments we share within its charming pieces.")
print(TextColors.WARNING+ "[P.S. All characters of your answers have to be in CAPS]\n" + TextColors.ENDC)

while guess != answer_1:
    if guess_count == 2:
        print(TextColors.FAIL+ "\n HINT: "+ TextColors.WARNING+ "A state not far from Chicago, that sets Wilderness in it's heart!\n" + TextColors.ENDC)

    guess = input("In the grand U.S.A, where dreams come true, In which state, my dear, did I fall for you?\n\n ")
    guess_count += 1

print(TextColors.OKBLUE+ "\n You've woven the threads of our story beautifully with Wisconsin, our first shared chapter.")
print(" But, a new puzzle awaits, a tapestry of moments yet to unfold, just for you.\n" +TextColors.ENDC)


answer_2 = "WP"

guess_2 = ""
guess_count_2 = 0
guess_limit_2 = 2

while guess_2 != answer_2:
    if guess_count_2 == 2:
        print(TextColors.FAIL+ "\n HINT: "+ TextColors.WARNING+ "The answer consists of two of the very first letters of our favorite colors!\n" 
              "EXAMPLE: RB= RedBrown\n"+ TextColors.ENDC)

    guess_2 = input("Mix the colors, my dear, a secret to reveal, \nThe dance of hues, just us, a bond to seal. "
                    "\nFrom your favorite shade to mine, take the cue,"
                    "\nCombine the first letters for a connection so true: \n")
    guess_count_2 += 1

print(TextColors.OKBLUE+ "\n You've perfectly unveiled the hues of our connection,")
print(" turning a simple guessing game into a beautiful testament of our shared world.")
print("But lets not wait for much longer as there is one more puzzle to solve \n"+TextColors.ENDC)

answer_3 = "ITALY"

guess_3 = ""
guess_count_3 = 0
guess_limit_3 = 2

while guess_3 != answer_3:
    if guess_count_3 == 2:
        print(TextColors.FAIL+ "\n HINT: "+ TextColors.WARNING+ "Think of a place where love weaves tales, where cobblestone walls whisper and where taste meets within pasta and wine! \n" + TextColors.ENDC)

    guess_3 = input("\nGuess the place, my dear, a destination concealed,"
                    "\nThe next adventure, in our shared world revealed. "
                    "\nIn capital letters, the answer we wield, \nDecipher the code, our next journey sealed:\n")
    guess_count_3 += 1

print(TextColors.OKBLUE+ "\n Well done my dear! You have guessed the place where our hearts will meet in warmth again,")
print("a place where we will be alone, just the two of us!\n"+TextColors.ENDC)

print("Congratulations again for conquering my little maze, the secret that it was hiding is a POEM. ")
print("A POEM that I have put together just for you! ")
print("I hope you will like it.\n")


print(TextColors.HEADER + "\n As treetops sway, wind whispers in the valley, "
      "\n embracing the ocean's breath.\n"           
      "\n A summer night unfolds, stars dance, echoing thoughts of her."
      "\n Dark-haired muse, eyes deep as the sea, gaze upon me, "
      "\n Penetrating my delicate soul with gentle touch.\n"
      "\n In the depths of that oceanic night I descended"
      "\n with your image in sight,\n"
      "\n Falling, yet not falling, floating, not merely floating,"
      "\n but soaring.\n"
      "\n She led me to Chicago heights and Cascais nights,"
      "\n Each moment, each heartbeat, belonged to her, "
      "\n a timeless pause amidst the world's motion." + TextColors.ENDC)

heart_char = "♥"

print("", end='                  ')
print(heart_char + heart_char + heart_char)