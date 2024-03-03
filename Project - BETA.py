from tkinter import *
from datetime import datetime
from googletrans import Translator
import time
translator = Translator()
temp = 0
timer_delenie = ''
List_lng_1 = ['Русский', 'Английский', 'Французский', 'Немецкий']
Lang_Dict = {'Русский':'ru', 'Английский':'en','Французский':'fr','Немецкий':'de'}
def Translate():
	tr_lng_index = Lang_List2.curselection()
	tr_lng = Lang_Dict[Lang_List2.get(tr_lng_index)]
	result = translator.translate(Original_Text.get(0.0, END), dest = tr_lng)
	if len(list(Translate_Text.get(0.0, END))) > 0:
		Translate_Text.delete(0.0, END)
		Translate_Text.insert(END, result.text)
	else:
		Translate_Text.insert(END, result.text)
def remember_all():
	l_start.place(x = 130, y = 100)
	start_b_2.place(x = 250, y = 150)
	Radiobutton_1.place(x = 250, y = 210)
	Radiobutton_2.place(x = 250, y = 260)
	Radiobutton_3.place(x = 250, y = 310)
	vib_programs.place(x = 270, y = 370)
def forget_all():
	l_start.place_forget()
	start_b_2.place_forget()
	Radiobutton_1.place_forget()
	Radiobutton_2.place_forget()
	Radiobutton_3.place_forget()
	vib_programs.place_forget()
def timer_exit():
	label1.place_forget()
	btn1.place_forget()
	btn2.place_forget()
	btn3.place_forget()
	btn4.place_forget()
	btn5.place_forget()
	remember_all()
def one_sec():
    global temp, timer_delenie
    timer_delenie = root.after(1000, one_sec)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    label1.configure(text=str(f_temp))
    temp += 1
def start_timer():
    btn1.place_forget()
    btn2.place(x = 170, y = 300)
    one_sec()
def stop_timer():
    btn2.place_forget()
    btn4.place(x = 170, y = 470)
    root.after_cancel(timer_delenie)
def continue_timer():
    btn3.place_forget()
    btn4.place_forget()
    btn2.place(x = 170, y = 300)
    one_sec()
def reset_timer():
    global temp
    temp = 0
    label1.configure(text="00:00")
    btn3.place_forget()
    btn4.place_forget()
    btn1.place(x = 170, y = 300)
def calc_exit():
	calc_button_1.place_forget()
	calc_button_2.place_forget()
	calc_button_3.place_forget()
	calc_button_4.place_forget()
	calc_button_5.place_forget()
	calc_button_6.place_forget()
	calc_button_7.place_forget()
	calc_button_8.place_forget()
	calc_button_9.place_forget()
	calc_button_10.place_forget()
	calc_button_plus.place_forget()
	calc_button_minus.place_forget()
	calc_entry.place_forget()
	calc_button_multiply.place_forget()
	calc_button_split.place_forget()
	calc_button_grade.place_forget()
	calc_button_equal.place_forget()
	calc_button_exit.place_forget()
	calc_button_dot.place_forget()
	calc_button_delete.place_forget()
	remember_all()
def equal_calc():
	a = calc_entry.get()
	b = eval(a)
	calc_entry.delete(0, END)
	calc_entry.insert(END, str(b))

