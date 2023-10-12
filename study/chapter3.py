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

