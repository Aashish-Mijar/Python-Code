details = {
    "name":"Aashish",
    "age":20,
    "address":"Waling",
    "profession":"Teacher"
}

details["address"] = "Waling-09"
# print(details)

# ---- Adding new items ----
details["gender"]="Male"

# ---- Using Loop ------

# for detail in details:
#     print(detail, details[detail])

for key, values in details.items():
    print(key, values)

# if "Waling" in details:
#     print("Yes, Information asked is present in loop")
# else:
#     print("No, it is not present. ")

# ------ Finding Length -----
print(len(details))

print(details)


