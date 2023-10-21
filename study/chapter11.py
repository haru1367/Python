# for i in range(20):
#     try:
#         print(20/i)
#     except ZeroDivisionError:
#         print('division by zero error')

# #IndexError : 리스트의 인덱스 범위를 넘어갈 때
# #NameError : 존재하지 않는 변수를 호출할 때
# #ZeroDivisionError : 0으로 숫자를 나눌 때
# #ValueError : 변환할 수 없는 문자나 숫자를 변환할 때
# #FileNotFoundError : 존재하지 않는 파일을 호출할 때

# arr = ['1','2','3']
# for i in range(0,5):
#     try:
#         arr[i]
#     except IndexError:
#         print('Index Error')
#     else:
#         print(arr[i])

# try:
#     for i in range(1,20):
#         result = 20/i
#         print(result)
# except ZeroDivisionError:
#     print('division by zero error')
# finally:
#     print('종료')

# while True:
#     value = input('숫자입력: ')
#     for c in value:
#         if c not in '0123456789':
#             raise ValueError('숫자값이 입력되지 않았습니다.')
#     else:
#         print(int(value))

# def  get_binary_number(decimal_number):
#     assert isinstance(decimal_number,int)
#     return bin(decimal_number)
# print(get_binary_number(10))
# print(get_binary_number('10'))

# f = open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt",'r')
# contents = f.read()
# print(contents)
# f.close()

# with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt",'r') as my_file:
#     contents = my_file.read()
#     print(type(contents),contents)

# with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt",'r') as my_file:
#     contents_list = my_file.readlines()
#     print(type(contents_list))
#     print(contents_list)

# with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt",'r') as my_file:
#     i = 0
#     while 1:
#         line = my_file.readline()
#         if not line:
#             break
#         print(str(i)+'==='+line.replace('\n',''))
#         i = i+1

# with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/oceans.txt",'r') as my_file:
#     contents = my_file.read()
#     word_list=contents.split(' ')
#     line_list=contents.split('\n')
# print('총 글자의 수 : ', len(contents))
# print('총 단어의 수 : ', len(word_list))
# print('총 줄의 수:', len(line_list))

# f = open('count_line.txt','w',encoding = 'utf8')
# for i in range(1,11):
#     data = '%d번째 줄이다.\n'%i
#     f.write(data)
# f.close()

# with open("C:/Users/jsk03/Desktop/vscodeGithub/Python/study/count_line.txt",'a',encoding='utf8') as f:
#     for i in range(11,20):
#         f.write('%d번째 줄이다.\n'%i)

import os
os.mkdir('log')

