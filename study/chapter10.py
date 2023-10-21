import random

print(random.randint(1,1000))
print(random.randint(0,100))
print(random.random())

import time
print(time.localtime())

import urllib.request
response = urllib.request.urlopen('https://harucode.tistory.com')
print(response.read())

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
