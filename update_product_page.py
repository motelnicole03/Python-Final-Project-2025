import tkinter as tk
from tkinter import ttk, messagebox
from base_page import BasePage
from queries import get_all_products, update_product

class UpdateProductPage(BasePage):
    def __init__(self, root, app):
        super().__init__(root, app)
        self.select_frame = self._create_frame()
        self.edit_frame = self._create_frame()
        self.setup_select_ui()
        self.setup_edit_ui()
        self.products = []
        self.editing_index = None

    def setup_select_ui(self):
        c = self.select_frame.inner
        tk.Label(c, text="Update Product", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        self.combo = ttk.Combobox(c, width=40)
        self.combo.pack(pady=6)
        btns = tk.Frame(c, bg="white")
        btns.pack(pady=10)
        ttk.Button(btns, text="UPDATE", style='Blue.TButton', command=self.show_edit).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.app.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def setup_edit_ui(self):
        c = self.edit_frame.inner
        tk.Label(c, text="Edit Product", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        form = tk.Frame(c, bg="white")
        form.pack(pady=6)

        # Product Name
        tk.Label(form, text="Product Name:", bg="white", anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(form, width=25)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Brand Name
        tk.Label(form, text="Brand Name:", bg="white", anchor="w").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.brand_entry = tk.Entry(form, width=25)
        self.brand_entry.grid(row=1, column=1, padx=5, pady=5)

        # Category
        tk.Label(form, text="Category:", bg="white", anchor="w").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.category_entry = tk.Entry(form, width=25)
        self.category_entry.grid(row=2, column=1, padx=5, pady=5)

        # Eco Rating
        tk.Label(form, text="Eco Rating:", bg="white", anchor="w").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.rating_spinbox = tk.Spinbox(form, from_=1, to=10, width=5)
        self.rating_spinbox.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Price
        tk.Label(form, text="Price:", bg="white", anchor="w").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.price_entry = tk.Entry(form, width=25)
        self.price_entry.grid(row=4, column=1, padx=5, pady=5)

        # Eco-Friendly
        tk.Label(form, text="Eco-Friendly:", bg="white", anchor="w").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.eco_var = tk.StringVar(value="yes")
        eco_frame = tk.Frame(form, bg="white")
        tk.Radiobutton(eco_frame, text="Yes", value="yes", variable=self.eco_var, bg="white").pack(side="left")
        tk.Radiobutton(eco_frame, text="No", value="no", variable=self.eco_var, bg="white").pack(side="left")
        eco_frame.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        btns = tk.Frame(c, bg="white")
        btns.pack(pady=20)
        ttk.Button(btns, text="SAVE", style='Green.TButton', command=self.save_update).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="RESET", style='Blue.TButton', command=self.reset_form).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.app.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def show(self):
        self.app.hide_all()
        try:
            self.products = get_all_products()
            self.combo['values'] = [p['name'] for p in self.products]
            self.select_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load products: {str(e)}")

    def show_edit(self):
        selected = self.combo.get()
        if not selected:
            messagebox.showerror("Error", "Select a product first!")
            return
        
        self.editing_index = next(i for i, p in enumerate(self.products) if p['name'] == selected)
        p = self.products[self.editing_index]
        
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, p['name'])
        self.brand_entry.delete(0, tk.END)
        self.brand_entry.insert(0, p['brand'])
        self.category_entry.delete(0, tk.END)
        self.category_entry.insert(0, p['category'])
        self.rating_spinbox.delete(0, tk.END)
        self.rating_spinbox.insert(0, p['eco_rating'])
        self.price_entry.delete(0, tk.END)
        self.price_entry.insert(0, p['price'])
        self.eco_var.set(p['eco_friendly'])
        
        self.app.hide_all()
        self.edit_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.brand_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.rating_spinbox.delete(0, tk.END)
        self.rating_spinbox.insert(0, 1)
        self.price_entry.delete(0, tk.END)
        self.eco_var.set("yes")

    def save_update(self):
        try:
            price = float(self.price_entry.get())
        except:
            messagebox.showerror("Error", "Invalid price")
            return

        product = {
            "name": self.name_entry.get(),
            "brand": self.brand_entry.get(),
            "category": self.category_entry.get(),
            "eco_rating": int(self.rating_spinbox.get()),
            "price": price,
            "eco_friendly": self.eco_var.get()
        }

        try:
            pid = self.products[self.editing_index]["id"]
            update_product(product, pid)
            messagebox.showinfo("Updated", "Product updated successfully!")
            self.app.show_main()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update product: {str(e)}")

    def hide(self):
        self.select_frame.place_forget()
        self.edit_frame.place_forget()
