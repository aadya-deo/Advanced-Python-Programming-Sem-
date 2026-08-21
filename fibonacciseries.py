# recursive function -> memoization approach without storage of subpart values 
def fiboRecur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fiboRecur(n-1)+fiboRecur(n-2)
    
# iterative function -> tabulation approach without storage of subpart values
def fiboIter(n):
    prev_n = 0
    curr_n = 1
    for i in range(1,n):
        prevPrev_n = prev_n 
        prev_n = curr_n
        curr_n = prevPrev_n + prev_n
    return curr_n

n = int(input("Enter the number: "))
print(f"Using recursion, value for fibo({n}) is {fiboRecur(n)}")
print(f"Using iteration, value for fibo({n}) is {fiboIter(n)}")
