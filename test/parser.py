from lib import Parser


def test_parse_xml():
    # parse from xml
    parsed_data = Parser.parse('test_data.xml')
    assert parsed_data is not None

    # validate parsed data
    assert len(parsed_data.data._all_tracks) == 290

    # TODO: add new test class for SQL database
    # convert to sql data (sql_data)
    # convert sql data to tracking data (tracking_data_from_sql)
    # compare tracking_data_from_sql vs. original tracking data
