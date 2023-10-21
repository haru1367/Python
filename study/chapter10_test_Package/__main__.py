from analysis.series import series_test
from crawling.parser import parser_test
from database.connection import connection_test

if __name__ == '__main__':
    series_test()
    parser_test()
    connection_test()