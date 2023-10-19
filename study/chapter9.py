class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name  # 선수 이름
        self.position = position  # 포지션
        self.back_number = back_number  # 등번호

    def change_back_number(self, back_number):
        self.back_number = back_number  # 등번호 변경 메서드

    def __str__(self):
        return f'안녕하세요, 제 이름은 {self.name}이고, 포지션은 {self.position}이며, 등번호는 {self.back_number}입니다.'

messi = SoccerPlayer('Messi', 'CF', 10)
print(messi)
messi.change_back_number(30)
print(messi)

names = ['이강인', '손흥민', '정우영']
positions = ['CM', 'ST', 'LF']
numbers = [18, 7, 9]

players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]

player_objects = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
for i in range(0, len(names)):
    print(player_objects[i])


class Note:
    def __init__(self, contents=None):
        self.contents = contents  # 노트 내용

    def write_contents(self, contents):
        self.contents = contents  # 내용 작성 메서드

    def remove_all(self):
        self.contents = ''  # 모든 내용 삭제 메서드

    def __str__(self):
        return self.contents

class Notebook:
    def __init__(self, title):
        self.title = title  # 노트북 제목
        self.page_number = 1  # 현재 페이지 번호
        self.notes = {}  # 노트 저장을 위한 딕셔너리

    def add_note(self, note, page=0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note  # 노트 추가 메서드
                self.page_number += 1
            elif self.page_number > 0 and self.page_number < 300:
                self.notes = {page: note}
                self.page_number += 1
            else:
                print('페이지가 모두 채워졌다.')

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)  # 노트 삭제 메서드
        else:
            print('해당 페이지는 존재하지 않습니다.')

    def get_number_of_pages(self):
        return len(self.notes.keys())  # 노트북의 페이지 수 반환 메서드

class Person:
    def __init__(self, name, age, gender):
        self.name = name  # 이름
        self.age = age  # 나이
        self.gender = gender  # 성별

    def about_me(self):
        print("제 이름은", self.name, "이고요, 제 나이는", str(self.age), "살입니다.")  # 자기 소개 메서드

class Employee(Person):
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)
        self.salary = salary  # 급여
        self.hire_date = hire_date  # 입사일

    def do_work(self):
        print('열심히 일을 합니다.')  # 일을 하는 메서드

    def about_me(self):
        super().about_me()
        print('제 급여는', self.salary, '원이고, 제 입사일은', self.hire_date, '입니다.')  # 자기 소개 메서드

chulsu = Employee('철수', 26, '남성', '3500', '20231021')
chulsu.about_me()

class Product:
    pass  # 빈 클래스

class Inventory:
    def __init__(self):
        self.__items = []  # 아이템 목록을 저장하는 private 변수

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)  # 새로운 아이템 추가 메서드
            print('새로운 아이템이 추가되었습니다.')
        else:
            raise ValueError('유효하지 않은 아이템입니다.')

    def get_number_of_items(self):
        return len(self.__items)  # 아이템 수 반환 메서드

    @property
    def items(self):
        return self.__items  # 아이템 목록을 가져오는 property

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
items = my_inventory.items
items.append(Product())
print(items)  # 아이템 목록 출력
