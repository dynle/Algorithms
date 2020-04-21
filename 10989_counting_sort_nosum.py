import sys
#입력으로 들어갈 최대 숫자까지만큼 만들어 줌
count=[0]*10001

len = int(sys.stdin.readline())
#count배열에 해당 숫자의 count를 늘려줌
for _ in range(len):
    v = int(sys.stdin.readline())
    count[v] +=1
#count배열을 다 loop해줘서 count된 만큼 출력해 줌
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            sys.stdout.write(str(i)+"\n")
