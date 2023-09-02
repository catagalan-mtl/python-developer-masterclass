items = {}
answer = input("Enter an item (or 'done' to finish): ")

while answer != 'done':
    if answer not in items:
        items[answer] =  1
    else:
        items[answer] = items[answer] + 1
    answer = input("Enter an item (or 'done' to finish): ")

print("\nItem counts:")
for key, value in items.items():
    print(f"{key}: {value}")
