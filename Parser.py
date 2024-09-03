from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageDraw
import os


class Parser:
    def __init__(self, xml):
        self.inpath = f'Programming-Assignment-Data/{xml}'
        self.outpath = f'output/updated-{xml}.png'
        self.tree = self.setsoup(self.inpath)
        self.tf = False
    
    def setsoup(self, xml):
        with open(xml, 'r') as file:
            tree = BeautifulSoup(file, 'xml')
            return tree
    
    def getboundsformatted(self, leaves):
        boundlist = []
        for i in leaves:
           if (len(i) == 0):
               bounds = i.get('bounds') #[,][,]
               tmp = bounds.split('][')
               firstlist = tmp[0].split(',')
               secondlist = tmp[1].split(',')

               x1 = firstlist[0][1:]
               y1 = firstlist[1]
               x2 = secondlist[0]
               y2 = secondlist[1][:-1]

               appendlist = []
               appendlist.append(int(x1))
               appendlist.append(int(y1))
               appendlist.append(int(x2))
               appendlist.append(int(y2))

               boundlist.append(appendlist)

        return boundlist
               
    
    def drawbounds(self, coords):
        if self.tf == False:
            tmppng= Image.open(self.xmltopng(self.inpath))
            self.tf = True
        else:
            tmppng = Image.open(self.outpath)
        draw = ImageDraw.Draw(tmppng)
        draw.rectangle(coords, fill=None, outline='yellow', width=4)
        tmppng.save(self.outpath)
    
    def xmltopng(self, xml):
        return f'{xml[:-3]}png'

if __name__ == "__main__":
    
    for x in os.listdir("Programming-Assignment-Data"):
        
        if x.endswith(".xml"):

            p = Parser(x)
            leaves = p.tree.find_all("node")
            coordinates = p.getboundsformatted(leaves)

            for i in coordinates:
                p.drawbounds(i)
            
            
