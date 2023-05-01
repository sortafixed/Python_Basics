temperature = 90

if temperature > 80:
    print("It's warm")
elif temperature > 72:
    print("Its's nice")
else:
    print("It's cold")
print("")

x = int(input("Enter an integer for comparison: "))
y = int(input("Enter the second integer: "))

if x == y:
    print(f"{x} and {y} are equal")
elif x > y:
    print(f"{x} Is greater than {y}")
else:
    print(f"{y} Is greater than {x}")

