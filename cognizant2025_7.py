#generate bill

def generateBill(i1,i2,i3):
    return i1*100 + i2 *20 + i3 *10

i1=int(input('enter i1:'))
i2=int(input('enter i2:'))
i3=int(input('enter i3:'))
result = generateBill(i1,i2,i3)
print(f'total price: {result}')
