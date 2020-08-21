import base64
import xml.etree.ElementTree as ET 
document = ET.parse(input())
document = document.getroot()
element = document.find(".//*[@nazwaPliku]")
name = base64.b64decode(element.attrib.get("nazwaPliku"))
content = base64.b64decode(list(element)[0].text)
with open(name, mode="wb+") as file:
    file.write(content)