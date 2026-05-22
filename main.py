import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
str_expr = tk.StringVar(root, "")

#trig functions
def sin(): str_expr.set(str_expr.get()+"sin(")
def cos(): str_expr.set(str_expr.get()+"cos(")
def tan(): str_expr.set(str_expr.get()+"tan(")
def asin(): str_expr.set(str_expr.get()+"asin(")
def acos(): str_expr.set(str_expr.get()+"acos(")
def atan(): str_expr.set(str_expr.get()+"atan(")
def cosec(): str_expr.set(str_expr.get()+"csc(")
def sec(): str_expr.set(str_expr.get()+"sec(")
def cot(): str_expr.set(str_expr.get()+"cot(")
def acosec(): str_expr.set(str_expr.get()+"acsc(")
def asec(): str_expr.set(str_expr.get()+"asec(")
def acot(): str_expr.set(str_expr.get()+"acot(")

#log and exponent
def log(): str_expr.set(str_expr.get()+"log(")
def exp(): str_expr.set(str_expr.get()+"exp(")
def power(): str_expr.set(str_expr.get()+"**")

#numbers
def num0(): str_expr.set(str_expr.get()+"0")
def num1(): str_expr.set(str_expr.get()+"1")
def num2(): str_expr.set(str_expr.get()+"2")
def num3(): str_expr.set(str_expr.get()+"3")
def num4(): str_expr.set(str_expr.get()+"4")
def num5(): str_expr.set(str_expr.get()+"5")
def num6(): str_expr.set(str_expr.get()+"6")
def num7(): str_expr.set(str_expr.get()+"7")
def num8(): str_expr.set(str_expr.get()+"8")
def num9(): str_expr.set(str_expr.get()+"9")

#symbols
def b_open(): str_expr.set(str_expr.get()+"(")
def b_close(): str_expr.set(str_expr.get()+")")
def add(): str_expr.set(str_expr.get()+"+")
def sub(): str_expr.set(str_expr.get()+"-")
def mul(): str_expr.set(str_expr.get()+"*")
def div(): str_expr.set(str_expr.get()+"/")
def variable(): str_expr.set(str_expr.get()+"x")

#actions
def back():
    current = str_expr.get()
    str_expr.set("")
    str_expr.set(current[:-1])

def clear():
    str_expr.set("")

def plot():
    expr = str_expr.get()
    x = sp.Symbol('x')
    try:
        sym_expr = sp.parse_expr(expr)
        lamb_expr = sp.lambdify(x, sym_expr, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 100)
        y_vals = lamb_expr(x_vals)
        ax = plt.subplot()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        plt.grid()
        plt.plot(x_vals, y_vals)
        plt.show()
    except RuntimeWarning:
        pass
    except:    
        messagebox.showwarning(title="Error", message="Recheck the entered expression.")

root.title("Graph Plotter Application")
root.geometry("800x700")

label = tk.Label(root, text="Graph Plotter Application", font=("Arial", 20))
label.pack(padx=10, pady=10)

entry = tk.Entry(root, font=("Arial", 20), width=50, textvariable=str_expr)
entry.config(state="readonly")
entry.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn_back = tk.Button(buttonframe, text="Back", command=back)
btn_back.grid(row=0, column=0, sticky=tk.E+tk.W)

btn_clear = tk.Button(buttonframe, text="Clear", command=clear)
btn_clear.grid(row=0, column=1, sticky=tk.E+tk.W)

btn_plot = tk.Button(buttonframe, text="Plot", command=plot)
btn_plot.grid(row=0, column=2, sticky=tk.E+tk.W)

btn_sin = tk.Button(buttonframe, text="sin", command=sin)
btn_sin.grid(row=1, column=0, sticky=tk.E+tk.W)

btn_cos = tk.Button(buttonframe, text="cos", command=cos)
btn_cos.grid(row=1, column=1, sticky=tk.E+tk.W)

btn_tan = tk.Button(buttonframe, text="tan", command=tan)
btn_tan.grid(row=1, column=2, sticky=tk.E+tk.W)

btn_asin = tk.Button(buttonframe, text="sin-1", command=asin)
btn_asin.grid(row=2, column=0, sticky=tk.E+tk.W)

