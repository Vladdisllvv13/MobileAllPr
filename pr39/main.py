from typing import Union
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker, MDDatePicker, MDColorPicker

class MainApp(MDApp):
    def build(self):
        Window.size = (400, 600) #Изменение размера окна
        return Builder.load_file('time.kv')

#Вызов диалогового окна выбора времени
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_cancel=self.on_cancel_time, on_save=self.on_save_time)
        time_dialog.open()

    #Сохранение выбора, вывод времени на главном экране
    def on_save_time(self, instance, time):
        self.root.ids.time_label.text = str(time)
    #Выход из диалогового окна выбора времени
    def on_cancel_time(self, instance, time):
        self.root.ids.time_label.text = "Время не выбрано!"

#Вызов диалогового окна выбора даты
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save_date, on_cancel=self.on_cancel_date)
        date_dialog.open()

    # Сохранение выбора, вывод даты на главном экране
    def on_save_date(self, instance, value, date_range):
         self.root.ids.date_label.text = str(value)
    # Выход из диалогового окна выбора времени
    def on_cancel_date(self, instance, value):
        self.root.ids.date_label.text = "Дата не выбрана!"

if __name__ == '__main__':
    MainApp().run()