# def Rec_area(x,y):
#     return x*y

# rectangle_x = 10
# rectangle_y = 5
# print('사각형의 넓이 : ',Rec_area(rectangle_x,rectangle_y))

# def f(x):
#     return 5*x - 7
# def g(x):
#     return x**3+5
# x = 3
# print(f(x)+g(x)+f(g(x)+g(f(x))))

# def classroom(student):
#     student.append(7)
# study = [1,2,3,4,5,6]
# classroom(study)
# print(study)

# def f():
#     global s
#     s = "I love London!"
#     print(s)
# s = "I love Paris!"
# print(s)

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(int(input('n팩토리얼 구하기:'))))

# def exercise_f(name1, name2):
#     print('Hello {0}, My name is {1}'.format(name2,name1))
# exercise_f('abc','def')

# def exercise_f1(name1,name2 = 'def'):
#     print('hello {0}, my name is {1}'.format(name1,name2))
# print(exercise_f1('abc'))

# def asterisk_test(a,b,*args):
#     print(args)
#     return a+b+sum(args)
# print(asterisk_test(1,2,3,4,5))

# def asterisk_test_2(*args):
#     x,y,*z = args
#     return x,y,z
# print(asterisk_test_2(3,4,5))
