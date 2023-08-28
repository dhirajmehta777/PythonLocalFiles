# import sys
# import xml.etree.ElementTree as etree
#
# def get_attr_number(node):
#     # your code goes here
#     val=0
#     for child in node.iter():
#         val+=len(child.attrib)
#     return val
#
# if __name__ == '__main__':
#     sys.stdin.readline()
#     xml = sys.stdin.read()
#     tree = etree.ElementTree(etree.fromstring(xml))
#     root = tree.getroot()
#     print(get_attr_number(root))

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    all_ele=node.findall(".//")
    count=0

    for child in all_ele:
        count+=len(child.attrib)
    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))