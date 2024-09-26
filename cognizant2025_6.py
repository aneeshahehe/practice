# minimum number of segment to remove so that all the members are wearing formal

def formalNumber(input1, input2):
    i=0
    j=input1-1
    count=0
    found = False
    # to change only the first I to F
    while i<input1: 
        if input2[i]=='I':
            if found:
                break
            else:
                found = True
        i=i+1

    while j>=i:
        if input2[j]=='I':
            break
        j=j-1

    if found:
        count = j-i+1
    else:
        count = 0

    return count

# input1 = int(input('enter N:'))
# print("string of I's and F's")
# for i in range(0,input1):
#     input2 = input()  

# result = formalNumber(input1, input2)
# print(f'the number is:{result}')

# Taking input correctly
input1 = int(input('Enter N (length of the string): '))
print("Enter a string of I's and F's (without spaces):")

# Take a single string input
input2 = input()

# Make sure input2 length matches input1
if len(input2) != input1:
    print(f"Error: The input string length must be {input1}.")
else:
    result = formalNumber(input1, input2)
    print(f'The number of segments to remove is: {result}')











# input1= int(input('enter N:'))
# elements = input('enter elements:')
# input2 = elements.split(',')