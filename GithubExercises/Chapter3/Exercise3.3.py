gender = str(input("Insert your biological gender: ")).lower()
hemoglobinValue = float(input("Insert your hemoglobin value: "))
hemoglobinRange = list(range(2))

if gender == "female":
    hemoglobinRange = [117, 155]
elif gender == "male":
    hemoglobinRange = [134, 167]
else:
    print("Invalid biological gender.")
    exit()

if hemoglobinValue < hemoglobinRange[0]:
    print("Your hemoglobin value is low.")
elif hemoglobinValue > hemoglobinRange[1]:
    print("Your hemoglobin value is high.")
else:
    print("Your hemoglobin value is normal.")