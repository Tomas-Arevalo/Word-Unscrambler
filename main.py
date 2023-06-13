import random

def get_subjectList():
    subjects = []
    with open("foods.txt", "r") as file:
        foods = file.readlines()
        subjects.append(foods)
    with open("brands.txt", "r") as file:
        brands = file.readlines()
        subjects.append(brands)
    with open("animals.txt", "r") as file:
        animals = file.readlines()
        subjects.append(animals)
    topics = ["foods", "brands", "animals"]
    index = random.randrange(len(subjects))
    subjectList = subjects[index]
    for i in range(len(subjectList)):
        subjectList[i] = str(subjectList[i])
        subjectList[i] = subjectList[i].strip()
    subjectList.append(topics[index])
    return subjectList

def scramble_word(a):
    list1 = []
    numberlist = []
    scramble = ""
    for i in range(len(a)):
        list1.append(a[i])
        numberlist.append(i)

    for i in range(len(list1)):
        index = numberlist[random.randrange(len(numberlist))]
        scramble += list1[index]
        numberlist.remove(index)
    return scramble

def play(unscram, scram, hint, guess):
    count = 0
    hint2 = ""
    while guess != unscram:
        if guess == "1":
            print("It's in the \"", hint, "\" category", sep="")
        elif guess == "2":
            hint2 += unscram[count:count + 1]
            print(hint2)
            if hint2 == unscram:
                print("You lose :(")
                print("The word was:", unscram)
                break
            count += 1
        else:
            print("Try again!")
        guess = input("Your Answer: ")
    if guess == unscram:
        print("Correct!")

def main():
    print("Welcome to Word Unscrambler!")
    words = get_subjectList()
    hint = words.pop()
    unscrambled = words[random.randrange(len(words))]
    scrambled = scramble_word(unscrambled)
    print("\nYour Scrambled Word:")
    print(scrambled)
    print("\nFor a hint type: 1")
    print("For the first/next letter type: 2")
    print("\nType the unscrambled word below!")
    userInput = input("Your Answer: ")
    play(unscrambled, scrambled, hint, userInput)

main()
