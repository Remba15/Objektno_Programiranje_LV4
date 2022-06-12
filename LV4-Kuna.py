import string
from tkinter import Frame, Menu, Canvas, filedialog as fd, Tk


class Application(Frame):

    def selectReadFile(self):
        self.openWindow = fd.askopenfilename()
        openFile = open(self.openWindow, 'r')
        for line in openFile:
            line = line.rstrip()
            drawCommands = line.split(' ')
            if drawCommands[0] == "Line":
                line = Line(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], xcoordinate2 = drawCommands[4],  ycoordinate2 = drawCommands[5])
                line.draw(self.c)
            if drawCommands[0] == "Triangle":
                triangle = Triangle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], xcoordinate2 = drawCommands[4],  ycoordinate2 = drawCommands[5], xcoordinate3 = drawCommands[6], ycoordinate3 = drawCommands[7])
                triangle.draw(self.c)
            if drawCommands[0] == "Rectangle":
                rectangle = Rectangle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], height = drawCommands[4],  width = drawCommands[5])
                rectangle.draw(self.c)
            if drawCommands[0] == "Circle":
                circle = Circle(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], radius = drawCommands[4])
                circle.draw(self.c)
            if drawCommands[0] == "Ellipse":
                ellipse = Ellipse(color = drawCommands[1], xcoordinate1 = drawCommands[2], ycoordinate1 = drawCommands[3], radius1 = drawCommands[4],  radius2 = drawCommands[5])
                ellipse.draw(self.c)
            if drawCommands[0] == "Polygon":
                polygonColor = drawCommands[1]
                polygonX1 = drawCommands[2]
                polygonY1 = drawCommands[3]
                del drawCommands[0:2]
                polygon = Polygon(polygonColor, polygonX1, polygonY1, drawCommands)
                polygon.draw(self.c)

    def initWidgets(self):
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label = "Open", command=self.selectReadFile)
        filemenu.add_command(label="Exit", command=exit)
        self.master.config(menu=menubar)
        self.master.title("LV4 Objektno Programiranje - Renato Kuna")
        self.c = Canvas(self, bg="#999999", height=600, width=800)
        self.c.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initWidgets()


class GrafickiLik():  #Klasa GrafLik pored svojeg inicijalizatora mora još imati funkcije: SetColor, GetColor i Draw. Također mora imati i dva atributa odnosno varijable: boja (pogledati prethodni opis kako se koriste boje u Tkinter-u) i tocka
    Color: string
        
    def __init__(self, color, xcoordinate1, ycoordinate1):
        self.Color = color
        self.xcoordinate1 = xcoordinate1
        self.ycoordinate1 = ycoordinate1

    def draw(self, canvas):
        pass

class Line(GrafickiLik):

    def __init__(self, color, xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.xcoordinate2 = xcoordinate2
        self.ycoordinate2 = ycoordinate2

    def draw(self, canvas):
        canvas.create_line((self.xcoordinate1, self.ycoordinate1, self.xcoordinate2, self.ycoordinate2), fill = self.Color)

class Triangle(Line):

    def __init__(self, color, xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2, xcoordinate3, ycoordinate3):
        super().__init__(color, xcoordinate1, ycoordinate1, xcoordinate2, ycoordinate2)
        self.xcoordinate3 = xcoordinate3
        self.ycoordinate3 = ycoordinate3

    def draw(self,canvas):
        canvas.create_line((self.xcoordinate1, self.ycoordinate1, self.xcoordinate2, self.ycoordinate2), fill=self.Color)
        canvas.create_line((self.xcoordinate2, self.ycoordinate2, self.xcoordinate3, self.ycoordinate3), fill=self.Color)
        canvas.create_line((self.xcoordinate3, self.ycoordinate3, self.xcoordinate1, self.ycoordinate1), fill=self.Color)

class Rectangle(GrafickiLik):

    def __init__(self, color, xcoordinate1, ycoordinate1, height, width):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.height = height
        self.width = width

    def draw(self,canvas):
        canvas.create_rectangle((self.xcoordinate1, self.ycoordinate1, float(self.xcoordinate1) + float(self.width), float(self.ycoordinate1) + float(self.height)), 
        outline = self.Color, fill = '')


class Circle(GrafickiLik):

    def __init__(self, color, xcoordinate1, ycoordinate1, radius):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.radius = radius

    def draw(self,canvas):
        canvas.create_oval((float(self.xcoordinate1) - float(self.radius), float(self.ycoordinate1) - float(self.radius), float(self.xcoordinate1) + 
        float(self.radius), float(self.ycoordinate1) + float(self.radius)), outline=self.Color, fill='')

class Ellipse(Circle):
    def __init__(self, color, xcoordinate1, ycoordinate1, radius1, radius2):
        super().__init__(color, xcoordinate1, ycoordinate1, radius1)
        self.radius2 = radius2

    def draw(self,canvas):
        canvas.create_oval((self.xcoordinate1, self.ycoordinate1, float(self.xcoordinate1) + float(self.radius), 
        float(self.ycoordinate1) + float(self.radius2)), outline=self.Color, fill="")

class Polygon(GrafickiLik):
    def __init__(self, color, xcoordinate1, ycoordinate1, coordinates = []):
        super().__init__(color, xcoordinate1, ycoordinate1)
        self.coordinates = coordinates
        self.coordinates.insert(0, xcoordinate1)
        self.coordinates.insert(1, ycoordinate1)

    def getCoordinates(self):
        return self.coordinates

    def setCoordinates(self, coordinates):
        self.coordinates = coordinates

    def draw(self, canvas):
        canvas.create_polygon(self.coordinates, outline = self.Color, fill = '')
    


if __name__ == "__main__":
    root = Tk()
    app = Application(root)
    app.mainloop()