pet_species = input("Enter species of your pet:\t")
pet_age = int(input("Enter age of your pet:\t"))

if pet_species == "Dog" and pet_age < 2:
    food = "Puppy food"
elif pet_species == "Cat" and pet_age > 5:
    food = "Senior cat food"
else:
    food = "Normal but with doctor's consult."

print(food)