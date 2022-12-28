import xml.etree.ElementTree as ET

tree =ET.parse('hodlers.xml')
root =tree.getroot()

print (ET.tostring(root))