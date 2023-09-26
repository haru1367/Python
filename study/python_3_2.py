#반환 함수
def f1(x):
    a = 3
    b =5
    y = a*x + b
    return y
c = f1(10)
print(c)

#연습문제 1번(숫자 읽기 함수 1~10)
def korean_number(x):
    match x:
        case 1:
            print('일')
        case 2:
            print('이')
        case 3:
            print('삼')
        case 4:
            print('사')
        case 5:
            print('오')
        case 6:
            print('육')
        case 7:
            print('칠')
        case 8:
            print('팔')
        case 9:
            print('구')
        case 10:
            print('십')
num = int(input())
korean_number(num)

#연습문제 2번(triple함수)
def triple(x):
    return x*3
print(triple(2))
print(triple('x'))

#연습문제 3번(한국나이 반환함수)
from datetime import datetime
today = datetime.today()
year = today.year
birth_year = int(input())
def korean_age(x):
    return year - birth_year + 1
print(korean_age(birth_year))

#연습문제 4번(단리 이자 계산)
def simple_interest(p,r,t):
    return p*r*t
print(simple_interest(10000000,0.03875,5))

#연습문제 5번(단리 원리금 계산)
def simple_interest_amount(p,r,t):
    return p * (1 + r*t)
print(simple_interest(1100000,0.05,5/12))

#연습문제 6번(복리 원리금 계산)
def compound_interest_amount(p,r,t,n):
    return p*(1+r/n)**(n*t)
print(compound_interest_amount(1500000,0.043,6,1/2))
