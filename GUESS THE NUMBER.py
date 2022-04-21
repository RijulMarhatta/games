import random
x = int(input("Guess the Random Number between 1 to 100:"))
randomnumber = random.randint(0, 100)
print(x)
# print(randomnumber)
if randomnumber == x:
    print("you are right")
else:
    print("You are wrong")

print(f"random number was", {randomnumber})
