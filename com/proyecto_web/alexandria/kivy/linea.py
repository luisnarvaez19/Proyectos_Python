from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, InstructionGroup
from threading import Thread
from random import randint
import time



class MyWidget(Widget):

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        self.ig = InstructionGroup()
        self.line = Line(points=[100, 200, 300, 400])
        self.ig.add(self.line)
        self.canvas.add(self.ig)

        Thread(target=self.draw).start()


    def draw(self):
        while True:
            self.line.points = [randint(0,400) for i in range(4)]
            time.sleep(0.5)



class MainApp(App):

    def build(self):
        return MyWidget()



MainApp().run()