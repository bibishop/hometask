import random

locations = random.sample(range(1, 8), 3)
weight1 = random.randint(1, 300)
weight2 = random.randint(1, 300)
weight3 = 713 - weight1 - weight2
print("Guess the locations of the 3 boxes and their weights. Enter one location and its weight at a time.")
print(f'They remembered the weight of the boxes: {weight1}, {weight2}, {weight3}.')

while True:
    print("Enter the first location and weight:")
    guess1 = int(input())
    guess_weight1 = int(input())
    print("Enter the second location and weight:")
    guess2 = int(input())
    guess_weight2 = int(input())
    print("Enter the third location and weight:")
    guess3 = int(input())
    guess_weight3 = int(input())

    if guess1 != guess2 and guess1 != guess3 and guess2 != guess3:
        print(locations)
        correct_guesses = 0
        for g in [guess1, guess2, guess3]:
            if g in locations:
                correct_guesses += 1
                print(f"Location {g} is correct.")

        if correct_guesses == 3:
            total_weight = guess_weight1 + guess_weight2 + guess_weight3
            if total_weight == 713:
                print("Congratulations! You found all the cargo!")
                break
            else:
                print("Weights do not sum to 713.")
        else:
            print(f"You found {correct_guesses} correct locations.")
    else:
        print("Guesses must be distinct.")