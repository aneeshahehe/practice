# #sort array on the basis of frequency from higher to lower
# #The line of code arr = list(map(int, input().split(" "))) is a Python statement that processes user input and converts it into a list of integers.
# input(): This function prompts the user to enter a string of text. By default, it waits for the user to press Enter after typing.
# .split(" "): This method takes the input string and splits it into a list of substrings based on spaces. If the user types 1 2 3, it will create a list like ['1', '2', '3'].
# map(int, ...): The map function applies the int function to each element of the list created by split(). This converts each substring (which is still in string format) into an integer.
# list(...): Finally, list() takes the result from map, which is an iterable, and converts it into a list.
# So, if a user inputs 1 2 3, the final output will be the list [1, 2, 3].

#comparator function
from collections import Counter
def sort_key(x):
    return -x[1],x[0]

#array to store elements as individuals
arr= list(map(int,input().split(" ")))
freq=Counter(arr)
#store a list that has two elements, but on the basis of the comparator key

freq_list.sort(key=sort_key)
#ans only contains num part of the list
ans= [num for num,freq in freq_list]

print(ans)