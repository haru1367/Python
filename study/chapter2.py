# 사용자로부터 이름 입력 받기
print("이름을 입력하세요 : ")
name = input()
print("Hello!", name, "nice to meet you~")

# 사용자로부터 키 입력 받기 (실수로 변환)
print("키를 입력해주세요 : ")
tall = float(input())
print("당신의 키는", tall, "입니다.")

# 사용자로부터 섭씨 온도 입력 받기
print("변환할 섭씨 온도를 입력해주세요 : ")
celsius = input()
fahrenheit = float(celsius) * 1.8 + 32
print("섭씨온도 :", celsius)
print("화씨온도 :", fahrenheit)

# 리스트 선언과 사용
colors = ['red', 'blue', 'green']
print(colors[0])  # 리스트 요소 출력
print(colors[2])
print(len(colors))  # 리스트의 길이 출력

cities = ['서울', '인천', '부산', '대전', '대구', '광주', '수원', '울산']
print(cities[0:6])  # 리스트의 슬라이싱
print(cities[5:])
print(cities[-8:])
print(cities[-50:50])
print(cities[::2])  # 간격을 두고 출력
print(cities[::-1])  # 역순 출력

# 리스트 연산 및 조작
list1 = ['A', 'B', 'C']
list2 = ['D', 'E', 'F']
len(list1)  # 리스트의 길이
total_list = list1 + list2  # 리스트 합치기
print(total_list)
print(list1 * 3)  # 리스트 반복
print('B' in list1)  # 항목 존재 여부 확인

list = ['a', 'b', 'c']
list.append('d')  # 리스트에 항목 추가
print(list)
list.extend(['e', 'f'])  # 다른 리스트 추가
print(list)
list.insert(0, 'z')  # 특정 위치에 항목 추가
print(list)
list.remove('z')  # 항목 삭제
print(list)
list[0] = "h"  # 항목 변경
print(list)
del list[0]  # 항목 삭제
print(list)

# 리스트 언패킹
t = [1, 2, 3]
a, b, c = t
print(a, b, c)

# 2차원 리스트
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)

# 리스트 내의 리스트
a = ["color", 1, -5.2]
color = ['yellow', 'blue', 'green', 'black', 'purple']
a[0] = color
print(a)

# 리스트 할당 및 정렬
list1 = [5, 4, 3, 2, 1]
list2 = [1, 2, 3, 4, 5]
list2 = list1  # list2가 list1을 참조
print(list2)
list1.sort()  # list1 정렬
print(list1)
list2 = [6, 7, 8, 9, 10]  # list2에 새로운 리스트 할당
print(list1, list2)