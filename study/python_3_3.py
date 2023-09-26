#전역변수를 함수안에서 변경
a = 20
def change(x):
    global a
    a = x
change(30)
print(a)
