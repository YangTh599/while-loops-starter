# Thayer Yang
# 25 NOV 2024
# While Loops

from time import sleep as s

run = True
temps = []

try:
    while run:
        temp = int(input("Enter a temperature in Fahrenheit(-9999 to quit): "))
        if temp != -9999:
            temps.append(temp)
        else:
            run = False
except ValueError:
    print("Enter an integer")

s(1)
print(f"Temperatures entered: {temps}")

avg_temp = sum(temps) / len(temps)
print(f"Average Temperature: {avg_temp:.2f}°F")