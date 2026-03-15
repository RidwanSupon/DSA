prev2 = 0
prev1 = 1
print(prev2)
print(prev1)

for fibo in range(18):
    newFibo = prev2 + prev1
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo
