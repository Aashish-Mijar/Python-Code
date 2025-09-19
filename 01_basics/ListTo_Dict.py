keys = ["Mode", "Medium", "Status"]
default_values = ["Oral", "Mobile Phone", "Complete"]

# ---- This method add all the values in each keys
new_dict = dict.fromkeys(keys, default_values)
print(new_dict)