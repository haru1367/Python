# line_counter = 0
# data_header=[]
# customer_list=[]
# with open("study/customers.csv") as customer_data:
#     while 1:
#         data = customer_data.readline()
#         if not data:break
#         if line_counter==0:
#             data_header = data.split(',')
#         else :
#             customer_list.append(data.split(','))
#         line_counter+=1
# print('Header:',data_header)
# for i in range(0,10):
#     print('Data',i,':',customer_list[i])
# print(len(customer_list))

# line_counter = 0
# data_header=[]
# employee = []
# customer_USA_only_list=[]
# customer = None
# with open("study/customers.csv",'r') as customer_data:
#     while 1:
#         data = customer_data.readline()
#         if not data:
#             break
#         if line_counter == 0:
#             data_header = data.split(',')
#         else:
#             customer = data.split(',')
#             if customer[10].upper()=="USA":
#                 customer_USA_only_list.append(customer)
#         line_counter+=1
# print('Header:',data_header)
# for i in range(0,10):
#     print('Data:',customer_USA_only_list[i])
# print(len(customer_USA_only_list))

# with open('study/customers_USA_only.csv','w')as customer_USA_only_csv:
#     for customer in customer_USA_only_list:
#         customer_USA_only_csv.write(",".join(customer).strip('\n')+'\n')

# import csv

# seoung_nam_data=[]
# header=[]
# rownum=0

# with open("study/korea_floating_population_data.csv",'r',encoding = 'cp949') as p_file:
#     csv_data = csv.reader(p_file)
#     for row in csv_data:
#         if rownum == 0:
#             header = row
#         location = row[7]
#         if location.find(u'성남시')!=-1:
#             seoung_nam_data.append(row)
#         rownum+=1

# with open("study/seoung_nam_floating_population_data.csv","w",encoding ='utf8') as s_p_file:
#     writer = csv.writer(s_p_file,delimiter='\t',quotechar="'",quoting=csv.QUOTE_ALL)
#     writer.writerow(header)
#     for row in seoung_nam_data:
#         writer.writerow(row)

import logging

# logging.debug('개발 시점에 프로그램이 문제없이 실행되는지 확인하기 위해 출력하는 결과')
# logging.info('사용자에게 실행 결과를 알려주는 로그 정보')
# logging.warning('문제가 될 수 있는 상황을 기록하는것')
# logging.error('잘못된 처리로 에러가 발생, 프로그램은 동작 가능')
# logging.critical('잘못된 처리로 데이터가 손실되었거나 프로그램이 더이상 동작 불가능')

# logger = logging.getLogger('main')
# stream_hander = logging.StreamHandler()
# logger.addHandler(stream_hander)
# logger.setLevel(logging.DEBUG)
# logger.debug('틀렸어!')
# logger.info('확인해')
# logger.warning('조심해')
# logger.error('에러났어')
# logger.critical('망했다')

# import configparser

# config = configparser.ConfigParser()
# config.sections()
# config.read("study/example.cfg")
# config.sections()
# for key in config['SectionOne']:
#     print(key)
# config['SectionOne']['status']

# logger = logging.getLogger('myapp')
# hdlr = logging.FileHandler('myapp.log')

# formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# hdlr.setFormatter(formatter)
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)

# logger.error('ERROR occured')
# logger.info('HERE WE ARE')
# logger.info('TEST finished')



