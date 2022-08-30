import xml.etree.ElementTree as etree

tree = etree.ElementTree(etree.fromstring(xml_string))
root = tree.getroot()
root.getchildren()
node.attrib
