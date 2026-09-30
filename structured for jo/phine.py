fruits =[]

while True:
    print("\n1.Add")
    print("2.View")
    print("3.Exit")
    
    choice = input("Enter your choice")
    match choice:
        case "1":
            name= input("Enter fruit name:")
            fruits.append(name)
            print("Added successfully")
        case "2":
            print(fruits)
        case "3":
            print("Exiting..")
            break
        case _:
            print("wrong choice, try again")