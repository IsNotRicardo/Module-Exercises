gender = str(input("Insert your biological gender: ")).lower()

if gender == "female":
    hemoglobinRange = [117, 155]
elif gender == "male":
    hemoglobinRange = [134, 167]
else:
    print("Invalid biological gender.")
    exit()

hemoglobinValue = float(input("Insert your hemoglobin value: "))

if hemoglobinValue < hemoglobinRange[0]:
    print("Your hemoglobin value is low.")
elif hemoglobinValue > hemoglobinRange[1]:
    print("Your hemoglobin value is high.")
else:
    print("Your hemoglobin value is normal.")
