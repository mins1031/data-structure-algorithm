num = int(input())

data = [1,2]

for i in range(2,num):
    data.append(data[i-1]+data[i-2])

print((data[num-1]) % 10007)

#가장 기본 dp 피보나치임. 그나마 내가 직접 점화식 도출해서 풀었다는데 의의를 두지
#만 기본 DP문제기에 이제 조그마한 감을 잡은 정도라고 생각..
