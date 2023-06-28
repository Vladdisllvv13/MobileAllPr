from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.core.window import Window
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MyPaintWidget(Widget):
    color: tuple = (0, 0, 0, 1)
    razm: int = 1
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(*self.color)
            touch.ud['line'] = Line(points=(touch.x, touch.y), width = self.razm)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def red_color(self, ):
        self.color = (255, 0, 0)
    
    def yellow_color(self, ):
        self.color = (255,124,0)

    def blue_color(self, ):
        self.color = (0, 0 , 255)
    
    def black_color(self, ):
        self.color = (0, 0, 0, 1)

    def sum(self, ):
        if (self.razm <30 and self.razm !=29):
            self.razm +=2
        else:
            self.razm = 30

    def minus(self, ):
        if (self.razm > 1):
            self.razm -=2
        else:
            self.razm = 1


class MyPaintApp(App):

    def build(self):
        Window.size = (400, 600)
        Window.clearcolor = (1, 1, 1, 1)
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        redbtn = Button(text = '', pos = (103, 1), size = (48, 48),  
                        background_color ="#ff0000", background_normal = '', 
                        on_press = self.get_red_color)
        yellowbtn = Button(text = '', pos = (103, 52), size = (48, 48),  
                        background_color ="#efeb00", background_normal = '', 
                        on_press = self.get_yellow_color)
        blackbtn = Button(text = '', pos = (154, 1), size = (48, 48),  
                        background_color ="#000000", background_normal = '', 
                        on_press = self.get_black_color)
        bluebtn = Button(text = '', pos = (154, 52), size = (48, 48),  
                        background_color ="#0000ff", background_normal = '', 
                        on_press = self.get_blue_color)
        #slide = Slider(min=1, max = 30, value = 1, pos = (205, 30) )
        btnminus = Button(text = '-', pos = (261, 1), size = (48, 48),  
                        background_color ="#404040", background_normal = '', 
                        on_press = self.btnminus_click, color = (0,1,0,1))
        btnpls = Button(text = '+', pos = (312, 1), size = (48, 48),  
                        background_color ="#404040", background_normal = '', 
                        on_press = self.btnpls_click, color = (0,1,0,1))
        self.label = Label(text = "1", pos = (261, 52), size = (100, 48), color = (0,1,0,1))
        with self.label.canvas:
            Color(170, 169, 170, 0.25)
            Rectangle(pos = self.label.pos, size = self.label.size)

        parent.add_widget(redbtn)
        parent.add_widget(yellowbtn)
        parent.add_widget(blackbtn)
        parent.add_widget(bluebtn)
        parent.add_widget(btnpls)
        parent.add_widget(btnminus)
        parent.add_widget(self.label)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

    def get_red_color(self, instance):
        self.painter.red_color()

    def get_yellow_color(self, instance):
        self.painter.yellow_color()

    def get_black_color(self, instance):
        self.painter.black_color()

    def get_blue_color(self, instance):
        self.painter.blue_color()
    
    def btnpls_click(self, instanse):
        self.painter.sum()
        a = int(self.label.text)
        if (a<30 and a !=29):
            a +=2
        else:
            a = 30
        self.label.text = str(a)

    def btnminus_click(self, instanse):
        self.painter.minus()
        a = int(self.label.text)
        if (a > 1):
            a -=2
        else:
            a = 1
        self.label.text = str(a)


        

if __name__ == '__main__':
    MyPaintApp().run()