btn_acos = tk.Button(buttonframe, text="cos-1", command=acos)
btn_acos.grid(row=2, column=1, sticky=tk.E+tk.W)

btn_atan = tk.Button(buttonframe, text="tan-1", command=atan)
btn_atan.grid(row=2, column=2, sticky=tk.E+tk.W)

btn_cosec = tk.Button(buttonframe, text="cosec", command=cosec)
btn_cosec.grid(row=3, column=0, sticky=tk.E+tk.W)

btn_sec = tk.Button(buttonframe, text="sec", command=sec)
btn_sec.grid(row=3, column=1, sticky=tk.E+tk.W)

btn_cot = tk.Button(buttonframe, text="cot", command=cot)
btn_cot.grid(row=3, column=2, sticky=tk.E+tk.W)

btn_acosec = tk.Button(buttonframe, text="cosec-1", command=acosec)
btn_acosec.grid(row=4, column=0, sticky=tk.E+tk.W)

btn_asec = tk.Button(buttonframe, text="sec-1", command=asec)
btn_asec.grid(row=4, column=1, sticky=tk.E+tk.W)

btn_acot = tk.Button(buttonframe, text="cot-1", command=acot)
btn_acot.grid(row=4, column=2, sticky=tk.E+tk.W)

btn_log = tk.Button(buttonframe, text="log", command=log)
btn_log.grid(row=5, column=0, sticky=tk.E+tk.W)

btn_exp = tk.Button(buttonframe, text="e^", command=exp)
btn_exp.grid(row=5, column=1, sticky=tk.E+tk.W)

btn_power = tk.Button(buttonframe, text="^", command=power)
btn_power.grid(row=5, column=2, sticky=tk.E+tk.W)

btn_0 = tk.Button(buttonframe, text="0", command=num0)
btn_0.grid(row=6, column=0, sticky=tk.E+tk.W)

btn_1 = tk.Button(buttonframe, text="1", command=num1)
btn_1.grid(row=6, column=1, sticky=tk.E+tk.W)

btn_2 = tk.Button(buttonframe, text="2", command=num2)
btn_2.grid(row=6, column=2, sticky=tk.E+tk.W)

btn_3 = tk.Button(buttonframe, text="3", command=num3)
btn_3.grid(row=7, column=0, sticky=tk.E+tk.W)

btn_4 = tk.Button(buttonframe, text="4", command=num4)
btn_4.grid(row=7, column=1, sticky=tk.E+tk.W)

btn_5 = tk.Button(buttonframe, text="5", command=num5)
btn_5.grid(row=7, column=2, sticky=tk.E+tk.W)

btn_6 = tk.Button(buttonframe, text="6", command=num6)
btn_6.grid(row=8, column=0, sticky=tk.E+tk.W)

btn_7 = tk.Button(buttonframe, text="7", command=num7)
btn_7.grid(row=8, column=1, sticky=tk.E+tk.W)

btn_8 = tk.Button(buttonframe, text="8", command=num8)
btn_8.grid(row=8, column=2, sticky=tk.E+tk.W)

btn_9 = tk.Button(buttonframe, text="9", command=num9)
btn_9.grid(row=9, column=0, sticky=tk.E+tk.W)

btn_open_bracket = tk.Button(buttonframe, text="(", command=b_open)
btn_open_bracket.grid(row=9, column=1, sticky=tk.E+tk.W)

btn_close_bracket = tk.Button(buttonframe, text=")", command=b_close)
btn_close_bracket.grid(row=9, column=2, sticky=tk.E+tk.W)

btn_add = tk.Button(buttonframe, text="+", command=add)
btn_add.grid(row=10, column=0, sticky=tk.E+tk.W)

btn_sub = tk.Button(buttonframe, text="-", command=sub)
btn_sub.grid(row=10, column=1, sticky=tk.E+tk.W)

btn_mul = tk.Button(buttonframe, text="*", command=mul)
btn_mul.grid(row=10, column=2, sticky=tk.E+tk.W)

btn_div = tk.Button(buttonframe, text="/", command=div)
btn_div.grid(row=11, column=0, sticky=tk.E+tk.W)

btn_x = tk.Button(buttonframe, text="X", command=variable)
btn_x.grid(row=11, column=1, sticky=tk.E+tk.W)

buttonframe.pack(padx=10, pady=10)

root.mainloop()
