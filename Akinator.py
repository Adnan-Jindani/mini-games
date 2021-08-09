data = ["elephant", "cat", "dog", "tiger", "bat"]
submit_dog = "Is your animal dog?\n"
submit_cat = "Is your animal cat?\n"
submit_elephant = "Is your animal elephant?\n"
submit_bat = "Is your animal bat\n"
submit_tiger = "Is your animal tiger?\n"

print("Keep an animal from the list in your mind :- elephant, cat, dog, tiger, bat")
print("Type 'yes' or 'no' for the questions that are asked to you")
a = input("Does your animal do bow - wow? \n")
#dog
if a == "yes":
    ans = input(submit_dog)
    if ans == "no":
        print("Sorry, I lose")
    input("Type exit and hit enter to exit\n")
elif a == "no":
    data = ["elephant", "cat", "tiger", "bat"]
    #cat
    b = input("Does your animal do meow - meow?\n")
    if b == "yes":
        ans = input(submit_cat)
        if ans == "no":
            print("Sorry, I lose")
        input("Type exit and hit enter to exit\n")
    elif b == "no":
        data = ["elephant", "tiger", "bat"]
        #elephant
        c = input("Does your animal have a long trunk?\n")
        if c == "yes":
            ans = input(submit_elephant)
            if ans == "no":
                print("Sorry, I lose")
            input("Type exit and hit enter to exit\n")
        elif c == "no":
            data = ["tiger", "bat"]
            #bat
            d = input("Does your animal sleep during day?\n")
            if d == "yes":
                ans = input(submit_bat)
                if ans == "no":
                    print("Sorry, I lose")
                input("Type exit and press enter to exit\n")
            elif d == "no":
                data = "tiger"
                #tiger
                ans = input(submit_tiger)
                if ans == "no":
                    print("Sorry, I lose")
                input("Type exit and hit enter to exit\n")