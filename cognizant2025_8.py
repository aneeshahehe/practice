#palindrome

def isPalindrome(n):

    if n<0:
        print('invalid input')
        return
    n_str= str(n)
    
    i = 0
    j=len(n_str)-1
    
    while i<=j:
        if n_str[i] != n_str[j]:
            print('not palindrome')
            return
        i+=1
        j-=1

        
    print('it is palindrome')

n=int(input('enter number:'))
isPalindrome(n)