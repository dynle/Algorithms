#1) basic for loop
def fibonacci_for(n):
    li = []
    num=0
    for i in range(n+1):
        if i == 0:
            li.append(0)
        elif i == 1:
            li.append(1)
        else:
            num = li[i-2]+li[i-1]
            li.append(num)
    return num


#2) recursive function
def fibonacci_re(n):
    if n < 2:
        return n
    else:
        return fibonacci_re(n-1) + fibonacci_re(n-2)

#3) recursive without for loop
def fibonacci_re_x(n):
    if n <3:
        memo[n] = 1
        return memo[n]
    else:
        if memo[n] != 0:
            return memo[n]
        else:
            memo[n] = fibonacci_re_x(n-1) + fibonacci_re_x(n-2)
            return memo[n]

#4) dynamic programming(dp) iterative
def fibonacci_dp_i(n):
    cache = [0 for _ in range(101)] # Memoization
    cache[1] = 1
    for i in range(2,n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

print(fibonacci_for(7))
print(fibonacci_re(7))
memo = [0] * 8 #If use recursive without for loop, create memo outside of the function
print(fibonacci_re_x(7))
print(fibonacci_dp_i(2))
