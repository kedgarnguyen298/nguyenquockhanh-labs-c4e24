from calc import evaluate

# User nhập vào 2 số
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

# Người dùng chọn phép toán và in ra kết quả
oper = input("Enter operation: ")

r = evaluate(x, y, oper)

print(r)
