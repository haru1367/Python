#람다(lambda)
print((lambda x,y:x+y)(10,20))

#map(리스트로 부터 원소를 하나씩 꺼내 함수를 적용시켜 새로운 리스트에 담아준다.)
print(list(map(lambda x: x**2,range(5))))

#reduce함수(원소들을 누적으로 함수에 적용시킴)
from functools import reduce
print(reduce(lambda x,y:x+y,[0,1,2,3,4])) #0+1+2+3+4

#filter함수(리스트에 들어있는 원소들을 함수에 적용시켜 결과가 참인값들을 새로운 리스트로 만들어준다.)
print(list(filter(lambda x:x<5,range(10))))

#연습문제 1
def read(text):
    hms = text.split(':')
    ridename = hms[0]
    if str.strip(hms[1]) == '-':
        cmin = None
        cmax = None
    else :
        if '~' in hms[1]:
            hms1 = hms[1].split('~')
            hms1[0] = str.strip(hms1[0])
            hms1[1] = str.strip(hms1[1])
            cmin = hms1[0].replace('cm','')         
            cmax = hms1[1].replace('cm','')
        else :
            hms1 = hms[1].split(' ')
            hms1[1]=str.strip(hms1[1])
            hms1[2]=str.strip(hms1[2])
            if hms1[2] =='이상':
                cmin = hms1[1].replace('cm','')
                cmax = 'None'
            elif hms1[2] == '이하':
                cmin = 'None'
                cmax = hms1[1].replace('cm','')
    return ridename,cmin,cmax

if __name__ == "__main__":
    ridename,cmin,cmax = read(input())
    print("이름:",ridename)
    print("하한:",cmin)
    print("상한:",cmax)
