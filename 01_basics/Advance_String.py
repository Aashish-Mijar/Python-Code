text = " Python is Awesome! "

# Strip and formatting
print(text.strip().lower())

# Count and replace
print("Count of 'o':", text.count('o'))
print(text.replace("Awesome", "Powerful"))

# ---Using f-String formatting----
name = "Aashish"
marks = 90
print(f"{name:^10} | {marks:>3}")