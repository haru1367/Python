#함수
a_list = [1,2,3,4,5]
def print_list(a):
    for i in a:
        print(i)
print_list(a_list)

def boy():
    print('I am a boy.')
    print('You are a girl.')
boy()

#연습문제 1(자릿수를 구하는 함수 만들기)

def numofDigits(a):
    num=0
    while a>0:
        num+=1
        a = a//10
        if a==0:
            print(num)
numofDigits(1234567890)

#연습문제 2(구구단)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}')
        
