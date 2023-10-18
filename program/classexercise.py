class Calculator:
    count = 0
    def __init__(self): #생성자
        Calculator.count+=1
        self.count = Calculator.count
        self.result = 0
    def add(self,num):
        self.result += num
        return self.result
    def sub(self,num):
        self.result -= num
        return self.result
    def mul(self,num):
        self.result *= num
        return self.result
    def der(self,num):
        self.result /=num
        return self.result
    
print(Calculator.count) #0
a = Calculator() 
print(Calculator.count) #1
print(a.count) #1
b = Calculator() 
print(Calculator.count) #2
print(a.count) #1
print(b.count) #2

print('a',a.add(4))
print('a',a.add(8))
print('b',b.add(7))
print('b',a.sub(2))
print('b',b.add(3))

class Test:
    count = 0
    def __init__(self,name = '아무개' ,age=19):
        self.name = name
        self.age = age
        Test.count += 1
        self.count = Test.count

    def __str__(self):
        return f'Test class [{self.count}번, {self.name}, {self.age}살]'

t1 = Test('홍길동',20)
print(t1)
t2 = Test('박철수')
print(t2)
t3 = Test()
print(t3)

class Person:
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age=age
        self.gender = gender

    def about_me(self):
        print(f'저의 이름은 {self.name}이고, 나이는{self.age}살, 성별은 {self.gender}입니다')    

class Animal:
    def talk(self):
        print('talk')

class Employee(Person,Animal): # 다중 상속
    def __init__(self,name,age,gender,job,salary,hire_date)->None:
        super().__init__(name,age,gender) # 부모 클래스를 호출하는 함수
        self.job = job
        self.salary = salary
        self.hire_date = hire_date
    def about_me(self):
        super().about_me()
        print(f'{self.job}직이고, 연봉은 {self.salary}, 입사일자는 {self.hire_date}입니다.')

a1 = Employee('홍길동',22,'남자','영업',1200,'2023-01-01')
a1.about_me()
a2 = Person('안정희',33,'여자')
a2.about_me()
