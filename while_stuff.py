i = 0

while i < 10:
    print(i)
    i += 1
print('')

legal_age = 21

age = int(input('How old are you? '))

while age < 21:
    print(f"{age} Is too young to drink!")
    age = int(input('How old are you? '))

print(f"{age} Is legal drinking age, have a drink")
