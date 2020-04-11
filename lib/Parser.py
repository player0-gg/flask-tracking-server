import xml.etree.ElementTree as ET
from lib import Errors
from models.data import TrackingData, DataContainerType, SqlDataContainer


def parse(xml_file_path, container_type=DataContainerType.MYSQL):
    # parse xml file
    # TODO: catch ParseError
    # TODO: is not secure => use other lib
    # https://docs.python.org/3/library/xml.etree.elementtree.html
    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except ET.ParseError:
        raise Errors.XML_FILE_INVALID

    return _parse_xml_root(root, container_type)


def parse_from_xml_string(xml_string, container_type=DataContainerType.MYSQL):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        raise Errors.XML_FILE_INVALID

    return _parse_xml_root(root, container_type)


def _parse_xml_root(root, container_type=DataContainerType.MYSQL):
    tracking_data = TrackingData.from_xml_root(root)

    if container_type != DataContainerType.MYSQL:
        raise Errors.DATA_CONTAINER_TYPE_INVALID

    if container_type == DataContainerType.MYSQL:
        return SqlDataContainer(tracking_data)
    # elif ...
