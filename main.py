def add(x, y):
    total_add = x + y
    return total_add

def subtract(x, y):
    total_sub = x - y
    return total_sub

def multiply(x, y):
    total_mul = x * y
    return total_mul

def divide(x, y):
    total_div = x / y
    return total_div


print('\n**********************************')
print('*                                *')
print('*        Select operation        *')
print('*                                *')
print('**********************************\n')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')


choice = input("Enter choice: ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


if choice == '1':
    print(f'Add total: { num1 } + { num2 } = { add(num1, num2) }')
elif choice == '2':
    print(f'Subtract total: { num1 } - { num2 } = { subtract(num1, num2) }')
elif choice == '3':
    print(f'Multiply total: { num1 } * { num2 } = { multiply(num1, num2) }')
elif choice == '4':
    print(f'Divide total: { num1 } / { num2 } = { divide(num1, num2) }')
