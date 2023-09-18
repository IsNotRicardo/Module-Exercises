listNames = set()

name = str(input("Insert a name: "))

while name != ' ':
    if name in listNames:
        print("Existing name")
    else:
        print("New name")
    listNames.add(name)
    name = str(input("Insert a name: "))

print(listNames)
