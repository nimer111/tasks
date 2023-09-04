#task  الاول تم حله ورفعه سابقا
#task ..2

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))


sum_result = num1 + num2
subtraction_result = num1 - num2
multiplication_result = num1 * num2


if num2 != 0:
    division_result = num1 / num2
    print(f"Sum: {sum_result}")
    print(f"Subtraction: {subtraction_result}")
    print(f"Multiplication: {multiplication_result}")
    print(f"Division: {division_result:.2f}")
else:
    print("Division by zero is not allowed.")

#task ..3
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8 + 32)
    return fahrenheit

celsius1 = 25
fahrenheit1 = celsius_to_fahrenheit(celsius1)
print(f"{celsius1} degrees Celsius is equal to {fahrenheit1:.2f} degrees Fahrenheit")


celsius2 = 0
fahrenheit2 = celsius_to_fahrenheit(celsius2)
print(f"{celsius2} degrees Celsius is equal to {fahrenheit2:.2f} degrees Fahrenheit")


celsius3 = -10
fahrenheit3 = celsius_to_fahrenheit(celsius3)
print(f"{celsius3} degrees Celsius is equal to {fahrenheit3:.2f} degrees Fahrenheit")

#task ..4
for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#task ..5


list1 = [1, 2, 3]
list2 = [4, 5, 6]

for item in list1:
    list2 += [item]

print("new lest", list2)

numbers = [4, 7, 6, 3, 9]
sorted_numbers = sorted(numbers, reverse=True)
second_biggest = sorted_numbers[1]
print("number:", second_biggest)

names = ["dana", "ali", "samar"]
capitalized_names = [name.capitalize() for name in names]
result_string = ", ".join(capitalized_names)
print("lest", result_string)

