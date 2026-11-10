import random

# Khởi tạo các biến
low = 1
high = 100
guesses = 0
number = random.randint(low, high)

# Chương trình đoán số
while True:
    guess = int(input(f"Enter a number between {low} through {high}: "))
    guesses += 1
    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is to hi")
    else:
        print(f"{guess} is correct")
    break
print(f"This round took you {guesses} guesses")

# Các ví dụ khác trong video
options = ['Rock', 'Paper', 'Scissors']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

number = random.random()
number = random.randint(1, 6)
number = random.randint(low, high)
choice = random.choice(options)
random.shuffle(cards)