# Lists
my_list = [10, 14, 22, 33, 9, 50]
for i in my_list:
    print(i)


# Tuples
my_tup = (1,2,3,4,5,6,7,22,18)
for i in my_tup:
    print(i)

# Dictionary
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
print(capitals.get("USA"))
capitals.update({"Germany": "Berlin"})
print(capitals)
capitals.pop("China")
print(capitals)
capitals.update({"USA": "Detroit"})
print(capitals)
for key in capitals.keys():
    print(key)


values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items()
items = capitals.items()
print(items)

for key, value in capitals.items():
    print(key, value)
    print(f"The capitol of {key} is {value}")

