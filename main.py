
#names_unparsed = input("Enter the names separated with space : ") 

#$isv_unparsed = input("Enter isv separated with space: ")

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
            name, isv_val = user_input.split()
            names.append(name)
            isv.append(isv_val)
        counter -= 1
        if counter == 0:
            running = False

main()

        
for n in names:
    print("NAMES : ",n)


for x in isv:
    print("ISV IS THIS : ",x)
