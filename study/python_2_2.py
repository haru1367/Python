#if else문
a = 1234 *4
b = 13456 / 2
if a>b:
    print('a')
else:
    print('b')

#elif문
c = 75
d = 75
if c>d:
    print('c is greater than d')
elif c == d:
    print('c is equal to d')
elif c<d:
    print('c is less than d')
else:
    print('I don\'t know')

#나머지 계산을 이용하는 if 문
a = 48
b= 4
if a%b == 0:
    print(f'{a}는 {b}로 나누어 떨어집니다.')
elif a%b != 0:
    print(f'{a}는 {b}로 나누어 떨어지지 않습니다.')

#조건에 따라 반복문 중단하기
max = 10
while True:
    num = int(input())
    if num>max:
        print(num,'is too big!')
        break

#if 문에 and/or를 사용
s = 'banana'
if 'a' in s and 'b' in s:
    print('banana 에는 a와 b가 모두 있습니다')

if 'a' in s or 'n' in s:
    print('banana 에는 a 또는 n이 있습니다')

        
#연습문제 1(숫자읽기(1~3))
num = int(input())
if num==1:
    print('일')
elif num ==2:
    print('이')
else :
    print('삼')
    
#연습문제 2(나이에 따른 세대)
num = int(input('태어난 연도는 : '))
if num<=1924:
    print('you are The Greatest Generation')
elif num>=1925 and num<=1945:
    print('you are The Silent Generation')
elif num>=1946 and num<=1964:
    print('you are baby boomer')
elif num>=1965 and num<=1980:
    print('you are Generation X')
elif num>=1981 and num<=1996:
    print('you are millennial')
else :
    print('you are Generation Z')

#연습문제 3(단위 기호)
num = int(input('단위 기호 숫자 입력 : '))
print(str(num//1000000)+'M',sep = "")

#연습문제 4(양수만 덧셈하기)
sum =0
while True:
    num = int(input('정수를 입력하세요 : '))
    if num>0:
        sum = sum + num
    else :
        print(sum)
        break

#연습문제 5(윤년 판별하기)
year = int(input('윤년인지 판별할 연도를 입력해주세요 : '))
if (year%4 == 0 or year%400 ==0) and (year%100!=0) :
    print(f'{year} 연도는 윤년입니다.')
else :
    print(f'{year} 연도는 평년입니다.') 
