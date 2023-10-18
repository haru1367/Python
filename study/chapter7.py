# 파이썬 스타일 코드

# 리스트의 항목을 문자열로 연결
colors = ['red', 'blue', 'green', 'yellow']
result = ''.join(colors)
print(result)

# 문자열을 구분자로 분리하고 다시 결합
example = 'python,jquery,javascript'
example.split(",")
print(example)

a, b, c = example.split(",")
print(a, b, c)

# 문자열을 점을 기준으로 분리
example = 'theteamlab.univ.edu'
subdomain, domain, tld = example.split('.')
print(subdomain, domain, tld)

# 리스트의 항목을 공백으로 연결
result = ' '.join(colors)
print(result)

# 리스트의 항목을 쉼표와 공백으로 연결
result = ', '.join(colors)
print(result)

# 리스트의 항목을 하이픈으로 연결
result = '-'.join(colors)
print(result)

# 리스트 컴프리헨션을 사용한 리스트 생성
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 == 0]
print(result)

result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)

# 두 문자열에서 모든 조합 생성
word_1 = 'Hello'
word_2 = 'World'
result = [i + j for i in word_1 for j in word_2]
print(result)

# 두 리스트에서 같은 요소가 아닌 모든 조합 생성
case_1 = ['A', 'B', 'C']
case_2 = ['D', 'E', 'A']
result = [i + j for i in case_1 for j in case_2 if not (i == j)]
print(result)

# 문장을 공백으로 분리하고 각 단어에 대한 대문자, 소문자, 길이 정보 리스트 생성
words = 'The quick brown fox jumps over the lazy dog'.split()
stuff = [[w.upper(), w.lower(), len(w)] for w in words]
print(stuff)

# 두 리스트의 각 항목을 더하여 2차원 리스트 생성
result = [[i + j for i in case_1] for j in case_2]
print(result)

# enumerate를 사용하여 리스트의 인덱스와 값 출력
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# 두 리스트의 항목을 짝지어 출력
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)

# 여러 튜플에서 같은 위치의 항목 더하기
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)
print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])

# enumerate와 zip을 함께 사용하여 인덱스와 두 리스트의 항목 출력
for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)