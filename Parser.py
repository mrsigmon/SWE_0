
import xml.etree.ElementTree as ET
import os
import aspose.pdf as ap

class Parser:
    def __init__(self, dest, xml):
        self.tree = ET.parse(dest)
        self.root = self.tree.getroot()
        self.xml = xml

    def parsexml(self, root):
        #handle parse error
        for child in root:
            if len(child.findall("node"))>0:
                self.parsexml(child)
            else:
                child.set('android:background', '@drawable/borderbox')
        dest = f'output/updated-{self.xml}'
        #pngdest = f'output/update-{self.xml[0:len(self.xml)-3]}.png'
        self.tree.write(dest)

        #pdf = ap.Document()
        #pdf.bind_xml(self.xml)
        #pdf.save(dest)
        #self.tree.write(pngdest)
    

if __name__ == "__main__":
    #pip install
    for x in os.listdir("Programming-Assignment-Data"):
        if x.endswith(".png"):
            continue
        elif x == "com.apalon.ringtones.xml":
            continue
        else:
            dest = f'Programming-Assignment-Data/{x}'
            p = Parser(dest, x)
            p.parsexml(p.root)