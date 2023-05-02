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