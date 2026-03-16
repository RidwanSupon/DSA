array = [12,9,5,6,1,78,13]
minVal = array[0]
secondMin = float('inf')

for i in array:
    if i < minVal:
        secondMin = minVal
        minVal = i
    elif i < secondMin and i != minVal:
        secondMin = i
print(secondMin)