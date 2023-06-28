from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from datetime import datetime
from kivy.uix.image import Image
import time
import os

class MainScreen(Screen):
    #Вывод статистики приложения на экран
    def show_info(self):
        count = 0
        for file in os.listdir(path):
            if file.endswith(".png"):
                count += 1
        self.ids.info.text = "Количество сделанных фотографий: {}".format(count)


class CameraScreen(Screen):
    def screen_shot(self, path):
        #Получение времени
        timenow = time.strftime("%Y_%m_%d_%H_%M_%S")
        #Сохранение изображения
        camera = self.ids.camera
        camera.export_to_png(path + "Image - " + timenow + ".png")


class ScreensManager(ScreenManager):
    def build(self):
        #Указание текущего экрана
        self.current = "Main screen"


class MainApp(App):
    def build(self):
        Window.size = (360, 650) #Изменение размера окна
        return ScreensManager.build(self)


if __name__ == "__main__":
    MainApp().run()