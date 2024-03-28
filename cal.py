def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divide(x, y):
    if y == 0:
        return "error!division by zero"
    else:
        return x/y


print("select option")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    choice = input("enter choice(1/2/3/4):")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("enter your first number:"))
        num2 = float(input("enter your second number:"))

        if choice == '1':
            print("result:", add(num1, num2))
        elif choice == '2':
            print("result:", subtract(num1, num2))
        elif choice == '3':
            print("result:", multiply(num1, num2))
        elif choice == '4':
            print("result:", divide(num1, num2))
        else:
            print("invalid number")

        next_calculation = input("do yoy want to perform another calculation?(yes/no):")
        if next_calculation.lower() != "yes":
            break



