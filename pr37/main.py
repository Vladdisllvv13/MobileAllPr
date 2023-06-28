from tkinter import *
from tkinter import messagebox as mb
import json
 
class Quiz:
    def __init__(self):
         
        self.q_no=0       
        self.display_title()
        self.display_question()   
        self.opt_selected=IntVar()        
        self.opts=self.radio_buttons()
        self.display_options()
        self.buttons()
        self.data_size=len(question)
        self.correct=0

    def display_result(self):
         
        # вычисляет неправильное количество
        wrong_count = self.data_size - self.correct
        correct = f"Правильные: {self.correct}"
        wrong = f"Неправильные: {wrong_count}"
         
        # вычисляет процент правильных ответов
        score = int(self.correct / self.data_size * 100)
        result = f"Прогресс: {score}%"
         
        # Показывает окно сообщения для отображения результата
        mb.showinfo("Результат", f"{result}\n{correct}\n{wrong}")
 
 
    # Этот метод проверяет ответ после того, как мы нажмем на Next
    def check_ans(self, q_no):
         
        # проверяет правильность выбранного параметра
        if self.opt_selected.get() == answer[q_no]:
            # если параметр правильный, он возвращает значение true
            return True
 
    def next_btn(self):
         
        # Проверка, правильный ли ответ
        if self.check_ans(self.q_no):
             
            # если ответ правильный, он увеличивает правильный на 1
            self.correct += 1
         
        # Переходит к следующему вопросу, увеличивая счетчик q_no counter
        self.q_no += 1
         
        # проверяет, равен ли размер q_no размеру данных
        if self.q_no==self.data_size:
             
            # если это правильно, то отображается оценка
            self.display_result()
             
            # выключает графический интерфейс
            gui.destroy()
        else:
            # показывает следующий вопрос
            self.display_question()
            self.display_options()
 
    def buttons(self):
         
        # Первая кнопка - это кнопка для перехода к
        # следующему вопросу
        next_button = Button(gui, text="Следующий",command=self.next_btn,
        width=10,bg="grey",fg="white",font=("ariel",16,"bold"))
         
        # размещение кнопки на экране
        next_button.place(x=350,y=380)
         
        # Это вторая кнопка, которая используется для выхода из графического интерфейса
        quit_button = Button(gui, text="Выход", command=gui.destroy,
        width=5,bg="red", fg="white",font=("ariel",16," bold"))
         
        # размещение кнопки выхода на экране
        quit_button.place(x=700,y=50)
 
 
    def display_options(self):
        val=0
         
        # отмена выбора параметров
        self.opt_selected.set(0)
         
        # перебираем параметры, которые будут отображаться для
        # текста переключателей.
        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
 
    # Этот метод показывает текущий вопрос на экране
    def display_question(self):
         
        # настройка свойств вопроса
        q_no = Label(gui, text=question[self.q_no], width=60,
        font=( 'ariel' ,14, 'bold' ), anchor= 'w' )
         
        #размещение опции на экране
        q_no.place(x=70, y=100)
 
 
    # Этот метод используется для отображения заголовка
    def display_title(self):
         
        # Заголовок, который будет показан
        title = Label(gui, text="Тест: Творчество Кендрика Ламара",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
         
        # место названия
        title.place(x=0, y=2)
 
    def radio_buttons(self):
         
        # инициализация списка пустым списком опций
        q_list = []
         
        # позиция первого варианта
        y_pos = 150
         
        # добавление опций в список
        while len(q_list) < 4:
             
            # настройка свойств переключателя
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
             
            # добавление кнопки в список
            q_list.append(radio_btn)
             
            # размещение кнопки
            radio_btn.place(x = 100, y = y_pos)
             
            # увеличение положения по оси y на 40
            y_pos += 40
         
        # возврат переключателей
        return q_list
 
# Создание окна графического интерфейса
gui = Tk()
 
# установка размера окна графического интерфейса
gui.geometry("800x450")
 
# установка заголовок окна
gui.title("Тест")
 
# получение данных из файла json
with open("практические\pr37\pr37-main\data.json",encoding="utf-8") as f:
    data = json.load(f)

 
# задание вопроса, варианты и ответ
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
 
# создание объект класса Quiz.
quiz = Quiz()
 
# Запуск графического интерфейса
gui.mainloop()