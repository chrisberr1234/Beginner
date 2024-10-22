known_users = ["Chris", "Cameron","Claire", "Dan", "Emma", "Fred"]

print(len(known_users))#PrintOutTheLengthOfTheList

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?:").strip().capitalize()

    #use logic to determine if name entered is in the list or not

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)

        #what if they say no, if they say no
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway")
            

    else:
        print("I do not know you yet {}".format(name))
        #ask user if the want to enter list using logic and get user input stored in a variable so that we can manipulate
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        #if user says yes, allow input to enter name
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        #if user says no, exit
        elif add_me =="n":
            print("No Worries, Maybe you'd like to join next time")
            
        
        
