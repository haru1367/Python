#while문
num = 1
while num<=100:
    print(num)
    num = num+1

#연습문제 1(사용자에게 정수를 입력받아, 그 수의 제곱을 계산해 출력하는 함수)
num = int(input())
print(num * num)

#연습문제 2(정수를 한개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트)
index = 1
num = int(input())
while index<=num:
    print(index, index*index)
    index = index+1

#연습문제 3(고무공을 100m에서 떨어뜨릴 때 원래높이의 3/5만큼 튀어오름, 열번 튈동안 공의 높이계산)
height = 100
i = 1
while i<=10:
    print(i,round(height*3/5,4))
    i = i+1
    height = height*3/5

