talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: ")) + talents * 20
lots = float(input("Enter lots: ")) + pounds * 32

weight = lots * 0.0133

print("The weight in modern units is:\n" +
      str(int(weight)), "kilograms and", round((weight - int(weight)) * 1000, 2), "grams.")