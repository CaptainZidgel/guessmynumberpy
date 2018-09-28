import random
num = random.randint(1,20)
guess = None
print(num)
while guess != num:
    print("Guess the number, between 1 and 20")
    try:
        guess = int(input())
    except ValueError:
        print("That's not a valid input.", end=" ")
        continue
    attempts = attempts + 1
    if guess < num:
        print("Your guess is too low!", end=" ")
    elif guess > num:
        print("Your guess is too high!", end=" ")
print("Correct! You guessed it in " + str(attempts), end="")        
if attempts > 1:                                                        
    print(" attempts!")                                                         
else:                                                                  
    print(" attempt!")                                                 
