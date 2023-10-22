# 0에서 19까지의 i 값으로 반복합니다.
for i in range(20):
    try:
        # 20을 i로 나눈 값을 출력하려고 시도합니다.
        print(20/i)
    except ZeroDivisionError:
        # 만약 0으로 나누는 경우 ZeroDivisionError가 발생하면 예외 처리됩니다.
        print('division by zero error')

#IndexError : 리스트의 인덱스 범위를 넘어갈 때
#NameError : 존재하지 않는 변수를 호출할 때
#ZeroDivisionError : 0으로 숫자를 나눌 때
#ValueError : 변환할 수 없는 문자나 숫자를 변환할 때
#FileNotFoundError : 존재하지 않는 파일을 호출할 때

# IndexError 예외 처리 예제
arr = ['1', '2', '3']
for i in range(0, 5):
    try:
        # arr 리스트의 i번째 요소를 출력하려고 시도합니다.
        print(arr[i])
    except IndexError:
        # 만약 인덱스가 범위를 벗어나는 경우 IndexError가 발생하면 예외 처리됩니다.
        print('Index Error')
    else:
        # 예외가 발생하지 않는 경우 해당 요소를 출력합니다.
        print(arr[i])

# ZeroDivisionError 예외 처리와 finally 블록
try:
    for i in range(1, 20):
        result = 20/i
        print(result)
except ZeroDivisionError:
    # 0으로 나누는 경우 ZeroDivisionError가 발생하면 예외 처리됩니다.
    print('division by zero error')
finally:
    # 예외 발생 여부와 관계없이 항상 실행됩니다.
    print('종료')

# 사용자 정의 예외(ValueError) 발생
while True:
    value = input('숫자 입력: ')
    for c in value:
        if c not in '0123456789':
            # 입력값이 숫자가 아닌 경우 ValueError 예외를 발생시킵니다.
            raise ValueError('숫자 값이 입력되지 않았습니다.')
    else:
        if c == '9':
            break

# assert를 사용한 사용자 정의 예외(ValueError) 발생
def get_binary_number(decimal_number):
    assert isinstance(decimal_number, int)
    # 입력값이 정수가 아닌 경우 AssertionError가 발생합니다.
    return bin(decimal_number)

# 파일 읽기
f = open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt", 'r')
contents = f.read()
print(contents)
f.close()

# with 문을 사용하여 파일 읽기
with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt", 'r') as my_file:
    contents = my_file.read()
    print(type(contents), contents)

# 파일 내용을 줄 단위로 리스트에 저장
with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt", 'r') as my_file:
    contents_list = my_file.readlines()
    print(type(contents_list))
    print(contents_list)

# 파일을 줄 단위로 읽어서 처리
with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt", 'r') as my_file:
    i = 0
    while 1:
        line = my_file.readline()
        if not line:
            break
        print(str(i) + '===' + line.replace('\n', ''))
        i = i + 1

# 파일 내용 분석
with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt", 'r') as my_file:
    contents = my_file.read()
    word_list = contents.split(' ')
    line_list = contents.split('\n')
print('총 글자의 수:', len(contents))
print('총 단어의 수:', len(word_list))
print('총 줄의 수:', len(line_list))

# 파일에 내용 작성
f = open('count_line.txt', 'w', encoding='utf8')
for i in range(1, 11):
    data = '%d번째 줄이다.\n' % i
    f.write(data)
f.close()

# 파일에 내용 추가 작성 (append 모드)
with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/count_line.txt", 'a', encoding='utf8') as f:
    for i in range(11, 20):
        f.write('%d번째 줄이다.\n' % i)

# 디렉토리 및 파일 생성
import os

if not os.path.isdir('log'):
    os.mkdir('log')
if not os.path.exists('log/count_log.txt'):
    f = open("log/count_log.txt", 'w', encoding='utf8')
    f.write('기록이 시작된다\n')
    f.close()

# 로그 파일 작성
with open("log/count_log.txt", 'a', encoding='utf8') as f:
    import random
    import datetime
    for i in range(1, 11):
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + '\t' + str(value) + '값이 생성되었다.\n'
        f.write(log_line)

# Pickle을 사용하여 객체를 직렬화하고 복원
import pickle

# 리스트를 Pickle을 사용하여 파일에 저장
f = open("list.pickle", 'wb')
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pickle.dump(test, f)
f.close()

# Pickle을 사용하여 파일에서 객체를 복원
f = open("list.pickle", 'rb')
test_pickle = pickle.load(f)
print(test_pickle)
f.close()

# 클래스를 Pickle을 사용하여 객체를 저장 및 복원
class Multiply:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):
        return number * self.multiplier

multiply = Multiply(5)

# 객체를 Pickle을 사용하여 파일에 저장
f = open("multiply_object.pickle", 'wb')
pickle.dump(multiply, f)
f.close()

# 파일에서 객체를 복원하고 메서드 호출
f = open("multiply_object.pickle", 'rb')
multiply_pickle = pickle.load(f)
print(multiply_pickle.multiply(5))
f.close()
