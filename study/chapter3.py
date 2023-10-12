age = int(input('당신의 나이는? :'))
if age < 20:
    print("당신은 미성년자 입니다.")
else:
    print('당신은 성인 입니다.')

a = 235
b = 236
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a is b)
print(a is not b)
print(a>=b)
print(a<=b)

a = 152
b = 160
print(a == 152 and b == 153)
print(a>5 or b > 25)
print(not(a>35))

score = int(input('성적입력 : '))
if score >=90: print('A')
elif score >=80 and score <90: print('B')
elif score >=70 and score <80: print('C')
elif score >=60 and score <70: print('D')
else : print('F')

year = int(input('태어난 연도 입력 : '))
age = 2023 - year
if age <= 26 and age >= 20:
    print("대학생")
elif age<20 and age>=17:
    print("고등학생")
elif age<17 and age >= 14:
    print("중학생")
elif age<14 and age >=8:
    print("초등학생")
else:
    print("학생이 아닙니다.")

for i in [1,2,3,4,5,6,7,8,9,10]:
    print("hello")

for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)

for i in range(10):
    print("hello")

for i in 'hello world':
    print(i)

for i in ['ABC','DEF','GHI']:
    print(i)

for i in range(1,52,5):
    print(i)

for i in range(16,3,-2):
    print(i)

i=1
while i<15:
    print(i)
    i += 1

for i in range(15):
    if i==7: break
    print(i)

for i in range(15):
    if i == 5: continue
    print(i)

for i in range(10):
    print(i)
else:
    print("end")

gugudan = int(input('계산할 구구단 단:'))
for i in range(1,10):
    print(gugudan,'*',i,'=',gugudan*i)

string_1 = "good day"
reverse_string = ''
for char in string_1:
    reverse_string = char + reverse_string
print(reverse_string)

decimal = 53
result = ''
while (decimal>0):
    remain = decimal%2
    decimal = decimal//2
    result = str(remain)+result
print(result)

import random
answer = random.randint(1,60)
num = int(input('숫자 입력 : '))
while num != answer:
    if num>answer:
        print('down')
    else:
        print('up')
    num = int(input('숫자 입력'))
else:
    print('정답')

gugudan = int(input('계산할 구구단 단수:'))
while gugudan!=0:
    for i in range (1,10):
        print(gugudan,'*',i,'=',gugudan*i)
    gugudan = int(input('계산할 구구단 단수:'))
else :
    print('구구단 계산 종료')
