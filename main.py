values = [[],[],[],[],[]] #meepless wanted to name it this
room_order = [[],[],[],[],[]] # final room order


def main():
    
    running = True
    counter = 0 # for incrementing 
    while running:
        user_input = input("Enter name followed by ISV or Q to quit ") # accept user input
        if user_input.upper() == "Q": # exits program
            running = False
        else:
            try:
                name_unparsed, isv_unparsed = user_input.split()  # split the name and isv
                isv_lead , isv_team = isv_unparsed.split("/")  # split the isv into leader and the team

                if not isv_lead.isdigit() or not isv_team.isdigit() or int(isv_team) < int(isv_lead): # error handling for isv
                    raise ValueError 
                
            except ValueError:
                 print("Error: Invalid input, please input correct ISV")
                 continue

            isv_value = (int(isv_team) - int(isv_lead))* 0.2 + int(isv_lead) # calculate isv value
            values[counter].append(isv_value) # appending 
            values[counter].append(name_unparsed)
            counter += 1
        
        if counter == 5: # increments counter
            running = False

    val_sorted = sorted(values) # sort the values

    room_order[0] = val_sorted[2] # order the room 
    room_order[1] = val_sorted[1]
    room_order[2] = val_sorted[0]
    room_order[3] = val_sorted[3]
    room_order[4] = val_sorted[4]
    
    try:
        print(" ".join(x[1] for x in room_order)) # print the results 
    except:
        print("Did not fill in all the members")


main()