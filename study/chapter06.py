#STACK 자료구조 
a = [1,2,3,4,5]
a.append(10)
print(a)
a.append(20)
print(a)
print(a.pop())
print(a.pop())

word = input('Input a word : ')
word_list = list(word)
print(word_list)
result = []
for i in range(len(word_list)):
    result.append(word_list.pop())
print(result)

#QUEUE 자료구조
a = [1,2,3,4,5]
a.append(10)
a.append(20)
print(a)
print(a.pop(0))
print(a.pop(0))
print(a)

#TUPLE 자료구조
t = (1,2,3)
print(t+t+t,t*3)
t = (3,)
print(t)

#SET 자료구조
s = set([1,2,3,1,2,3])
print(s)
s.add(1)
print(s)
s.remove(1)
print(s)
s.update([1,4,5,6,7])
print(s)
s.discard(3)
print(s)
s.clear()
print(s)

s1 = set([1,2,3,4,5])
s2 = set([3,4,5,6,7])
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)
print(s1.difference(s2))
print(s1-s2)

#tuple 자료구조
student_info = {20153201:'A', 20165945:'B',20148435:'C'}
print(student_info[20153201])
student_info[20143201] = 'D'
print(student_info.keys())
print(student_info.values())
print(student_info.items())

for k,v in student_info.items():
    print("Key:",k)
    print('Value:',v)

print(20153201 in student_info.keys())

#deque모듈
from collections import deque
deque_list = deque()
for i in range(10):
    deque_list.append(i)
print(deque_list)
print(deque_list.pop())

deque_list1 = deque()
for i in range(10):
    deque_list1.appendleft(i)
print(deque_list1)
print(deque_list1.pop())

deque_list1 = deque()
for i in range(10):
    deque_list1.appendleft(i)
print(deque_list1)
deque_list1.rotate(2)
print(deque_list1)
deque_list1.rotate(3)
print(deque_list1)

print(reversed(deque_list1))
deque_list1.extend([10,11,12])
deque_list1.extendleft([13,14,15])
print(deque_list1)

#OrderedDict 모듈
from collections import OrderedDict
d = OrderedDict()
d['a'] = 100
d['b'] = 200
d['y'] = 500
d['f'] = 400
for k,v in d.items():
    print(k,v)

def sort_by_key(t):
    return t[0]

def sort_by_value(t):
    return t[1]

d = dict()
d['x'] = 400
d['y'] = 200
d['z'] = 300
d['f'] = 600

for k,v in dict(sorted(d.items(),key=sort_by_key)).items():
    print(k,v)

print('')
for k,v in OrderedDict(sorted(d.items())).items():
    print(k,v)

print('')
for k,v in dict(sorted(d.items(),key=sort_by_value)).items():
    print(k,v)

print('')
for k,v in OrderedDict(sorted(d.items()),key=sort_by_value).items():
    print(k,v)

#defaultdict 모듈
from collections import defaultdict
d = defaultdict(lambda:0)
print(d["first"])

s = [('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d = defaultdict(list)
for k,v in s:
    d[k].append(v)
print(d.items())

#Counter모듈
from collections import Counter
text = list('gallahad')
print(text)
c = Counter(text)
print(c)

c = Counter({'red':4,'blue':2})
print(c)
print(list(c.elements()))

c = Counter(cats = 4, dogs = 8)
print(list(c.elements()))

c= Counter(a=4,b=2,c=0,d=-2)
d= Counter(a=1,b=2,c=3,d=4)
print(c-d)
print(c+d)
print(c&d)
print(c|d)

#namedtuple모듈
from collections import namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(11,y=22)
print(p)
print(p.x,p.y)
print(p[0] + p[1])

text = '''A press release is the quickest and easiest way to get gree publicity.
If well written, a press release can result in multiple published articles about
your firm and its products. and that can mean new prospects contacting you asking
you to sell to them.'''.lower().split()

from collections import defaultdict

word_count = defaultdict(lambda:0)
for word in text:
    word_count[word] += 1
from collections import OrderedDict
for i,v in OrderedDict(sorted(word_count.items(),key = lambda t:t[1],reverse=True)).items():
    print(i,v)