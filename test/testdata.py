from lib import Parser

# call in main method in testdata
# TEST_DATA_PARSED_XML = Parser.parse(test_data.xml')

# run app.py
TEST_DATA_PARSED_XML = Parser.parse('./test/test_data.xml')

TEST_DATA_OVERVIEW = [
    {'id': 1, 'title': 'Data 1', 'comment': 'comment 1', 'content': ''},
    {'id': 2, 'title': 'Data 2', 'comment': 'comment 2', 'content': ''},
    {'id': 3, 'title': 'Data 3', 'comment': 'comment 3', 'content': ''}
]


if __name__ == '__main__':

    print('data = {}'.format(TEST_DATA_PARSED_XML))
