items = ["apple", "banana", "orange", "apple"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Dupliate:", item)
        break
    unique_item.add(item)