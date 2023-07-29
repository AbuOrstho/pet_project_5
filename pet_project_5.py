# Импорт необходимых библиотек
import tkinter as tk
from tkinter.ttk import Combobox

# Создание главного окна и словаря для хранения задач
window = tk.Tk()  # Создание окна
window.title('Список задач')  # Присваивание титульного названия
window.configure(bg='#202020')  # Цвет окна
window.geometry('213x300+700+80')  # Координаты
task = {}  # Словарь для хранения задач


# Функция для отрисовки новых виджетов добавления задач
def add_task():
    for widget in all_widget.winfo_children():
        widget.destroy()  # Удаление всех виджетов
    window.geometry('250x300+700+80')
    # Создаем новые виджеты для замены
    new_label = tk.Label(all_widget, text="Новая задача:", fg='white', bg='#202020', font=('Times New Roman', 12))
    new_label.grid(row=1, column=0, padx=4)

    new_entry = tk.Entry(all_widget, width=22)
    new_entry.grid(row=1, column=1, padx=4)

    new_pol = tk.Text(master=all_widget, width=30, height=10)
    new_pol.grid(row=2, column=0, padx=4, pady=6, columnspan=2)

    new_button = tk.Button(all_widget, width=8, height=2, bg='#76b9ed', fg='#213442', font=('Times New Roman', 13),
                           text='Сохранить', command=save_new_task)
    new_button.place(x=90, y=200)
    global new_entrys, new_pols
    new_entrys = new_entry
    new_pols = new_pol


# Функция для добавления новой задачи
def save_new_task():
    window.geometry('213x300+700+80')
    x = new_entrys.get()
    n = new_pols.get('1.0', tk.END)
    task[x] = n
    for widget in all_widget.winfo_children():
        widget.destroy()

    # Обновление текста в pol в зависимости от значения в combo
    def update_text(event):
        selected_key = combo.get()  # Получение значения из combo
        if selected_key in task:
            pol.delete("1.0", tk.END)
            pol.insert(tk.END, task[selected_key])

    # Функция для удаления задач
    def delete_task():
        del_key = combo.get()
        if del_key in task:
            del task[del_key]
            combo.set('')
            combo.delete(0, 'end')
            pol.delete("1.0", tk.END)
            combo['values'] = list(task.keys())
            combo.grid(row=1, column=0, padx=4)

    # Создание виджетов
    entry = tk.Label(all_widget, text="Мои задачи:", fg='white', bg='#202020', font=('Times New Roman', 12), width=23)
    entry.grid(row=0, column=0)

    combo = Combobox(master=all_widget, width=23, font=('Times New Roman', 12))
    combo['values'] = list(task.keys())
    combo.grid(row=1, column=0, padx=4)

    pol = tk.Text(master=all_widget, width=25, height=10)
    pol.grid(row=2, column=0, padx=4, pady=6)

    add_button = tk.Button(master=all_widget, width=8, height=2, bg='#76b9ed', fg='#213442',
                           font=('Times New Roman', 13),
                           text='Добавить',
                           command=add_task)
    add_button.place(x=5, y=225)

    del_button = tk.Button(master=all_widget, width=8, height=2, bg='#A5260A', fg='white', font=('Times New Roman', 13),
                           text='Удалить', command=delete_task)
    del_button.place(x=128, y=225)

    combo.bind("<<ComboboxSelected>>", update_text)

    all_widget.pack(expand=True, fill='both')


# Обновление текста в pol в зависимости от значения в combo
def update_text(event):
    selected_key = combo.get()
    if selected_key in task:
        pol.delete("1.0", tk.END)
        pol.insert(tk.END, task[selected_key])


# Создание виджетов
all_widget = tk.Frame(window, bg='#202020')

entry = tk.Label(all_widget, text="Мои задачи:", fg='white', bg='#202020', font=('Times New Roman', 12), width=23)
entry.grid(row=0, column=0)

combo = Combobox(master=all_widget, width=23, font=('Times New Roman', 12))
combo['values'] = list(task.keys())
combo.grid(row=1, column=0, padx=4)

pol = tk.Text(master=all_widget, width=25, height=10)
pol.grid(row=2, column=0, padx=4, pady=6)

add_button = tk.Button(master=all_widget, width=8, height=2, bg='#76b9ed', fg='#213442', font=('Times New Roman', 13),
                       text='Добавить',
                       command=add_task)
add_button.place(x=5, y=225)

del_button = tk.Button(master=all_widget, width=8, height=2, bg='#A5260A', fg='white', font=('Times New Roman', 13),
                       text='Удалить')
del_button.place(x=128, y=225)

combo.bind("<<ComboboxSelected>>", update_text)

all_widget.pack(expand=True, fill='both')
window.mainloop()
