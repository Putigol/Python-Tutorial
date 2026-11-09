friends = 0
friends += 1  # Tăng lên 1

# Toán tử số học cơ bản
friends -= 2
friends *= 3
friends /= 2
friends **= 2  # Lũy thừa
remainder = 10 % 3  # Chia lấy dư

# 2. Các hàm toán học tích hợp (Built-in Math Functions)
result = round(3.14)   # Làm tròn
result = abs(-4)       # Giá trị tuyệt đối
result = pow(4, 3)     # Lũy thừa (4^3)
result = max(3.14, 4, 5) # Tìm giá trị lớn nhất
result = min(3.14, 4, 5) # Tìm giá trị nhỏ nhất

# 3. Module Math
import math

print(math.pi)    # Giá trị PI
print(math.e)     # Hằng số e
result = math.sqrt(9) # Căn bậc hai
result = math.ceil(9.1) # Làm tròn lên
result = math.floor(9.9) # Làm tròn xuống

# 4. Bài tập thực hành
import math

# Bài 1: Chu vi hình tròn
radius = float(input("Nhập bán kính: "))
circumference = 2 * math.pi * radius
print(f"Chu vi là: {round(circumference, 2)}")

# Bài 2: Diện tích hình tròn
area = math.pi * pow(radius, 2)
print(f"Diện tích là: {round(area, 2)}")

# Bài 3: Tính cạnh huyền tam giác vuông
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Cạnh huyền c là: {c}")