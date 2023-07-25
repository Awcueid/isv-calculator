values = [[],[],[],[],[]] #meepless wanted to name it this
room_order = [[],[],[],[],[]]
def main():
    

    running = True
    counter = 0
    while running:
        user_input = input("Enter name followed by ISV or Q to quit ") 
        if user_input.upper() == "Q":
            running = False
        else:
            try:
                name_unparsed, isv_unparsed = user_input.split()
                isv_lead , isv_team = isv_unparsed.split("/")

                if not isv_lead.isdigit() or not isv_team.isdigit() or int(isv_team) < int(isv_lead):
                    raise ValueError 
                

            except ValueError:
                 print("Error: Invalid input, please input correct ISV")
                 continue

            
            isv_value = (int(isv_team) - int(isv_lead))* 0.2 + int(isv_lead)
            values[counter].append(isv_value)
            values[counter].append(name_unparsed)
            counter += 1


        
        if counter == 5:
            running = False

    val_sorted = sorted(values)

    room_order[0] = val_sorted[2]
    room_order[1] = val_sorted[1]
    room_order[2] = val_sorted[0]
    room_order[3] = val_sorted[3]
    room_order[4] = val_sorted[4]

main()

print(" ".join(x[1] for x in room_order))