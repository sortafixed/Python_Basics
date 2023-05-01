for i in range(10):
    print(i)
print('')

grocery_list = ['milk', 'toast', 'eggs', 'avocados']

for item in grocery_list:
    print(item)
print('')

weights = [208, 175, 225, 189, 230, 115, 204]

total_weight = 0

for weight in weights:
    total_weight += weight

print(f"Total Weight: {total_weight}")
number_of_players = len(weights)
average_weight = total_weight / number_of_players
print(f"Average Weight is: {int(average_weight)}")
print('')

for number in range(3):
    print(f"Attempt: {number}")
