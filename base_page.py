import tkinter as tk

class BasePage:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.frame = self._create_frame()
        
    def _create_frame(self):
        outer = tk.Frame(self.root, bg="white", highlightthickness=1, highlightbackground="black")
        outer.place_forget()
        inner = tk.Frame(outer, bg="white")
        inner.pack(fill="both", expand=True, padx=20, pady=20)
        outer.inner = inner
        return outer
    
    def hide(self):
        self.frame.place_forget()
    
    def show(self):
        self.app.hide_all()
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)
