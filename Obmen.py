from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
import json

def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)

def update_target_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)


def exchange():
    target_code = target_combobox.get()
    base_code = base_combobox.get()
    if target_code and base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            data = response.json()

            if target_code in data['rates']:
                exchange_rate = data['rates'][target_code]
                base_name = currencies[base_code]
                target_name = currencies[target_code]
                mb.showinfo("Курс обмена",f"Курс обмена: {exchange_rate:.2f} {target_name} за 1 "
                                          f"{base_name}")
            else:
                mb.showerror("Ошибка", f"Валюта {target_code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка",f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание"," Введите код валюты")

currencies = {"EUR": "Евро",
              "JPY": "Японская йена",
              "GBP": "Британский фунт",
              "AUD": "Австралийский доллар",
              "CAD": "Канадский доллар",
              "CHF": "Швейцарский франк",
              "CNY": "Китайский юань",
              "RUB": "Российский рубль",
              "KZT": "Казахский тенге",
              "UZS": "Узбекский сум",
              "AED": "Эмиратский дирхам",
              "USD": "Американский доллар"}

window = Tk()
window.title("Курс обмена валюты")
window.geometry("360x300")

Label(text="Базовая валюта: ").pack(padx=10, pady=10)

base_combobox = ttk.Combobox(values=list(currencies.keys()))
base_combobox.pack(padx=10, pady=10)
base_combobox.bind("<<ComboboxSelected>>", update_base_label)

base_label = ttk.Label()
base_label.pack(padx=10, pady=10)

Label(text="Целевая валюта: ").pack(padx=10, pady=10)

target_combobox = ttk.Combobox(values=list(currencies.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind("<<ComboboxSelected>>", update_target_label)

target_label = ttk.Label()
target_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)
window.mainloop()




