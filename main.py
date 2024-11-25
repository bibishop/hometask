import random
locations = [random.randint(1, 7) for _ in range(3)]
print("Guess the locations of the 3 boxes and their weights. Enter one location and its weight at a time.")

while True:
    print("Enter the first location and weight:")
    guess1 = int(input())
    weight1 = int(input())
    print("Enter the second location and weight:")
    guess2 = int(input())
    weight2 = int(input())
    print("Enter the third location and weight:")
    guess3 = int(input())
    weight3 = int(input())

    if guess1 != guess2 and guess1 != guess3 and guess2 != guess3:
        correct_guesses = 0
        for g in [guess1, guess2, guess3]:
            if g in locations:
                correct_guesses += 1

        if correct_guesses == 3:
            total_weight = weight1 + weight2 + weight3
            if total_weight == 713:
                print("Congratulations! You found all the cargo!")
                break
            else:
                print("Weights do not sum to 713.")
        else:
            print("Incorrect locations.")
    else:
        print("Guesses must be distinct.")