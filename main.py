
names_unparsed = input("Enter the names separated with space : ") 

isv_unparsed = input("Enter isv separated with space: ")

isv = isv_unparsed.split()
names = names_unparsed.split()

for n in names:
    print(n)


for x in isv:
    print(x)