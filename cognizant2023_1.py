# Write a program to calculate the fuel consumption of your truck.The program should ask the user to enter the quantity of diesel to fill up the tank and the distance covered till the tank goes dry.
# Calculate the fuel consumption and display it in the format (liters per 100 kilometers).
import sys
print('enter quantity')
quant=int(input())
print('enter distance')
dist=int(input())

if (quant>0 and dist>0):
    fuel_cons_inlithun = (quant/dist)*100
    print("fuel consumption in litre/km:")
    print(round(fuel_cons_inlithun,2))

    dis_to_miles=dist*0.624
    quant_to_gallons=quant*0.2642

    fuel_cons_ingalhun = (quant_to_gallons/dis_to_miles) *100

    print("fuel consumption in gallons/miles")
    print(round(fuel_cons_ingalhun,2))

if (quant<=0 or dist<=0):
    print('invalid input')

