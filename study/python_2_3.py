#리스트에서 for문
family = ['mother','father','gentleman','sexy lady']
for x in family:
    print(x,len(x))

#range()
print(list(range(2,7)))
a = [4,5,6,7]
for i in a:
    print(i)

#연습문제 1(입력받은 숫자만큼 반복하기)
num = int(input())
for i in range(1,num+1):
    print(num)

#연습문제 2(제곱표)
num = int(input())
for i in range(1,num+1):
    print(i, i*i)

#연습문제 3(화학 실험실)
safe_min_temp = int(input())
safe_max_temp = int(input())
while True:
    temp = int(input())
    if temp == -999:
        break
    elif (temp >=safe_min_temp and temp <= safe_max_temp):
        print('Nothing to report')
    else :
        print('Alert!')
        break
