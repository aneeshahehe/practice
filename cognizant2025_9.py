def pattern(n):
    for i in range(n):
        stars = '*'*(i+1)

        print(stars)
    
n=int(input('enter n:'))
pattern(n)