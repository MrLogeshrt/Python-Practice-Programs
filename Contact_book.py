#Contact book Program
global d
d = {}


def add(d) :
    name = input("Enter a name to add : ")
    while name in d :
        print("The provided name is already in use , use a different one.")
        name = input("Enter a name to add : ")
    num = int(input("Enter the contact number : "))
    d[name] = num
    if name in d :
        print("Contact added successfully.")
    else :
        print("There is an error while adding the contact.")
    return 0


def search(d) :
    find = input("Enter the error free name to search : ")
    if find not in d :
        print("Contact not found , Please recheck the name carefully.")
    for key in d :
        if key == find :
            print(f"The contact number of {key} is {d[key]}")
            break
    return 0


def delete(d) :
    de = input("Enter the contact name to delete : ")
    if de in d :
        del(d[de])
        print("Contact deleted successfully.")
    else :
        print("Contact not found , Please recheck the name carefully.")
    return 0


def update(d) :
    upd = input("Enter the contact to update : ")
    if upd not in d :
        print("Contact not found , Please recheck the name carefully.")
    else :
        upd_num = int(input("Enter the number to update : "))
        for key in d :
            if key == upd :
                d[key] = upd_num
                print("Contact updated sucessfully.")
                break
    return 0


while True :
    print("1.Add a contact\n2.Search a contact\n3.Delete an existing contact\n4.Update a contact\n")
    opt = int(input("Enter your Choice : "))
    if opt == 1 :
        add(d)
    elif opt == 2 :
        search(d)  
    elif opt == 3 :
        delete(d)
    else :
        update(d)
    ch = int(input("\nAre you want to continue.? (1 for Yes & 0 for No) : "))
    if ch != 0 and ch != 1 :
        print("\nInvalid choice..")
    elif ch == 0 :
        print("Thank you..")
        break
    else :
        continue