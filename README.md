import tkinter as tk
from tkinter import ttk, messagebox

class EcoFriendlyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eco-Friendly Product Analyzer and Comparator")
        self.root.geometry("600x520")
        self.root.configure(bg="white")

        self.products = []

        # -------------------
        # SETUP STYLES
        # -------------------
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

        # -------------------
        # MAIN MENU BOX
        # -------------------
        self.main_outer = tk.Frame(root, bg="white", highlightthickness=1, highlightbackground="black")
        self.main_outer.place(relx=0.5, rely=0.5, anchor="center", width=420, height=400)

        title = tk.Label(self.main_outer, text="Eco-Friendly Product\nAnalyzer and Comparator",
                         font=("Arial", 20, "bold"), bg="white", justify="center")
        title.pack(pady=(20, 10))

        btn_frame = tk.Frame(self.main_outer, bg="white")
        btn_frame.pack(expand=True)

        ttk.Button(btn_frame, text="Add Product", style='Green.TButton', command=self.show_add, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="View Products", style='Yellow.TButton', command=self.show_view, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="Update Product", style='Blue.TButton', command=self.show_update, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="Delete Product", style='Red.TButton', command=self.show_delete, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="Compare Products", style='Orange.TButton', command=self.show_compare, width=25).pack(pady=6, ipadx=10, ipady=5)

        # -------------------
        # PAGES
        # -------------------
        self.add_frame = self.make_box()
        self.view_frame = self.make_box()
        self.update_select_frame = self.make_box()
        self.update_edit_frame = self.make_box()
        self.delete_frame = self.make_box()
        self.compare_select_frame = self.make_box()
        self.compare_result_frame = self.make_box()

        self.setup_add()
        self.setup_view()
        self.setup_update_select()
        self.setup_update_edit()
        self.setup_delete()
        self.setup_compare_select()
        self.setup_compare_result()

        self.show_main()

    # -----------------------------
    # BOX UTILITY
    # -----------------------------
    def make_box(self):
        outer = tk.Frame(self.root, bg="white", highlightthickness=1, highlightbackground="black")
        outer.place_forget()
        inner = tk.Frame(outer, bg="white")
        inner.pack(fill="both", expand=True, padx=20, pady=20)
        outer.inner = inner
        return outer

    def hide_all(self):
        self.main_outer.place_forget()
        for f in [self.add_frame, self.view_frame, self.update_select_frame, self.update_edit_frame,
                  self.delete_frame, self.compare_select_frame, self.compare_result_frame]:
            f.place_forget()

    def show_main(self):
        self.hide_all()
        self.main_outer.place(relx=0.5, rely=0.5, anchor="center", width=420, height=400)

    # ===============================
    # ADD PAGE
    # ===============================
    def show_add(self):
        self.hide_all()
        self.reset_add_form()
        self.add_frame.place(relx=0.5, rely=0.5, anchor="center", width=420, height=420)

    def setup_add(self):
        c = self.add_frame.inner
        tk.Label(c, text="Add Product", font=("Arial", 14, "bold"), bg="white").pack(pady=6)
        form = tk.Frame(c, bg="white"); form.pack(pady=6)

        # Entries
        tk.Label(form, text="Product Name:", bg="white", anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.add_name = tk.Entry(form, width=25); self.add_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Brand Name:", bg="white", anchor="w").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.add_brand = tk.Entry(form, width=25); self.add_brand.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form, text="Category:", bg="white", anchor="w").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.add_category = tk.Entry(form, width=25); self.add_category.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form, text="Eco Rating:", bg="white", anchor="w").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.add_rating = tk.Spinbox(form, from_=1, to=10, width=5); self.add_rating.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form, text="Price:", bg="white", anchor="w").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.add_price = tk.Entry(form, width=25); self.add_price.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form, text="Eco-Friendly:", bg="white", anchor="w").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.add_eco_var = tk.StringVar(value="yes")
        eco_frame = tk.Frame(form, bg="white")
        tk.Radiobutton(eco_frame, text="Yes", value="yes", variable=self.add_eco_var, bg="white").pack(side="left")
        tk.Radiobutton(eco_frame, text="No", value="no", variable=self.add_eco_var, bg="white").pack(side="left")
        eco_frame.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        btns = tk.Frame(c, bg="white"); btns.pack(pady=20)
        ttk.Button(btns, text="SAVE", style='Green.TButton', command=self.add_product).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="RESET", style='Blue.TButton', command=self.reset_add_form).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def reset_add_form(self):
        self.add_name.delete(0, tk.END)
        self.add_brand.delete(0, tk.END)
        self.add_category.delete(0, tk.END)
        self.add_rating.delete(0, tk.END); self.add_rating.insert(0, 1)
        self.add_price.delete(0, tk.END)
        self.add_eco_var.set("yes")

    def add_product(self):
        try: price = float(self.add_price.get())
        except: messagebox.showerror("Error","Invalid price!"); return
        self.products.append({
            "name": self.add_name.get(),
            "brand": self.add_brand.get(),
            "category": self.add_category.get(),
            "eco_rating": int(self.add_rating.get()),
            "price": price,
            "eco_friendly": self.add_eco_var.get()
        })
        messagebox.showinfo("Saved","Product added successfully!"); self.show_main()

    # ===============================
    # VIEW PAGE
    # ===============================
    def setup_view(self):
        c = self.view_frame.inner
        tk.Label(c, text="View Products", font=("Arial",14,"bold"), bg="white").pack(pady=6)
        self.view_text = tk.Text(c,width=48,height=18)
        self.view_text.pack()
        ttk.Button(c, text="BACK", style='Red.TButton', command=self.show_main).pack(pady=10, ipadx=10, ipady=5)

    def show_view(self):
        self.hide_all()
        self.view_text.delete(1.0,tk.END)
        if not self.products: self.view_text.insert(tk.END,"NO PRODUCTS AVAILABLE")
        else:
            for i,p in enumerate(self.products,1):
                self.view_text.insert(tk.END,
                    f"{i}. {p['name']}\nBrand: {p['brand']}\nCategory: {p['category']}\n"
                    f"Eco-Rating: {p['eco_rating']}\nPrice: ₱{p['price']}\nEco-Friendly: {p['eco_friendly']}\n\n")
        self.view_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)

    # ===============================
    # UPDATE PAGE
    # ===============================
    def setup_update_select(self):
        c = self.update_select_frame.inner
        tk.Label(c,text="Update Product", font=("Arial",14,"bold"),bg="white").pack(pady=6)
        self.update_combo = ttk.Combobox(c,width=40)
        self.update_combo.pack(pady=6)
        btns = tk.Frame(c,bg="white"); btns.pack(pady=10)
        ttk.Button(btns,text="UPDATE",style='Blue.TButton',command=self.show_update_edit).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns,text="CANCEL",style='Red.TButton',command=self.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def show_update(self):
        self.hide_all()
        self.update_combo['values'] = [p['name'] for p in self.products]
        self.update_select_frame.place(relx=0.5,rely=0.5,anchor="center",width=420,height=420)

    def setup_update_edit(self):
        c = self.update_edit_frame.inner
        tk.Label(c, text="Edit Product", font=("Arial",14,"bold"), bg="white").pack(pady=6)
        form = tk.Frame(c, bg="white"); form.pack(pady=6)

        # Entries like Add Page
        tk.Label(form, text="Product Name:", bg="white", anchor="w").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.u_name = tk.Entry(form, width=25); self.u_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form, text="Brand Name:", bg="white", anchor="w").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.u_brand = tk.Entry(form, width=25); self.u_brand.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form, text="Category:", bg="white", anchor="w").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.u_category = tk.Entry(form, width=25); self.u_category.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(form, text="Eco Rating:", bg="white", anchor="w").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.u_rating = tk.Spinbox(form, from_=1, to=10, width=5); self.u_rating.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        tk.Label(form, text="Price:", bg="white", anchor="w").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.u_price = tk.Entry(form, width=25); self.u_price.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form, text="Eco-Friendly:", bg="white", anchor="w").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.u_eco = tk.StringVar(value="yes")
        eco_frame = tk.Frame(form, bg="white")
        tk.Radiobutton(eco_frame, text="Yes", value="yes", variable=self.u_eco, bg="white").pack(side="left")
        tk.Radiobutton(eco_frame, text="No", value="no", variable=self.u_eco, bg="white").pack(side="left")
        eco_frame.grid(row=5, column=1, padx=5, pady=5, sticky="w")

        # Buttons
        btns = tk.Frame(c, bg="white"); btns.pack(pady=20)
        ttk.Button(btns, text="SAVE", style='Green.TButton', command=self.update_product).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="RESET", style='Blue.TButton', command=self.reset_update_form).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns, text="CANCEL", style='Red.TButton', command=self.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def show_update_edit(self):
        selected = self.update_combo.get()
        if not selected: messagebox.showerror("Error","Select a product first!"); return
        self.editing_index = next(i for i,p in enumerate(self.products) if p['name']==selected)
        p = self.products[self.editing_index]
        self.u_name.delete(0,tk.END); self.u_name.insert(0,p['name'])
        self.u_brand.delete(0,tk.END); self.u_brand.insert(0,p['brand'])
        self.u_category.delete(0,tk.END); self.u_category.insert(0,p['category'])
        self.u_rating.delete(0,tk.END); self.u_rating.insert(0,p['eco_rating'])
        self.u_price.delete(0,tk.END); self.u_price.insert(0,p['price'])
        self.u_eco.set(p['eco_friendly'])
        self.hide_all(); self.update_edit_frame.place(relx=0.5,rely=0.5,anchor="center",width=420,height=420)

    def reset_update_form(self):
        self.u_name.delete(0, tk.END)
        self.u_brand.delete(0, tk.END)
        self.u_category.delete(0, tk.END)
        self.u_rating.delete(0, tk.END); self.u_rating.insert(0,1)
        self.u_price.delete(0, tk.END)
        self.u_eco.set("yes")

    def update_product(self):
        try: price = float(self.u_price.get())
        except: messagebox.showerror("Error","Invalid price"); return
        self.products[self.editing_index] = {
            "name": self.u_name.get(),
            "brand": self.u_brand.get(),
            "category": self.u_category.get(),
            "eco_rating": int(self.u_rating.get()),
            "price": price,
            "eco_friendly": self.u_eco.get()
        }
        messagebox.showinfo("Updated","Product updated successfully!"); self.show_main()

    # ===============================
    # DELETE PAGE
    # ===============================
    def setup_delete(self):
        c = self.delete_frame.inner
        tk.Label(c,text="Delete Product", font=("Arial",14,"bold"),bg="white").pack(pady=6)
        self.del_combo = ttk.Combobox(c,width=40); self.del_combo.pack(pady=8)
        btns = tk.Frame(c,bg="white"); btns.pack(pady=8)
        ttk.Button(btns,text="DELETE",style='Green.TButton',command=self.delete_product).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns,text="CANCEL",style='Red.TButton',command=self.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def show_delete(self):
        self.hide_all()
        self.del_combo['values'] = [p['name'] for p in self.products]
        self.delete_frame.place(relx=0.5,rely=0.5,anchor="center",width=420,height=420)

    def delete_product(self):
        selected = self.del_combo.get()
        if not selected: messagebox.showerror("Error","Select a product"); return
        self.products = [p for p in self.products if p['name']!=selected]
        messagebox.showinfo("Deleted","Product deleted successfully!"); self.show_main()

    # ===============================
    # COMPARE PAGE
    # ===============================
    def setup_compare_select(self):
        c = self.compare_select_frame.inner
        tk.Label(c,text="Compare Products", font=("Arial",14,"bold"),bg="white").pack(pady=6)
        tk.Label(c,text="Product 1:", bg="white").pack(anchor="w")
        self.com1 = ttk.Combobox(c,width=40); self.com1.pack(pady=6)
        tk.Label(c,text="Product 2:", bg="white").pack(anchor="w")
        self.com2 = ttk.Combobox(c,width=40); self.com2.pack(pady=6)
        btns = tk.Frame(c,bg="white"); btns.pack(pady=10)
        ttk.Button(btns,text="COMPARE",style='Orange.TButton',command=self.show_compare_result).pack(side="left", padx=6, ipadx=10, ipady=5)
        ttk.Button(btns,text="CANCEL",style='Red.TButton',command=self.show_main).pack(side="left", padx=6, ipadx=10, ipady=5)

    def show_compare(self):
        self.hide_all()
        values = [p['name'] for p in self.products]
        self.com1['values'] = values; self.com2['values'] = values
        self.compare_select_frame.place(relx=0.5,rely=0.5,anchor="center",width=420,height=420)

    def setup_compare_result(self):
        c = self.compare_result_frame.inner
        tk.Label(c,text="Comparison Result", font=("Arial",14,"bold"),bg="white").pack(pady=6)
        self.result_text = tk.Text(c,width=48,height=17); self.result_text.pack()
        ttk.Button(c,text="DONE",style='Green.TButton',command=self.show_main).pack(pady=10, ipadx=10, ipady=5)

    def show_compare_result(self):
        p1 = self.com1.get()
        p2 = self.com2.get()
    
    # Basic validation
        if p1 == "" or p2 == "":
            messagebox.showerror("Error","Select two products")
            return
        if p1 == p2:
            messagebox.showerror("Error","Choose different products!")
            return

    # Get product data
        a = next(p for p in self.products if p['name'] == p1)
        b = next(p for p in self.products if p['name'] == p2)

        # Check for tie (same eco rating and eco-friendly status)
        if a['eco_rating'] == b['eco_rating'] and a['eco_friendly'] == b['eco_friendly']:
            tie = True
        else:
            tie = False

        if tie:
            better_name = "Both products"
            reason_text = "Both products are equally eco-friendly. 🌱 Choose based on your preference!"
        else:
            # Normal comparison: prefer eco-friendly first, then higher rating
            candidates = [a, b]
            eco_candidates = [c for c in candidates if c['eco_friendly'] == "yes"]
            if eco_candidates:
                better = max(eco_candidates, key=lambda x: x['eco_rating'])
            else:
                better = max([a, b], key=lambda x: x['eco_rating'])
            better_name = better['name']

            # Dynamic convincing & rhyming reason
            reason_parts = []
            if better['eco_friendly'] == "yes":
                reason_parts.append("more eco-friendly")
            if better['eco_rating'] >= 8:
                reason_parts.append(f"high Eco-Rating ({better['eco_rating']})")
            reason_text = f"Pick {better_name} — " + " and ".join(reason_parts) + ", a greener choice for the earth! 🌿"

        # Display results
        self.hide_all()
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END,
            f"{a['name']}\n  Eco-Rating: {a['eco_rating']}\n  Price: ₱{a['price']}\n  Eco-Friendly: {a['eco_friendly']}\n\n"
            f"{b['name']}\n  Eco-Rating: {b['eco_rating']}\n  Price: ₱{b['price']}\n  Eco-Friendly: {b['eco_friendly']}\n\n"
            f"✔ Suggested Product: {better_name}\n"
            f"Reason: More Eco-Friendly.\n"
            
        )
        self.compare_result_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=450)


# RUN APP
root = tk.Tk()
app = EcoFriendlyApp(root)
root.mainloop()
