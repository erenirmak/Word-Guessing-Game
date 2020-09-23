import random

category_lists = {
    1 : ["cat", "dog", "elephant", "giraffe", "monkey", "hippopotamus", "turtle", "dolphin", "shark", "snake"],
    2 : ["paris", "london", "istanbul", "adana", "ankara", "izmir", "moscow", "new york", "california"],
    3 : ["brad pitt", "angelina jolie", "ricky martin", "michael jackson", "britney spears", "jennifer lopez"],
    4 : ["apple", "watermelon", "banana", "tomato", "pinetree", "strawberry", "orange"],
    5 : ["pencil", "book", "pen", "paper", "plate", "fork", "watch", "spoon", "chair"]
    }

#1 : animals
#2 : cities
#3 : famous
#4 : plants
#5 : objects

def rand_item(list):
    item = random.randint(1, len(list))
    if isinstance(list, dict):
        if item == 1:
            print("Animal: ")
        elif item == 2:
            print("City: ")
        elif item == 3:
            print("Famous Person: ")
        elif item == 4:
            print("Plant: ")
        elif item == 5:
            print("Object: ")
        return rand_item(list.get(item))
    else:
        return list[item-1]

def guesser(tmp, word, charVar):
    if len(charVar) == 1:
        for i in range(0, len(word)):
            c = word[i]
            if c == charVar:
                tmp = tmp[:i] + c + tmp[i + 1:] #working with index(!)

            print(tmp[i], end = " ")
        return tmp
    else:
        if word == charVar:
            tmp = word
            return tmp
        else:
            return 0

def main():
    print("Welcome to game of guessing!")
    
    res = 0
    while res == 0:
        word = rand_item(category_lists)
        tmp = ""
        for c in word: #encoding
            if c == ' ':
                tmp += " "
                print(" ", end = " ")
            else:
                tmp += "_"
                print("_", end = " ")

        count = 0
        flag = 0
        while flag == 0:
            
            lttr = input("\n\nEnter letter: ")
            tmp = guesser(tmp, word, lttr)

            if word == tmp:
                print("\nCongratulations!")
                flag = 1
            elif tmp == 0:
                print("\nYou failed in your guess!")
                flag = 1

            count += 1
            if count == 6:
                print("\n\nYou failed to guess the word!")
                flag = 1

        ext_ctrl = 0
        while ext_ctrl == 0:
            cnt = input("\nWant to play new game? y/n\n").upper()
            if cnt == 'Y':
                ext_ctrl = 1
                res = 0
            elif cnt == 'N':
                print("Thanks for playing the game!")
                ext_ctrl = 1
                res = 1
            else:
                print("Entered something wrong!")
                ext_ctrl = 0


if __name__ == '__main__':
    main()