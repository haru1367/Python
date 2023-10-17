'''
반장선거에서 투표한 후보자 번호들을 공백을 구분자로 하여 입력하면
각 값들을 분리하고 분리한 값들은 숫자로 변경하여
각 숫자별로 같은 값의 갯수를 체크해 출력하는 프로그램
함수는 아래와 같이 작성
- 공백을 구분자로 하여 입력받은 후보자 번호를 분리하는 함수
- 숫자로 변경된 값들의 항목별로 갯수를 카운트 하는 함수
- 결과값을 출력하는 함수
입력예 -> 1 2 3 5 3 4 2 1 2
출력예 -> 기호 : 1 득표수 : 2
'''
# def sort_by_key(t):
#     return t[0]
# from collections import Counter
# data = list(input('선거 결과를 입력해주세요 : ').split())
# c = dict(Counter(data))
# for k,v in dict(sorted(c.items(),key=sort_by_key)).items():
#     print('기호 : {} 득표수 : {}'.format(k,v))

def sort_by_key(t):
    return t[0]

def str2int(data):
    result = list(data.split())
    result1 = []
    for i in range(0,len(result)):
        result1.append(int(result[i]))
    return result1

def countvotes(result):
    c = {}
    for i in range(0,len(result)):
        c[result[i]] = 0
    for i in range(0,len(result)):
        c[result[i]] += 1
    return c

def printresult(c):
    for k,v in dict(sorted(c.items(),key=sort_by_key)).items():
        print('기호 : {} 득표수 : {}'.format(k,v))

data = input('선거 결과 입력 : ')
result = str2int(data)
c = countvotes(result)
printresult(c)