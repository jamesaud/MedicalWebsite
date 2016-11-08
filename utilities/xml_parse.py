import xml.etree.ElementTree as ET


def parseTable(xml_file):
    tree = ET.parse(xml_file)


parseTable('comparison.xml')

