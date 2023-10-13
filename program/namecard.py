#명함관리 프로그램
#기능(입력,수정,삭제,목록,검색,종료,저장)
#데이터구조(이름,주소,전화번호,이메일) - 리스트로 저장
card = []
count = 0

def card_append(card):
    print('명함에 정보를 추가합니다.')
    name = input('이름:')
    address = input('주소:')
    phone = input('전화번호:')
    email = input('이메일:')
    global count
    count+=1
    card.append([count,name,address,phone,email])
    return card

def print_card(card):
    for i in card:
        print(i)

def modify_card(card):
    data = int(input('수정할 데이터의 번호를 입력하세요 : '))
    num = int(input('''
1.이름 수정
2.주소 수정
3.전화번호 수정
4.이메일 수정
                    
>>> 수정할 내용을 골라주세요 : '''))
    modify = input('바꿀 내용 : ')
    card[data-1][num] = modify
    print('수정이 완료되었습니다!')

def delete_card(card):
    data = int(input('삭제할 데이터의 번호를 입력하세요 : '))
    del(card[data-1])
    for index in range(1,len(card)+1):
        card[index-1][0] = index
    print('삭제가 완료되었습니다')
    return card

while True:
    menu = input('''
-----------------------------------------------------
 1.입력  2.수정  3.삭제  4.목록  5.검색  6.저장  7.종료
-----------------------------------------------------
>>>메뉴를 골라주세요: ''')
    if menu == '1':
        card_append(card)
    elif menu == '2':
        modify_card(card)
    elif menu == '3':
        delete_card(card)
    elif menu == '4':
        print_card(card)
    elif menu == '5':
        pass
    elif menu == '6':
        pass
    elif menu == '7':
        print('프로그램을 종료합니다')
        break
    else:
        print('입력이 잘못되었습니다.')
    
    
    