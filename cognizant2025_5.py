def countSubarrays(input1, input2, input3):
    
    i=0
    j=input1-1
    count=0
    while i<=j:
        if input3[i]+input3[j]<=input2:
            count+=(j-i) +1
            i=i+1   
        else:
            j=j-1
            
    return count

input1=int(input('size:'))
input2 =int(input('comparison:'))
input3=[]
for i in range(0,input1):
    ele=int(input())
    input3.append(ele)
result = countSubarrays(input1, input2, input3)
print(f'Count of valid subarrays: {result}')