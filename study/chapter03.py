# 나이를 입력받아, 미성년자와 성인 여부를 확인합니다.
age = int(input('당신의 나이는? :'))
if age < 20:
    print("당신은 미성년자 입니다.")
else:
    print('당신은 성인 입니다.')

# 두 개의 숫자를 비교하고, 다양한 비교 연산의 결과를 출력합니다.
a = 235
b = 236
print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a is b)        # 객체 동일성 확인 (정수에 대해서는 거의 True가 나오지 않을 것입니다)
print(a is not b)    # 객체 동일성 확인 (정수에 대해서는 거의 True가 나오지 않을 것입니다)
print(a >= b)
print(a <= b)

a = 152
b = 160
print(a == 152 and b == 153)
print(a > 5 or b > 25)
print(not(a > 35))

# 사용자로부터 성적을 입력받고, 성적에 따라 학점을 출력합니다.
score = int(input('성적입력 : '))
if score >= 90:
    print('A')
elif score >= 80 and score < 90:
    print('B')
elif score >= 70 and score < 80:
    print('C')
elif score >= 60 and score < 70:
    print('D')
else:
    print('F')

# 사용자로부터 태어난 연도를 입력받고, 나이를 계산하여 학생의 학년을 확인합니다.
year = int(input('태어난 연도 입력 : '))
age = 2023 - year
if age <= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 17 and age >= 14:
    print("중학생")
elif age < 14 and age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")

# 리스트에 있는 값들을 반복하며 "hello"를 출력합니다.
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print("hello")

# 리스트에 있는 값들을 반복하며 각 값을 출력합니다.
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    print(i)

# 범위를 사용한 반복문을 통해 "hello"를 출력합니다.
for i in range(10):
    print("hello")

# 문자열을 반복문을 통해 한 글자씩 출력합니다.
for i in 'hello world':
    print(i)

# 리스트에 있는 문자열들을 반복문을 통해 출력합니다.
for i in ['ABC', 'DEF', 'GHI']:
    print(i)

# 범위와 스텝을 활용하여 숫자를 반복하여 출력합니다.
for i in range(1, 52, 5):
    print(i)

# 역순으로 범위를 활용하여 숫자를 반복하여 출력합니다.
for i in range(16, 3, -2):
    print(i)

# while 반복문을 사용하여 숫자를 출력합니다.
i = 1
while i < 15:
    print(i)
    i += 1

# break문을 사용하여 반복문을 중단시킵니다.
for i in range(15):
    if i == 7:
        break
    print(i)

# continue문을 사용하여 반복문을 스킵합니다.
for i in range(15):
    if i == 5:
        continue
    print(i)

# 반복문에 else 블록을 사용하여 반복문 종료 후 "end"를 출력합니다.
for i in range(10):
    print(i)
else:
    print("end")

# 사용자로부터 입력받은 숫자에 대한 구구단을 출력합니다.
gugudan = int(input('계산할 구구단 단:'))
for i in range(1, 10):
    print(gugudan, '*', i, '=', gugudan * i)

# 문자열을 역순으로 출력합니다.
string_1 = "good day"
reverse_string = ''
for char in string_1:
    reverse_string = char + reverse_string
print(reverse_string)

# 10진수를 2진수로 변환하여 출력합니다.
decimal = 53
result = ''
while decimal > 0:
    remain = decimal % 2
    decimal = decimal // 2
    result = str(remain) + result
print(result)

# 무작위 숫자를 생성하고, 사용자가 그 숫자를 맞출 때까지 "up" 또는 "down"을 출력합니다.
import random
answer = random.randint(1, 60)
num = int(input('숫자 입력 : '))
while num != answer:
    if num > answer:
        print('down')
    else:
        print('up')
    num = int(input('숫자 입력'))
else:
    print('정답')

# 사용자로부터 입력받은 숫자에 대한 구구단을 출력하고, 0을 입력할 때까지 반복합니다.
gugudan = int(input('계산할 구구단 단수:'))
while gugudan != 0:
    for i in range(1, 10):
        print(gugudan, '*', i, '=', gugudan * i)
    gugudan = int(input('계산할 구구단 단수:'))
else:
    print('구구단 계산 종료')
