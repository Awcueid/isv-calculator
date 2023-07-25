isv = []
names = []
def main():
    

    running = True
    counter = 5
    while running:
        user_input = input("Enter name followed by ISV or Q to quit ") 
        if user_input.upper() == "Q":
            running = False
        else:
            try:
                name_unparsed, isv_unparsed = user_input.split()
                isv_lead , isv_team = isv_unparsed.split("/")
                print(isv_lead)
                print(isv_team)

                if not isv_lead.isdigit() or not isv_team.isdigit():
                    raise ValueError 

            except ValueError:
                 print("Error: Invalid input, please input correct ISV")
                 continue
            names.append(name_unparsed)



        counter -= 1
        if counter == 0:
            running = False

main()

        
for n in names:
    print("NAMES : ",n)


for x in isv:
    print("ISV IS THIS : ",x)
