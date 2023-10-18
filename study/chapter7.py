#파이썬 스타일 코드
colors = ['red','blue','green','yellow']
result = ''.join(colors)
print(result)

#문자열 분리 및 결합
example = 'python,jquery,javascript' 
example.split(",")
print(example)

a,b,c = example.split(",")
print(a,b,c)

example = 'theteamlab.univ.edu'
subdomain, domain, tld = example.split('.')
print(subdomain,domain,tld)

result = ' '.join(colors)
print(result)

result = ', '.join(colors)
print(result)

result = '-'.join(colors)
print(result)

#리스트 컴프리헨션(list comprehension)
result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i%2 == 0]
print(result)

result = [i if i % 2 == 0 else 10 for i in range(10)]
print(result)

word_1 = 'Hello'
word_2 = 'World'
result = [i+j for i in word_1 for j in word_2]
print(result)

case_1 = ['A','B','C']
case_2 = ['D','E','A']
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)
stuff = [[w.upper(),w.lower(),len(w)] for w in words]
print(stuff)

result = [[i+j for i in case_1] for j in case_2]
print(result)

#다양한 방식의 리스트값 출력
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a, b in zip(alist,blist):
    print(a,b)

a,b,c = zip((1,2,3),(10,20,30),(100,200,300))
print(a,b,c)
print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))])

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)
