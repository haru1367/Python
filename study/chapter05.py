a = 'abcde'
print(a[0], a[4])       # 'a'와 'e'를 출력합니다.
print(a[-1], a[-5])     # 'e'와 'a'를 출력합니다.

a = 'hello world study python'
print(a[0:6], a[-9:])    # 인덱스 0부터 5까지의 부분 문자열과 뒤에서부터 9번째 문자부터 끝까지의 부분 문자열을 출력합니다.
print(a[:])              # 문자열 'a' 전체를 출력합니다.
print(a[-50:50])        # 문자열 'a' 전체를 출력합니다. (음수 인덱스는 오류를 발생시키지 않습니다)
print(a[::2], a[::-1])  # 'a'의 모든 두 번째 문자와 문자열을 역순으로 출력합니다.

a = 'hello'
b = 'world'
print(a + ' ' + b)      # 'a'와 'b'를 사이에 공백을 두고 연결하여 출력합니다.
print(a * 2 + ' ' + b * 2)  # 'a'와 'b'를 반복하여 연결하고 그 사이에 공백을 두어 출력합니다.
if 'h' in a:            # 'a'에 'h'가 포함되어 있는지 확인하고, 그에 따라 'a' 또는 'b'를 출력합니다.
    print(a)
else:
    print(b)

# 다양한 문자열 메서드:
title = 'study python!'
print(title.upper())         # 대문자로 변환합니다.
print(title.lower())         # 소문자로 변환합니다.
print(title.title())         # 각 단어의 첫 글자를 대문자로 변환합니다.
print(title.capitalize())     # 첫 글자를 대문자로 변환합니다.
print(title.count('t'))      # 't'의 출현 횟수를 세어 출력합니다.
print(title.upper().count('o'))  # 대문자로 변환한 후 'o'의 출현 횟수를 세어 출력합니다.
print(title.isdigit())       # 문자열이 숫자로 이루어져 있는지 확인합니다.
print(title.startswith('s'))  # 문자열이 's'로 시작하는지 확인합니다.

# 파일을 읽어와서 출현 횟수를 세는 예제:
f = open("C:/Users/haru1367/Desktop/coding깃허브/Python/study/oceans.txt", 'r')
oceans_lyric = f.readlines()
f.close()
contents = ""
for line in oceans_lyric:
    contents = contents + line.strip() + '\n'
n_of_oceans = contents.upper().count('YOU')
print("단어 'You'의 출현 횟수:", n_of_oceans)
print(oceans_lyric)

# 문자열 형식 지정 방법의 다양한 예제:
print(1, 2, 3)
print('a' + '' + 'b' + '' + 'c')
print('%d %d %d' % (1, 2, 3))
print('{}{}{}'.format('a', 'b', 'c'))
a = 1
b = 2
c = 3
print(f'{a} {b} {c}')
print('%s %s' % ('one', 'two'))
print('%d %d' % (1, 2))

# 문자열 형식 지정자를 사용한 예제:
print('I eat %d apples' % 3)
print('I eat %s apples' % 'five')

# 값을 사용하여 문자열 형식 지정:
number = 3
day = 'three'
print('나는 %d개의 사과를 먹었어. 나는 %s일 동안 아팠어.' % (number, day))

# format 메서드를 사용한 문자열 형식 지정의 다양한 방법:
print("나는 {}살이야.".format(20))
age = 40
name = '홍길동'
print("나는 {}살이야.".format(age))
print("내 이름은 {}이고 {}살이야.".format(name, age))
print("제품: {}, 단가: {:.2f}.".format("사과", 5.243))

# 다양한 문자열 형식 지정 방법:
print('%10d' % 12)
print('%-10d' % 12)
print('%10.3f' % 5.94343)
print('%10.2f' % 5.94343)
print('%-10.2f' % 5.94343)

# 정렬 지정자를 사용한 문자열 형식 지정:
print('{:>10s}'.format('Apple'))
print('{:<10s}'.format('apple'))
print('{:^10s}'.format('apple'))

# 딕셔너리를 사용한 문자열 형식 지정:
print('Product:%(name)5s,Price per unit : %(price)5.5f.' % {'name': '사과', 'price': 5.243})