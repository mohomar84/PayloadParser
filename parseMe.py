# Imports

import xml.etree.ElementTree as ET


tree = ET.parse('payload.xml')
root = tree.getroot()
iter = tree.iter()
# all items data
print('Expertise Data:')


for elem in iter:
   print('level 1')
   print(elem)
   for subelem in elem:
      print('level 2')
      subelem
      print(subelem.text)
      for subelem in subelem:
         print('level 3')
         print(subelem.text)



# check if the element has sub element using -- print(len(tree.findall(".")))
