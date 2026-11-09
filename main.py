# 1. Kiểm tra độ tuổi
age = int(input("Enter your age: "))

if age >= 100: print("You are too old to sign up")
elif age >= 18: print("You are now signed up")
elif age < 0: print("You haven't been born yet")
else: print("You must be 18 plus to sign up")

# 2. Kiểm tra phản hồi có/không
response = input("Would you like food (Y/N)?: ")

if response == "y":print("Have some food")
else:print("No food for you")

# 3. Kiểm tra tên người dùng
name = input("Enter your name: ")

if name == "":print("You did not type in your name")
else:print(f"Hello {name}")

# 4. Sử dụng Boolean
for_sale = True

if for_sale:print("This item is for sale")
else:print("This item is not for sale")