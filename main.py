# 1. List (Danh sách)

# Khởi tạo list
fruits = ["apple", "orange", "banana", "coconut"]

# Truy cập phần tử
print(fruits[0])  # Apple

# Thay đổi phần tử
fruits[0] = "pineapple"

# Các phương thức phổ biến
fruits.append("pineapple")
fruits.remove("pineapple")
fruits.insert(0, "pineapple")
fruits.sort()
fruits.reverse()
fruits.clear()

# 2. Set (Tập hợp)

# Khởi tạo set
fruits = {"apple", "orange", "banana", "coconut"}

# Các phương thức phổ biến
fruits.add("pineapple")
fruits.remove("apple")
fruits.pop() # Xóa phần tử ngẫu nhiên
fruits.clear()

# 3. Tuple (Bộ giá trị)

# Khởi tạo tuple
fruits = ("apple", "orange", "banana", "coconut")

# Các phương thức khả dụng
fruits.index("apple")
fruits.count("coconut")