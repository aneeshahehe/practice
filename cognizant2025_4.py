# create the pyramid pattern

def pyramidStar(n):  
    for i in range(n):
        spaces = ' ' * i 
        stars = '*' * (2*(n-i)-1)
        print(spaces + stars)

n = int(input('enter n:'))
pyramidStar(n)