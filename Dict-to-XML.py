from xml.etree import ElementTree


def convert_to_xml(tag, dct):
    tree = ElementTree.ElementTree()
    elem = ElementTree.Element(tag)

    for k, v in dct.items():
        child = ElementTree.Element(k)
        for subkey, subval in v.items():
            grandchild = ElementTree.Element(subkey)
            grandchild.text = str(subval)
            child.append(grandchild)
        elem.append(child)
        tree._setroot(elem)
    return tree


convert_to_xml("data", data_dct).write("data.xml")
