people = dict({"ganesh":"builder","Mukhesh":"Engineer","Kalandhar":"Singer"})

def intro():
    print("Welcome to my Database.\nEnter the Password to login\n")
    enter_password()

def enter_password():
    password = "Nithesh944@"
    entry1 = input("Enter password here: ")
    if entry1 != password:
        print("Access Denied!!")
        enter_password()
    else:
        print ("Access Granted!!!")
        data_base()

def data_base():
        print("\nThis Database consists of people and their profession\n",people)   
        x = int(input("\nWhat you Want to do?\nClear(1)\nUpdate(2)\nPrint(3)\nEnter here: "))
        if x == 1:
            people.clear()
            print(people)
            confirm()
        elif x == 2 :
            update_dictionary()
        elif x == 3:
            print(people)
            confirm()
    

def update_dictionary():
    print("\nYou can update the database below!")
    name = input("\nEnter name: ")
    job = input("Enter job: ")
    people[name]= job
    print("Here's your updated Database:\n",people)
    Further = input ("Do you want to update futher?\n")
    Further1 = Further.lower()
    if Further1=="yes":
        update_dictionary()
    else:
        print("Thanks For Accessing!")
        confirm()

def confirm():
    confirm = input("Do you want to access Database Further..?\n")
    confirm1 = confirm.lower() 
    if confirm1 == "yes":
        data_base()
    elif confirm1 == "no" :
            print("You will not be accesing the database Anymore!")



intro()
    

    
    