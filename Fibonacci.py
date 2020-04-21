#1) basic for loop
def fabonacci_for(n):
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
def fabonacci_re(n):
    if n < 2:
        return n
    else:
        return fabonacci_re(n-1) + fabonacci_re(n-2)

#3) dynamic programming(dp) iterative
def fabonacci_dp_i(n):
    cache = [0 for _ in range(101)] # Memoization
    cache[1] = 1
    for i in range(2,n+1):
        cache[i] = cache[i-1] + cache[i-2]
    return cache[n]

print(fabonacci_for(7))
print(fabonacci_re(7))
print(fabonacci_dp_i(2))
