import random
locations = [random.randint(1, 7) for _ in range(3)]
print("Guess the locations of the 3 boxes and their weights. Enter one location and its weight at a time.")
while True:
    print("Enter the first location and weight:")
    guess1 = int(input())
    weight1 = int(input())