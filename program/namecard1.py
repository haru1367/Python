#명함관리 프로그램
#기능(입력,수정,삭제,목록,검색,종료,저장)
#데이터구조(이름,주소,전화번호,이메일) - 딕셔너리로 저장
import json
import os

card = {}
count = len(card)

def card_append(card):
    print('명함에 정보를 추가합니다.')
    name = input('이름:')
    check = False
    for i in range(0,len(card)):
        if card[i]['name'].lower() == name.lower():
            print('이미 명함이 존재합니다!')
            check = True
            break
    if check == False:
        address = input('주소:')
        phone = input('전화번호:')
        email = input('이메일:')
        global count
        count+=1
        card.append({'count':count,'name':name,'address':address,'phone':phone,'email':email})
    return card

def print_card(card):
    for i in card:
        print(i)

def modify_card(card):
    data = int(input('수정할 데이터의 번호를 입력하세요 : '))
    global count
    if data > count:
        print('숫자 입력이 잘못되었습니다.')
    else:
        num = int(input('''
    1.이름 수정
    2.주소 수정
    3.전화번호 수정
    4.이메일 수정
                    
    >>> 수정할 내용을 골라주세요 : '''))
        modify = input('바꿀 내용 : ')
        if num == 1:
            card[data-1]['name'] = modify
        elif num ==2 :
            card[data-1]['address'] = modify
        elif num==3 :
            card[data-1]['phone'] = modify
        elif num==4 :
            card[data-1]['email'] = modify
        print('수정이 완료되었습니다!')

def delete_card(card):
    data = int(input('삭제할 데이터의 번호를 입력하세요 : '))
    del(card[data-1])
    global count
    count -=1
    for index in range(1,len(card)+1):
        card[index-1]['count'] = index
    print('삭제가 완료되었습니다')
    return card

def search_name(card):
    data = input('검색할 이름을 입력해주세요 : ')
    check = False
    for i in range(0,len(card)):
        if card[i]['name'].lower() == data.lower():
            print(card[i])
            check = True
            break
    if check == False:
        print('해당 정보를 찾을 수 없습니다.')

if os.path.isfile("C:/Users/haru1367/Desktop/coding깃허브/Python/program/namecard1.txt") == True:
    f=open("C:/Users/haru1367/Desktop/coding깃허브/Python/program/namecard1.txt",'r')
    card = json.load(f)
    count = len(card)
    f.close()
else:f=open("C:/Users/haru1367/Desktop/coding깃허브/Python/program/namecard1.txt",'w')

while True:
    menu = input('''
-----------------------------------------------------
 1.입력  2.수정  3.삭제  4.목록  5.검색  6.저장  7.종료
-----------------------------------------------------
>>>메뉴를 골라주세요: ''')
    
    if menu == '1':
        card_append(card)
        f.close()
    elif menu == '2':
        modify_card(card)
        f.close()
    elif menu == '3':
        delete_card(card)
        f.close()
    elif menu == '4':
        print_card(card)
        f.close()
    elif menu == '5':
        search_name(card)
        f.close()
    elif menu == '6':
        f.close()
        f = open("C:/Users/haru1367/Desktop/coding깃허브/Python/program/namecard1.txt",'w')
        json.dump(card,f)
        f.close()
        print('저장이 완료되었습니다!')
    elif menu == '7':
        print('프로그램을 종료합니다')
        f.close()
        break
    else:
        print('입력이 잘못되었습니다.')