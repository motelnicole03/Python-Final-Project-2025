import tkinter as tk
from tkinter import ttk
from add_product_page import AddProductPage
from view_products_page import ViewProductsPage
from update_product_page import UpdateProductPage
from delete_product_page import DeleteProductPage
from compare_products_page import CompareProductsPage
from styles import setup_styles

class EcoFriendlyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eco-Friendly Product Analyzer and Comparator")
        self.root.geometry("600x520")
        self.root.configure(bg="white")

        # Setup styles
        setup_styles()

        # Initialize pages FIRST
        self.add_page = AddProductPage(root, self)
        self.view_page = ViewProductsPage(root, self)
        self.update_page = UpdateProductPage(root, self)
        self.delete_page = DeleteProductPage(root, self)
        self.compare_page = CompareProductsPage(root, self)

        # Main menu AFTER pages are initialized
        self.create_main_menu()

        self.show_main()

    def create_main_menu(self):
        self.main_outer = tk.Frame(self.root, bg="white", highlightthickness=1, highlightbackground="black")
        self.main_outer.place(relx=0.5, rely=0.5, anchor="center", width=420, height=400)

        title = tk.Label(self.main_outer, text="Eco-Friendly Product\nAnalyzer and Comparator",
                         font=("Arial", 20, "bold"), bg="white", justify="center")
        title.pack(pady=(20, 10))

        btn_frame = tk.Frame(self.main_outer, bg="white")
        btn_frame.pack(expand=True)

        ttk.Button(btn_frame, text="Add Product", style='Green.TButton', 
                   command=self.add_page.show, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="View Products", style='Yellow.TButton', 
                   command=self.view_page.show, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="Update Product", style='Blue.TButton', 
                   command=self.update_page.show, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="Delete Product", style='Red.TButton', 
                   command=self.delete_page.show, width=25).pack(pady=6, ipadx=10, ipady=5)
        ttk.Button(btn_frame, text="Compare Products", style='Orange.TButton', 
                   command=self.compare_page.show, width=25).pack(pady=6, ipadx=10, ipady=5)

    def hide_all(self):
        self.main_outer.place_forget()
        self.add_page.hide()
        self.view_page.hide()
        self.update_page.hide()
        self.delete_page.hide()
        self.compare_page.hide()

    def show_main(self):
        self.hide_all()
        self.main_outer.place(relx=0.5, rely=0.5, anchor="center", width=420, height=400)
