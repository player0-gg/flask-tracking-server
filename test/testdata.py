from lib import Parser


TEST_XML_DATA = Parser.parse('test_data.xml')


if __name__ == '__main__':

    print('data = {}'.format(TEST_XML_DATA))
