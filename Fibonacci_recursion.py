prev2 = 0
prev1 = 1
count = 2

def fibonacci(prev2, prev1):
    global count
    if count <= 18:
        newFibo = prev2 + prev1
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        fibonacci(prev2, prev1)
    else:
        return 
fibonacci(0,1)