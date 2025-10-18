# empty dictionary
contacts = {}

while True:
    print("\nContact Book App")
    print('1. Create Contact')
    print('2. View Contact')
    print('3. UPdate Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contact')
    print('7. Exit ')

    choice = input("Enter your choice = ")

    if choice == '1':
        name = input("Enter your name: ")
        if name in contacts:
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age = ")
            email = input("Enter email = ")
            mobile = input("Enter mobile number = ")
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f"Contact name {name} has been created successfully!")
        
    elif choice == '2':
        
        