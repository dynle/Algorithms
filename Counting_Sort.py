def countingSort(list):
    max_num = 10000

    #a length of the original list
    N = len(A)

    count = [0]*(max_num+1)
    countSum = [0]*(max_num+1)

    # count each num
    for i in range(0,N):
        count[A[i]] +=1

    #sum list
    countSum[0]=count[0]
    for i in range(1,max_num+1):
        countSum[i] = countSum[i-1]+count[i]

    #new list
    B = [0]*(N+1)
    for i in range(N-1,-1,-1):
        B[countSum[A[i]]] = A[i]
        countSum[A[i]] -=1

    #print
    for i in B[1:]:
        print(i)

#original list
length=int(input())
A=[0]*length

for i in range(length):
    A[i] = int(input())
countingSort(A)
