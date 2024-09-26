#check prime or not -- Happy Number


def is_Prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n %i==0:
            return False
    return True



def printPrime(a,b):
    if a>=0 and b>=0 and a<=b:
        for num in range(a,b+1):
            if is_Prime(num):
                print(num, end=' ')
    else:
          print('invalid number')


a=int(input())
b=int(input())
printPrime(a,b)