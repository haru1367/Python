# 줄 카운터 및 데이터 저장을 위한 빈 리스트 초기화
line_counter = 0
data_header = []
customer_list = []

# "study/customers.csv" 파일을 열고 읽어들입니다
with open("study/customers.csv") as customer_data:
    while 1:
        data = customer_data.readline()
        if not data:
            break

        # 첫 번째 라인인 경우, 헤더로 분할하여 저장
        if line_counter == 0:
            data_header = data.split(',')
        else:
            # 그렇지 않으면 데이터를 분할하고 customer_list에 추가
            customer_list.append(data.split(','))
        line_counter += 1

# 헤더 및 처음 10개 데이터 항목 출력
print('헤더:', data_header)
for i in range(0, 10):
    print('데이터', i, ':', customer_list[i])

# 고객 항목의 총 수 출력
print(len(customer_list))

# 변수 초기화 및 "study/customers.csv" 파일 다시 열기
line_counter = 0
data_header = []
employee = []
customer_USA_only_list = []
customer = None

with open("study/customers.csv", 'r') as customer_data:
    while 1:
        data = customer_data.readline()
        if not data:
            break

        # 첫 번째 라인인 경우, 헤더로 분할하여 저장
        if line_counter == 0:
            data_header = data.split(',')
        else:
            customer = data.split(',')

            # 고객이 미국에서 온 경우 목록에 추가
            if customer[10].upper() == "USA":
                customer_USA_only_list.append(customer)
        line_counter += 1

# 헤더 및 미국에서 온 고객의 처음 10개 항목 출력
print('헤더:', data_header)
for i in range(0, 10):
    print('데이터:', customer_USA_only_list[i])

# "study/customers_USA_only.csv" 파일을 만들고 미국에서 온 고객 데이터를 쓰기
with open('study/customers_USA_only.csv', 'w') as customer_USA_only_csv:
    for customer in customer_USA_only_list:
        customer_USA_only_csv.write(",".join(customer).strip('\n') + '\n')

# 필요한 라이브러리 가져오기
import csv

# 리스트와 변수 초기화
seoung_nam_data = []
header = []
rownum = 0

# "korea_floating_population_data.csv" 파일을 'cp949' 인코딩으로 열기
with open("study/korea_floating_population_data.csv", 'r', encoding='cp949') as p_file:
    csv_data = csv.reader(p_file)
    for row in csv_data:
        if rownum == 0:
            header = row
        location = row[7]

        # 위치에 '성남시'가 포함되어 있는지 확인하고 seoung_nam_data에 행 추가
        if location.find(u'성남시') != -1:
            seoung_nam_data.append(row)
        rownum += 1

# "study/seoung_nam_floating_population_data.csv" 파일을 만들고 필터된 데이터를 쓰기
with open("study/seoung_nam_floating_population_data.csv", "w", encoding='utf8') as s_p_file:
    writer = csv.writer(s_p_file, delimiter='\t', quotechar="'", quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    for row in seoung_nam_data:
        writer.writerow(row)

# 로깅 라이브러리 가져오기
import logging

# 다른 로그 레벨과 메시지를 사용하여 루트 로거 구성
logging.debug('개발 시점에 프로그램이 문제없이 실행되는지 확인하기 위해 출력하는 결과')
logging.info('사용자에게 실행 결과를 알려주는 로그 정보')
logging.warning('문제가 될 수 있는 상황을 기록하는 것')
logging.error('잘못된 처리로 에러가 발생, 프로그램은 동작 가능')
logging.critical('잘못된 처리로 데이터가 손실되었거나 프로그램이 더이상 동작 불가능')

# 사용자 지정 로거 'main' 생성 및 구성
logger = logging.getLogger('main')
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# 사용자 정의 로그 메시지와 함께 다른 로그 레벨로 메시지 기록
logger.debug('틀렸어!')
logger.info('확인해')
logger.warning('조심해')
logger.error('에러났어')
logger.critical('망했다')

# 설정 파일 읽기 위한 configparser 라이브러리 가져오기
import configparser

# ConfigParser 인스턴스 생성
config = configparser.ConfigParser()

# "study/example.cfg" 파일 읽기
config.read("study/example.cfg")

# 구성 파일의 섹션 가져오기
config.sections()

# 'SectionOne' 섹션에서 값을 액세스하고 출력
for key in config['SectionOne']:
    print(key)
config['SectionOne']['status']

# 사용자 지정 로거 'myapp' 생성 및 로그 메시지를 파일에 기록하도록 구성
logger = logging.getLogger('myapp')
file_handler = logging.FileHandler('myapp.log')

# 사용자 정의 로그 메시지 형식 정의
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일 핸들러에 포매터 설정
file_handler.setFormatter(formatter)

# 파일 핸들러를 'myapp' 로거에 추가하고 로그 레벨을 INFO로 설정
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# 다른 로그 레벨로 로그 메시지 기록
logger.error('오류 발생')
logger.info('여기에 있습니다')
logger.info('테스트 완료')
