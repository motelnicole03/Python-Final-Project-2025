import tkinter as tk
from tkinter import ttk
from base_page import BasePage
from queries import get_all_products

class ViewProductsPage(BasePage):
    def __init__(self, root, app):
        super().__init__(root, app)
        self.setup_ui()
    
    def setup_ui(self):
        c = self.frame.inner
        tk.Label(c, text="View Products", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        self.text_widget = tk.Text(c, width=48, height=18)
        self.text_widget.pack()
        ttk.Button(c, text="BACK", style='Red.TButton', command=self.app.show_main).pack(pady=10, ipadx=10, ipady=5)

    def show(self):
        self.app.hide_all()
        self.load_products()
        self.frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    def load_products(self):
        self.text_widget.delete(1.0, tk.END)
        try:
            products = get_all_products()
            if not products:
                self.text_widget.insert(tk.END, "NO PRODUCTS AVAILABLE")
            else:
                for i, p in enumerate(products, 1):
                    self.text_widget.insert(tk.END,
                        f"{i}. {p['name']}\nBrand: {p['brand']}\nCategory: {p['category']}\n"
                        f"Eco-Rating: {p['eco_rating']}\nPrice: ₱{p['price']}\nEco-Friendly: {p['eco_friendly']}\n\n")
        except Exception as e:
            self.text_widget.insert(tk.END, f"Error loading products: {str(e)}")
