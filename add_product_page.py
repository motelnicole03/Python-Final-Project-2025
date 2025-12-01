import tkinter as tk
from tkinter import ttk, messagebox
from base_page import BasePage
from queries import insert_product

class AddProductPage(BasePage):
    def __init__(self, root, app):
        super().__init__(root, app)
        self.setup_ui()
    
    def setup_ui(self):
        c = self.frame.inner
        tk.Label(c, text="Add Product", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
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
        ttk.Button(btns, text="SAVE", style='Green.TButton', command=self.save_product).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="RESET", style='Blue.TButton', command=self.reset_form).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.app.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def reset_form(self):
        self.name_entry.delete(0, tk.END)
        self.brand_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.rating_spinbox.delete(0, tk.END)
        self.rating_spinbox.insert(0, 1)
        self.price_entry.delete(0, tk.END)
        self.eco_var.set("yes")

    def save_product(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Product Name is required!")
            return

        price_text = self.price_entry.get().strip()
        if not price_text:
            messagebox.showerror("Error", "Price is required!")
            return

        # --- Validate price ---
        try:
            price = float(price_text)
        except:
            messagebox.showerror("Error", "Invalid price! Please enter a number.")
            return

        # Build product data
        product = {
            "name": name,
            "brand": self.brand_entry.get(),
            "category": self.category_entry.get(),
            "eco_rating": int(self.rating_spinbox.get()),
            "price": price,
            "eco_friendly": self.eco_var.get()
        }

        # Attempt to save
        try:
            insert_product(product)
            messagebox.showinfo("Saved", "Product added successfully!")
            self.app.show_main()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add product: {str(e)}")


    def show(self):
        self.reset_form()
        super().show()