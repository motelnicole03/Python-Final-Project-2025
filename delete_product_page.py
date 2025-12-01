import tkinter as tk
from tkinter import ttk, messagebox
from base_page import BasePage
from queries import get_all_products, delete_product

class DeleteProductPage(BasePage):
    def __init__(self, root, app):
        super().__init__(root, app)
        self.products = []
        self.setup_ui()

    def setup_ui(self):
        c = self.frame.inner
        tk.Label(c, text="Delete Product", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        self.combo = ttk.Combobox(c, width=40)
        self.combo.pack(pady=8)
        btns = tk.Frame(c, bg="white")
        btns.pack(pady=8)
        ttk.Button(btns, text="DELETE", style='Green.TButton', command=self.delete).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.app.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def show(self):
        self.app.hide_all()
        try:
            self.products = get_all_products()
            self.combo['values'] = [p['name'] for p in self.products]
            self.frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load products: {str(e)}")

    def delete(self):
        selected = self.combo.get()
        if not selected:
            messagebox.showerror("Error", "Select a product")
            return
        
        try:
            pid = next(p["id"] for p in self.products if p["name"] == selected)
            delete_product(pid)
            messagebox.showinfo("Deleted", "Product deleted successfully!")
            self.app.show_main()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete product: {str(e)}")
