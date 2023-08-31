length = float(input("Insert the zander length (cm): "))

if length < 42:
    print("You need to return the zander to the lake. It is", 42 - length, "cm below the size limit.")
else:
    print("You can keep the zander.")