def programs():
	if like.get() == 1:
		forget_all()
		global label1
		label1 = Label(root, width=5, font=("Candara", 70), text="00:00")
		label1.place(x = 170, y = 160)
		global btn1
		btn1 = Button(root,width = 17, height = 1, text="Начать", font=("Candara", 20),bd = 6, bg = 'gray',activeforeground = 'white', activebackground = '#4d4d4d', command=start_timer)
		global btn2
		btn2 = Button(root,width = 17, height = 1, text="Стоп", font=("Candara", 20),bd = 6, bg = 'gray',activeforeground = 'white', activebackground = '#4d4d4d', command=stop_timer)
		global btn3
		btn3 = Button(root,width = 17, height = 1, text="Продолжить", font=("Candara", 20),bd = 6, bg = 'gray',activeforeground = 'white', activebackground = '#4d4d4d', command=continue_timer)
		global btn4
		btn4 = Button(root,width = 17, height = 1, text="Сброс", font=("Candara", 20),bd = 6, bg = 'gray',activeforeground = 'white', activebackground = '#4d4d4d', command=reset_timer)
		btn1.place(x = 170, y = 300)
		global btn5
		btn5 = Button(root,width = 17, height = 1, text='Выход', font = ('Candara', 20),bd = 6, bg = 'gray', activeforeground = 'white', activebackground = '#4d4d4d', command = timer_exit)
		btn5.place(x = 170, y = 380)
	elif like.get() == 2:
		forget_all()
		global calc_button_1
		calc_button_1 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '7', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '7': calc_entry.insert(END, text)) 
		calc_button_1.place(x = 70, y = 100)
		global calc_button_2
		calc_button_2 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '4', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '4': calc_entry.insert(END, text))
		calc_button_2.place(x = 70, y = 215)
		global calc_button_3
		calc_button_3 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '1', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '1': calc_entry.insert(END, text))
		calc_button_3.place(x = 70, y = 330)
		global calc_button_4
		calc_button_4 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '8', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '8': calc_entry.insert(END, text))
		calc_button_4.place(x = 185, y = 100)
		global calc_button_5
		calc_button_5 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '5', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '5': calc_entry.insert(END, text))
		calc_button_5.place(x = 185, y = 215)
		global calc_button_6
		calc_button_6 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '2', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '2': calc_entry.insert(END, text))
		calc_button_6.place(x = 185, y = 330)
		global calc_button_7
		calc_button_7 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '9', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '9': calc_entry.insert(END, text))
		calc_button_7.place(x = 300, y = 100)
		global calc_button_8
		calc_button_8 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '6', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '6': calc_entry.insert(END, text))
		calc_button_8.place(x = 300, y = 215)
		global calc_button_9
		calc_button_9 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '3', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '3': calc_entry.insert(END, text))
		calc_button_9.place(x = 300, y = 330)
		global calc_button_10
		calc_button_10 = Button(width = 6, height = 2, bg = '#808080', bd = 3, text = '0', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '0': calc_entry.insert(END, text))
		calc_button_10.place(x = 185, y = 445)
		global calc_button_plus
		calc_button_plus = Button(width = 4, height = 1, bg = '#808080', bd = 3, text = '+', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '+': calc_entry.insert(END, text))
		calc_button_plus.place(x = 415, y = 100)
		global calc_button_minus
		calc_button_minus = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '-', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '-': calc_entry.insert(END, text))
		calc_button_minus.place(x = 500, y = 100)
		global calc_button_multiply
		calc_button_multiply = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '*', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '*': calc_entry.insert(END, text))
		calc_button_multiply.place(x = 415, y = 185)
		global calc_button_split
		calc_button_split = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '/', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '/': calc_entry.insert(END, text))
		calc_button_split.place(x = 500, y = 185)
		global calc_button_grade
		calc_button_grade = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '**', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '**': calc_entry.insert(END, text))
		calc_button_grade.place(x = 415, y = 270)
		global calc_button_dot
		calc_button_dot = Button(width = 4, height = 1, bg = '#808080', bd = 3, text = '.', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda text = '.': calc_entry.insert(END, text))
		calc_button_dot.place(x = 500, y = 270)
		global calc_button_equal
		calc_button_equal = Button(width = 4, height = 1, bg= '#808080', bd = 3, text = '=', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = equal_calc)
		calc_button_equal.place(x = 415, y = 355)
		global calc_button_delete
		calc_button_delete = Button(width = 4, height = 1, bg = '#808080', bd = 3, text = 'C', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = lambda: calc_entry.delete(0, END))
		calc_button_delete.place(x = 500, y = 355)
		global calc_entry
		calc_entry = Entry(width = 21, bd = 4, text = ' ', font = ('Candara', 20))
		calc_entry.place(x = 70, y = 50)
		global calc_button_exit
		calc_button_exit = Button(width = 6, height = 1, bg = '#808080', bd = 3, text = 'Выход', font = ('Candara', 20), activeforeground = 'white', activebackground = '#4d4d4d', command = calc_exit)
		calc_button_exit.place(x = 400, y = 450)
	elif like.get() == 3:
		forget_all()
		global Original_Text
		Original_Text = Text(width = 50, height = 10, bd = 6)
		Original_Text.place(x = 100, y = 50)
		global Translate_Text
		Translate_Text = Text(width = 50, height = 10, bd = 6)
		Translate_Text.place(x = 100, y = 350)
		global Lang_List2
		Lang_List2 = Listbox(root, selectmode = SINGLE, height = 4, font = 10, exportselection=0)
		Lang_List2.place(x = 150, y = 250)
		for i in List_lng_1:
			Lang_List2.insert(END, i)
		global Translate_Button
		Translate_Button = Button(width = 10, height = 1, bg= '#808080', bd = 3, text = 'Перевести', font = ('Candara', 15), activeforeground = 'white', activebackground = '#4d4d4d', command = Translate)
		Translate_Button.place(x = 350, y = 250)
def start_b_1_games():
	l_start['text'] = 'games'
def start_b_2_programs(): #Функция, отвечающая за нажатие кнопки 'Программы'
	global like
	like = IntVar()
	like.set(None)
	global Radiobutton_1
	Radiobutton_1 = Radiobutton(root, text = 'Таймер', font = ('Candara', 15), variable = like, value = 1)
	Radiobutton_1.place(x = 250, y = 210)
	global Radiobutton_2
	Radiobutton_2 = Radiobutton(root, text = 'Калькулятор', font = ('Candara', 15), variable = like, value = 2)
	Radiobutton_2.place(x = 250, y = 260)
	global Radiobutton_3
	Radiobutton_3 = Radiobutton(root, text = 'Переводчик', font = ('Candara', 15), variable = like, value = 3)
	Radiobutton_3.place(x = 250, y = 310)
	global vib_programs
	vib_programs = Button(width = 10, height = 1, bg = '#808080', text = 'Выбрать', font = ('Candara', 12), activeforeground = 'white', activebackground = '#4d4d4d', command = programs)
	vib_programs.place(x = 270, y = 370)



root = Tk()
root.title('BETA')
root.geometry('600x600')

l_start = Label(text = 'Здравствуйте! Чем хотите заняться?', font = ('Candara', 15))
l_start.place(x = 130, y = 100)
start_b_2 = Button(width = 10, height = 1, text = 'Программы', font = ('Candara', 15), bg = '#808080', activeforeground = 'white', activebackground = '#4d4d4d', command = start_b_2_programs) # Кнопка для вывода программ
start_b_2.place(x = 250, y = 150)



root.mainloop()