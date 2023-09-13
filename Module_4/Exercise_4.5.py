count = 1
username = str(input("Enter the username: "))
password = str(input("Enter the password: "))

while username != 'python' and password != 'rules':
    if count == 5:
        exit("Access denied")
    else:
        count += 1
    print("Incorrect information, try again:")
    username = str(input("Enter the username: "))
    password = str(input("Enter the password: "))

print("Welcome!")