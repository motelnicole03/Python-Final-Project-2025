import tkinter as tk
from tkinter import ttk, messagebox
from base_page import BasePage
from queries import get_all_products

class CompareProductsPage(BasePage):
    def __init__(self, root, app):
        super().__init__(root, app)
        self.select_frame = self._create_frame()
        self.result_frame = self._create_frame()
        self.setup_select_ui()
        self.setup_result_ui()
        self.products = []

    def setup_select_ui(self):
        c = self.select_frame.inner
        tk.Label(c, text="Compare Products", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        tk.Label(c, text="Product 1:", bg="white").pack(anchor="w")
        self.combo1 = ttk.Combobox(c, width=40)
        self.combo1.pack(pady=6)
        tk.Label(c, text="Product 2:", bg="white").pack(anchor="w")
        self.combo2 = ttk.Combobox(c, width=40)
        self.combo2.pack(pady=6)
        btns = tk.Frame(c, bg="white")
        btns.pack(pady=10)
        ttk.Button(btns, text="COMPARE", style='Orange.TButton', command=self.show_result).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.app.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def setup_result_ui(self):
        c = self.result_frame.inner
        tk.Label(c, text="Comparison Result", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        self.text_widget = tk.Text(c, width=48, height=17)
        self.text_widget.pack()
        ttk.Button(c, text="DONE", style='Green.TButton', command=self.app.show_main).pack(pady=10, ipadx=10, ipady=5)

    def show(self):
        self.app.hide_all()
        try:
            self.products = get_all_products()
            values = [p['name'] for p in self.products]
            self.combo1['values'] = values
            self.combo2['values'] = values
            self.select_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load products: {str(e)}")

    def show_result(self):
        p1 = self.combo1.get()
        p2 = self.combo2.get()
        
        if p1 == "" or p2 == "":
            messagebox.showerror("Error", "Select two products")
            return
        if p1 == p2:
            messagebox.showerror("Error", "Choose different products!")
            return
        
        a = next(p for p in self.products if p['name'] == p1)
        b = next(p for p in self.products if p['name'] == p2)
        
        if a['eco_rating'] == b['eco_rating'] and a['eco_friendly'] == b['eco_friendly']:
            better_name = "Both products"
            reason_text = "Both products are equally good. \n 🌱 Choose based on your preference!"
        else:
            candidates = [a, b]
            eco_candidates = [c for c in candidates if c['eco_friendly'] == "yes"]
            if eco_candidates:
                better = max(eco_candidates, key=lambda x: x['eco_rating'])
            else:
                better = max([a, b], key=lambda x: x['eco_rating'])
            better_name = better['name']
            reason_parts = []
            if better['eco_friendly'] == "yes":
                reason_parts.append("more eco-friendly")
            if better['eco_rating'] >= 8:
                reason_parts.append(f"high Eco-Rating ({better['eco_rating']})")
            reason_text = f"Pick {better_name} — " + " and ".join(reason_parts) + ""
        
        self.app.hide_all()
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END,
            f"{a['name']}\n  Eco-Rating: {a['eco_rating']}\n  Price: ₱{a['price']}\n  Eco-Friendly: {a['eco_friendly']}\n\n"
            f"{b['name']}\n  Eco-Rating: {b['eco_rating']}\n  Price: ₱{b['price']}\n  Eco-Friendly: {b['eco_friendly']}\n\n"
            f"✔ Suggested Product: {better_name}\n"
            f"Reason: {reason_text}\n"
        )
        self.result_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    def hide(self):
        self.select_frame.place_forget()
        self.result_frame.place_forget()