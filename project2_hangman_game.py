import random
word_list=["apple","banana","apricot","blackberry","blueberry","cherry","cranberry","custardapple","dates","dragonfruit","grapes","jackfruit","kiwi","lychee","mango","muskmelon","orange","papaya","peach","pear","pineapple","pomegranate","raspberry","chikoo","strawberry","watermelon"]
selected_word=random.choice(word_list)
lives=len(selected_word)+2


display=[]
for i in range(len(selected_word)):
    display += '_'
print(display)

game_ends=False
while not game_ends:
    guessed_letter=input("Guess a letter: ").lower()
    for position in range(len(selected_word)):
        letter=selected_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)            
                
    if guessed_letter not in selected_word:
        lives -= 1
        print(f"{lives} Chances left")
        if lives == 0:
            game_ends = True
            print("NO MORE CHANCES LEFT")
            print("         ...GAME OVER...")
    if '_' not in display:
            game_ends=True
            print("*** YOU WON ***")    
            