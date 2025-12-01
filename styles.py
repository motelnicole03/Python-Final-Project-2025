from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')

    style.configure('Green.TButton', foreground='white', background='#4CAF50', borderwidth=1)
    style.map('Green.TButton', background=[('active','#45A049')])

    style.configure('Red.TButton', foreground='white', background='#F44336', borderwidth=1)
    style.map('Red.TButton', background=[('active','#D32F2F')])

    style.configure('Blue.TButton', foreground='white', background='#2196F3', borderwidth=1)
    style.map('Blue.TButton', background=[('active','#1976D2')])

    style.configure('Yellow.TButton', foreground='black', background='#FFEB3B', borderwidth=1)
    style.map('Yellow.TButton', background=[('active','#FDD835')])

    style.configure('Orange.TButton', foreground='white', background='#FF9800', borderwidth=1)
    style.map('Orange.TButton', background=[('active','#FB8C00')])
