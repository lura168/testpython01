print("====Welcome to the Tip Calculaor====")
bill= float(input("What was the total bill ? $"))
tippercentage=int(input("How many tip would yuo like to give? 10,12,15 ? "))
person=int(input("How many people to split the bill ? "))
tip=tippercentage/100
totalbill = (bill+(bill*tip))/2
print(f"Ëach person should pay :{totalbill}$")


