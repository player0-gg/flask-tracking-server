import xml.etree.ElementTree as ET
from lib import Errors


def parse(xml_file_path):
    # parse xml file
    # TODO: catch ParseError
    # TODO: is not secure => use other lib
    # https://docs.python.org/3/library/xml.etree.elementtree.html
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    return _parse_xml_root(root)


def parse_from_xml_string(xml_string):
    root = ET.fromstring(xml_string)
    return _parse_xml_root(root)


def _parse_xml_root(root):
    if root is None or root.tag != "TrackMate":
        raise Errors.XML_ROOT_INVALID

    return root.tag
