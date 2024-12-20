from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import random
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Bill Software")

        # Variable
        z = random.randint(1000, 10000)
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill_no = StringVar()
        self.c_bill_no.set(z)
        self.c_email = StringVar()
        self.c_search_bill = StringVar()
        self.c_product = StringVar()
        self.c_price = IntVar()
        self.c_quantity = IntVar()
        self.c_sub_total = StringVar()
        self.c_tax_input = StringVar()
        self.c_total = StringVar()

        # Product Categories list
        self.Category = [
            "Select Option",
            "Clothing",
            "Electronic",
            "Grocery",
            "Mobiles",
        ]

        # Clothing
        self.SubCatClothing = [
            "Select Option",
            "Pant",
            "T-Shirt",
            "Shirt",
            "Cargo",
            "Shoes",
        ]
        # Pant
        self.pant = ["Select Option", "Levis", "Gucci", "Puma", "Nike", "Addidas"]
        self.price_levis = 2500
        self.price_Gucci = 2000
        self.puma = 2400
        self.Nike = 3500
        self.addidas = 2800
        # T-shirt
        self.Tshirt = ["Select Option", "Spykar", "Lookout", "Mufti", "Peter England"]
        self.spykar = 5000
        self.lookout = 3000
        self.Mufti = 4000
        self.peter = 2500
        # Shirt
        self.Shirt = [
            "Select Option",
            "Levis",
            "Gucci",
            "Puma",
            "Nike",
            "Addidas",
            "Mufti",
            "Peter England",
        ]
        self.shirt_levis = 3000
        self.shirt_Gucci = 3500
        self.shirt_Nike = 2500
        self.shirt_puma = 3000
        self.shirt_Addidas = 4000
        self.shirt_mufti = 3200
        self.shirt_peter = 2800

        # Cargo
        self.cargo = [
            "Select Option",
            "Dennis Lingo",
            "HIGHLANDER",
            "KILLER",
            "Snitch",
            "Spykar",
        ]
        self.Dennis_Lingo = 8000
        self.Highlander = 5000
        self.Killer = 4500
        self.Sntch = 4800
        self.cargo_spykar = 3800

        # Shoes
        self.shoes = ["Select Option", "Woodland", "Sparx", "Addidas", "Puma", "Nike"]
        self.woodland = 3000
        self.sparx = 2000
        self.shoes_puma = 2500
        self.shoes_Addidas = 1500
        self.shoes_nike = 2000

        # Electronic
        self.Sub_Elect = [
            "Select Option",
            "Laptop",
            "Bluetooth",
            "TV",
            "Powerbank",
            "Tablet",
        ]

        # laptop
        self.Laptop = ["Select Option", "Acer", "Dell", "Asus", "Hp", "Apple", "Lenovo"]
        self.Dell = 60000
        self.Hp = 65000
        self.Acer = 45000
        self.Apple = 80000
        self.Asus = 55000
        self.Lenovo = 60000

        # Bluetooth
        self.Bluetooth = ["Select Option", "Boat", "Kdm", "Apple", "OnePlus", "Sony"]
        self.Boat = 1500
        self.Kdm = 800
        self.Blue_Apple = 5000
        self.oneplus = 1200
        self.sony = 600

        # Tv
        self.TV = ["Select Option", "Sony", "LG", "Vediocon", "Samsung", "SanSui"]

        self.Sony = 25000
        self.Lg = 30000
        self.Vedio = 20000
        self.Samsung = 35000
        self.Sansui = 12000

        # Power Bank
        self.power = [
            "Select Option",
            "Oneplus",
            "Apple",
            "Redmi",
            "Kdm",
        ]
        self.power_oneplus = 2000
        self.power_apple = 5000
        self.power_redmi = 1500
        self.power_kdm = 2500

        # Tablets
        self.Tablet = ["Select Option", "Oneplus", "Apple", "Realme", "Sony", "Lenovo"]

        self.tablets_oneplus = 10000
        self.tablets_apple = 20000
        self.tablets_realme = 15000
        self.tablets_Sony = 8000
        self.tablets_lenovo = 9000

        self.Sub_Grocery = [
            "Select Option",
            "Biscuits",
            "Shampo",
            "Sugar",
            "Pasta",
            "Oil",
        ]
        # BisCuits
        self.Biscuits = [
            "Select Option",
            "Mari gold",
            "Parle",
            "Jim Jam",
            "Happy Happy",
        ]
        self.Bis_Mari = 20
        self.Bis_parle = 10
        self.Bis_Jim = 10
        self.Bis_Happy = 20

        # Shampo
        self.Shampo = ["Select Option", "Dove", "Cleanic Plus", "Sunsulk", "Lux"]
        self.sham_Dove = 80
        self.sham_cleanic = 50
        self.sham_sun = 45
        self.sham_lux = 60

        # Sugar
        self.Sugar = ["Select Option", "Thin Sugar", "Fat Sugar"]
        self.sugar_thin = 40
        self.sugar_fat = 42
        # Pasta
        self.Pasta = ["Select Option", "Small pasta", "Medium Pasta"]
        self.pas_small = 50
        self.pas_medium = 60
        # oil
        self.oil = ["Select Option", "Sunflow", "Priya", "Coconut oil", "Peanut oil"]
        self.oil_sunflow = 150
        self.oil_priya = 130
        self.oil_coco = 140
        self.oil_Peanut = 120
        # Mobile
        self.Sub_Mobile = [
            "Select Option",
            "Samsung",
            "Redmi",
            "Apple",
        ]
        self.mob_samsung = ["Select Option", "S21", "S24 ultra", "Samsung Folded"]
        self.mob_sam21 = (50000,)
        self.mob_sam24 = (60000,)
        self.mob_sam_ultra = (100000,)
        self.mob_sam_fold = (150000,)

        self.mob_Redmi = [
            "Select Option",
            "redmi note 10",
            "redmi note 11",
            "redmi note 12",
            "redmi series",
            "redmi 13T 5G",
        ]
        self.mob_red10 = (10000,)
        self.mob_red11 = (12000,)
        self.mob_red12 = (13000,)
        self.mob_red13 = (16000,)
        self.mob_red13T = (30000,)

        self.mob_Apple = [
            "Select Option",
            "Iphone-12",
            "Iphone-13",
            "Iphone-14",
            "Iphone-15",
            "Iphone-15 pro",
        ]
        self.apple_12 = (40000,)
        self.apple_13 = (60000,)
        self.apple_14 = (70000,)
        self.apple_15 = (90000,)
        self.apple_15pro = (120000,)

        # Image
        img = Image.open("image/image.jpeg")
        img = img.resize((1530, 150), Image.ANTIALIAS)
        self.phoneimg = ImageTk.PhotoImage(img)

        # Specify the desired width and height

        lbl_img = Label(self.root, image=self.phoneimg)
        lbl_img.place(x=0, y=0, width=1530, height=150)

        lbl_title = Label(
            self.root,
            text="BILLING SOFTWARE",
            font=("time new roman", 30, "bold"),
            bg="white",
        )
        lbl_title.place(x=0, y=130, width=1530, height=45)

        # Customer section
        Main_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="white")
        Main_Frame.place(x=0, y=175, width=1530, height=620)

        Cust_Frame = LabelFrame(
            Main_Frame,
            text="Customer",
            font=("time new roman", 12, "bold"),
            bg="white",
            fg="black",
        )
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        self.lbl_mob = Label(
            Cust_Frame,
            text="Mobile No.",
            font=("arial", 10, "bold"),
            bg="white",
        )
        self.lbl_mob.grid(row=0, column=0, sticky=W, padx=5, pady=4)

        self.entry_mob = ttk.Entry(
            Cust_Frame, font=("arial", 10, "bold"), width=24, textvariable=self.c_phone
        )
        self.entry_mob.grid(row=0, column=1)

        self.lbl_CoustomerName = Label(
            Cust_Frame,
            font=("arial", 10, "bold"),
            bg="white",
            text="Customer Name",
            bd=4,
        )
        self.lbl_CoustomerName.grid(row=1, column=0, sticky=W, padx=5, pady=4)

        self.txtCustomerName = ttk.Entry(
            Cust_Frame, font=("arial", 10, "bold"), width=24, textvariable=self.c_name
        )
        self.txtCustomerName.grid(row=1, column=1, sticky=W, padx=5, pady=4)

        self.lbl_CoustomerName = Label(
            Cust_Frame,
            font=("arial", 10, "bold"),
            bg="white",
            text="Email",
            bd=4,
        )
        self.lbl_CoustomerName.grid(row=2, column=0, sticky=W, padx=5, pady=4)

        self.txtCustomerEmail = ttk.Entry(
            Cust_Frame, font=("arial", 10, "bold"), width=24, textvariable=self.c_email
        )
        self.txtCustomerEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # Product Section
        Product_Frame = LabelFrame(
            Main_Frame,
            text="Product",
            font=("time new roman", 12, "bold"),
            bg="white",
            fg="black",
        )
        Product_Frame.place(x=370, y=5, width=720, height=140)
        # Category
        self.lblCategory = Label(
            Product_Frame,
            font=("arial", 10, "bold"),
            bg="white",
            text="Select Categories",
            bd=4,
        )
        self.lblCategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.Combo_Catergory = ttk.Combobox(
            Product_Frame,
            value=self.Category,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )
        self.Combo_Catergory.current(0)
        self.Combo_Catergory.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Catergory.bind("<<ComboboxSelected>>", self.Categories)

        # Sub Category
        self.lblSubCategory = Label(
            Product_Frame,
            font=("arial", 10, "bold"),
            bg="white",
            text="Sub Category",
            bd=4,
        )
        self.lblSubCategory.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.ComboSubCatergory = ttk.Combobox(
            Product_Frame,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
        )

        self.ComboSubCatergory.grid(row=1, column=1, sticky=W, padx=5, pady=5)
        self.ComboSubCatergory.bind("<<ComboboxSelected>>", self.Product_add)
        #  Product
        self.lblProCategory = Label(
            Product_Frame,
            font=("arial", 10, "bold"),
            bg="white",
            text="Product Name",
            bd=4,
        )
        self.lblProCategory.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.lblCombo_Catergory = ttk.Combobox(
            Product_Frame,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
            textvariable=self.c_product,
        )
        self.lblCombo_Catergory.grid(row=2, column=1, sticky=W, padx=5, pady=5)
        self.lblCombo_Catergory.bind("<<ComboboxSelected>>", self.CPrice)
        # Price
        self.lblPriCategory = Label(
            Product_Frame, font=("arial", 10, "bold"), bg="white", text="Price", bd=4
        )
        self.lblPriCategory.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.Price_Cat = ttk.Combobox(
            Product_Frame,
            font=("arial", 12, "bold"),
            width=24,
            state="readonly",
            textvariable=self.c_price,
        )
        self.Price_Cat.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        self.lblQuaCategory = Label(
            Product_Frame, font=("arial", 10, "bold"), bg="white", text="Quantity", bd=4
        )
        self.lblQuaCategory.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        self.Quantity = ttk.Entry(
            Product_Frame,
            font=("arial", 12, "bold"),
            width=24,
            textvariable=self.c_quantity,
        )
        self.Quantity.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Search
        Search_frame = Frame(Main_Frame, bd=2, bg="white")
        Search_frame.place(x=1100, y=15, width=500, height=40)

        self.lblBillSearch = Label(
            Search_frame,
            font=("arial", 10, "bold"),
            fg="white",
            bg="black",
            text="Bill Number",
            bd=4,
        )
        self.lblBillSearch.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.txt_Entry_Search = ttk.Entry(
            Search_frame,
            font=("arial", 12, "bold"),
            width=24,
            textvariable=self.c_search_bill,
        )
        self.txt_Entry_Search.grid(row=0, column=1, sticky=W, padx=0)

        self.BtnAddToCart = Button(
            Search_frame,
            text="Search",
            font=("arial", 10, "bold"),
            bg="black",
            fg="white",
            width=8,
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=0, column=2, padx=2)

        # Rightframe_billing area
        Right_label_frame = LabelFrame(
            Main_Frame,
            text="Bill Area",
            font=("arial", 12, "bold"),
            bg="white",
            fg="black",
        )
        Right_label_frame.place(x=1100, y=50, width=400, height=550)

        scroll_y = Scrollbar(Right_label_frame, orient=VERTICAL)
        self.textarea = Text(
            Right_label_frame,
            yscrollcommand=scroll_y.set,
            bg="white",
            fg="black",
            font=("arial", 12, "bold"),
        )
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter LabelFrame
        Button_Frame = LabelFrame(
            Main_Frame,
            text="Bill Counter",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="black",
        )
        Button_Frame.place(x=0, y=200, width=1090, height=180)

        # Sub total
        self.lblSubtotal = Label(
            Button_Frame, font=("arial", 10, "bold"), bg="white", text="Sub Total", bd=4
        )
        self.lblSubtotal.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubtotal = ttk.Entry(
            Button_Frame,
            font=("arial", 12, "bold"),
            width=26,
            textvariable=self.c_sub_total,
        )
        self.EntrySubtotal.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        # Giv Tax
        self.lblGovtax = Label(
            Button_Frame, font=("arial", 10, "bold"), bg="white", text="Gov Tax", bd=4
        )
        self.lblGovtax.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubtotal = ttk.Entry(
            Button_Frame,
            font=("arial", 12, "bold"),
            width=26,
            textvariable=self.c_tax_input,
        )
        self.EntrySubtotal.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        # Total
        self.lblTotal = Label(
            Button_Frame, font=("arial", 10, "bold"), bg="white", text="Total", bd=4
        )
        self.lblTotal.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubtotal = ttk.Entry(
            Button_Frame,
            font=("arial", 12, "bold"),
            width=26,
            textvariable=self.c_total,
        )
        self.EntrySubtotal.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        # # Button Frame
        Btn_Frame = Frame(Button_Frame, bd=2, bg="white")
        Btn_Frame.place(x=350, y=10)

        self.BtnAddToCart = Button(
            Btn_Frame,
            command=self.Additem,
            text="Add to Cart",
            font=("arial", 15, "bold"),
            bg="black",
            fg="white",
            width=15,
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=0, column=0)

        # Button_Frame
        Btn_Frame = Frame(Button_Frame, bd=2, bg="white")
        Btn_Frame.place(x=620, y=10)

        self.BtnAddToCart = Button(
            Btn_Frame,
            text="Generate Bill",
            font=("arial", 15, "bold"),
            bg="black",
            fg="white",
            command=self.gen_bill,
            width=15,
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=0, column=2)
        # Button_Frame
        Btn_Frame = Frame(Button_Frame, bd=2, bg="white")
        Btn_Frame.place(x=870, y=10)

        self.BtnAddToCart = Button(
            Btn_Frame,
            text="Save Bill",
            font=("arial", 15, "bold"),
            bg="black",
            fg="white",
            width=15,
            command=self.save_bill,
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=0, column=3)

        # Button_Frame
        Btn_Frame = Frame(Button_Frame, bd=2, bg="white")
        Btn_Frame.place(x=350, y=80)

        self.BtnAddToCart = Button(
            Btn_Frame,
            text="Clear",
            font=("arial", 15, "bold"),
            bg="black",
            fg="white",
            width=15,
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=1, column=0)

        # Button_Frame
        Btn_Frame = Frame(Button_Frame, bd=2, bg="white")
        Btn_Frame.place(x=620, y=80)

        self.BtnAddToCart = Button(
            Btn_Frame,
            text="Print",
            font=("arial", 15, "bold"),
            bg="black",
            fg="white",
            width=15,
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=1, column=1)

        # Button_Frame
        Btn_Frame = Frame(Button_Frame, bd=2, bg="white")
        Btn_Frame.place(x=870, y=80)

        self.BtnAddToCart = Button(
            Btn_Frame,
            text="Exit",
            font=("arial", 15, "bold"),
            bg="black",
            width=15,
            fg="white",
            cursor="hand2",
        )
        self.BtnAddToCart.grid(row=1, column=2)
        self.welcome()
        self.l = []

    # Function declaration
    def Additem(self):
        Tax = 1
        self.n = self.c_price.get()
        self.m = self.c_quantity.get() * self.n
        self.l.append(self.m)
        if self.c_product.get() == "Select Option":
            messagebox.showerror("Error", "Please Select the Product Name")
        else:
            self.textarea.insert(
                END,
                f"\n {self.c_product.get()}\t\t\t{self.c_quantity.get()} \t {self.m}",
            )
            self.c_sub_total.set(str("Rs.%.2f" % (sum(self.l))))
            self.c_tax_input.set(
                str("Rs.%.2f" % ((((sum(self.l)) - (self.c_price.get())) * Tax) / 100))
            )
            self.c_total.set(
                str(
                    "Rs.%.2f"
                    % (
                        (
                            (sum(self.l))
                            + ((((sum(self.l)) - (self.c_price.get())) * Tax) / 100)
                        )
                    )
                )
            )

    def gen_bill(self):
        if self.c_product.get() == "Select Option":
            messagebox.showerror("Error", "Please Add to Cart")
        else:
            text = self.textarea.get(10.0, (10.0 + float(len(self.l))))
            self.welcome()
            self.textarea.insert(END, text)

            self.textarea.insert(END, "\n =========================================")
            self.textarea.insert(END, f"\n Sub Amount: \t\t\t{self.c_sub_total.get()}")
            self.textarea.insert(END, f"\n Tax: \t\t\t{self.c_tax_input.get()}")
            self.textarea.insert(END, f"\n Total: \t\t\t{self.c_total.get()}")
            self.textarea.insert(END, "\n =========================================")

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you Want to save bill")
        if op > 0:
            self.bill_data = self.textarea.get(1.0, END)
            f1 = open("bills/" + str(self.c_bill_no.get()) + ".txt", "w")
            f1.write(self.bill_data)
            op = messagebox.showinfo(
                "Saved", f"Bill no. {self.c_bill_no.get()} Saved Succesfully"
            )
            f1.close()

    # def bill_search(self):
    #     if self.c_bill_no.get() == self.c_search_bill:
    #         self.textarea.insert(END, f"{self.welcome}")

    def welcome(self):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, "\t Welcome to Walmart")
        self.textarea.insert(END, f"\n Bill Number:{self.c_bill_no.get()}")
        self.textarea.insert(END, f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END, f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END, f"\n Email:{self.c_email.get()}")

        self.textarea.insert(END, "\n =========================================")
        self.textarea.insert(END, "\nProduct\t\t\tQty \t Price")
        self.textarea.insert(END, "\n =========================================\n")

    def Categories(self, event=""):
        if self.Combo_Catergory.get() == "Clothing":
            self.ComboSubCatergory.config(values=self.SubCatClothing)
            self.ComboSubCatergory.current(0)
        elif self.Combo_Catergory.get() == "Electronic":
            self.ComboSubCatergory.config(value=self.Sub_Elect)
            self.ComboSubCatergory.current(0)
        elif self.Combo_Catergory.get() == "Grocery":
            self.ComboSubCatergory.config(value=self.Sub_Grocery)
            self.ComboSubCatergory.current(0)
        elif self.Combo_Catergory.get() == "Mobiles":
            self.ComboSubCatergory.config(value=self.Sub_Mobile)
            self.ComboSubCatergory.current(0)

    def Product_add(self, event=""):
        if self.ComboSubCatergory.get() == "Pant":
            self.lblCombo_Catergory.config(value=self.pant)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "T-Shirt":
            self.lblCombo_Catergory.config(value=self.Tshirt)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Shirt":
            self.lblCombo_Catergory.config(value=self.Shirt)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Cargo":
            self.lblCombo_Catergory.config(value=self.cargo)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Shoes":
            self.lblCombo_Catergory.config(value=self.shoes)
            self.lblCombo_Catergory.current(0)

        if self.ComboSubCatergory.get() == "Laptop":
            self.lblCombo_Catergory.config(value=self.Laptop)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Bluetooth":
            self.lblCombo_Catergory.config(value=self.Bluetooth)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "TV":
            self.lblCombo_Catergory.config(value=self.TV)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Powerbank":
            self.lblCombo_Catergory.config(value=self.power)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Tablet":
            self.lblCombo_Catergory.config(value=self.Tablet)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Biscuits":
            self.lblCombo_Catergory.config(value=self.Biscuits)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Shampo":
            self.lblCombo_Catergory.config(value=self.Shampo)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Sugar":
            self.lblCombo_Catergory.config(value=self.Sugar)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Pasta":
            self.lblCombo_Catergory.config(value=self.Pasta)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Oil":
            self.lblCombo_Catergory.config(value=self.oil)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Samsung":
            self.lblCombo_Catergory.config(value=self.mob_samsung)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Redmi":
            self.lblCombo_Catergory.config(value=self.mob_Redmi)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Apple":
            self.lblCombo_Catergory.config(value=self.mob_Apple)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Fan":
            self.lblCombo_Catergory.config(value=self.fan)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Refregerator":
            self.lblCombo_Catergory.config(value=self.refre)
            self.lblCombo_Catergory.current(0)
        elif self.ComboSubCatergory.get() == "Light":
            self.lblCombo_Catergory.config(value=self.light)
            self.lblCombo_Catergory.current(0)

    def CPrice(self, event=""):
        # Pant
        if self.lblCombo_Catergory.get() == "Levis":
            self.Price_Cat.config(value=self.price_levis)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Puma":
            self.Price_Cat.config(value=self.puma)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Nike":
            self.Price_Cat.config(value=self.Nike)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Addidas":
            self.Price_Cat.config(value=self.addidas)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Gucci":
            self.Price_Cat.config(value=self.price_Gucci)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # T-shirt
        if self.lblCombo_Catergory.get() == "Spykar":
            self.Price_Cat.config(value=self.spykar)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Lookout":
            self.Price_Cat.config(value=self.lookout)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Mufti":
            self.Price_Cat.config(value=self.Mufti)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Peter England":
            self.Price_Cat.config(value=self.peter)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Shirt
        if self.lblCombo_Catergory.get() == "Levis":
            self.Price_Cat.config(value=self.shirt_levis)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Gucci":
            self.Price_Cat.config(value=self.shirt_Gucci)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Puma":
            self.Price_Cat.config(value=self.shirt_puma)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Nike":
            self.Price_Cat.config(value=self.shirt_Nike)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Addidas":
            self.Price_Cat.config(value=self.shirt_Nike)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Mufti":
            self.Price_Cat.config(value=self.shirt_mufti)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Peter England":
            self.Price_Cat.config(value=self.shirt_peter)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)

        # cargo
        if self.lblCombo_Catergory.get() == "Dennis Lingo":
            self.Price_Cat.config(value=self.Dennis_Lingo)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "HIGHLANDER":
            self.Price_Cat.config(value=self.Highlander)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "KILLER":
            self.Price_Cat.config(value=self.Killer)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Snitch":
            self.Price_Cat.config(value=self.Sntch)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Spykar":
            self.Price_Cat.config(value=self.cargo_spykar)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Shoes
        if self.lblCombo_Catergory.get() == "Woodland":
            self.Price_Cat.config(value=self.woodland)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Sparx":
            self.Price_Cat.config(value=self.sparx)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Addidas":
            self.Price_Cat.config(value=self.shoes_puma)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Puma":
            self.Price_Cat.config(value=self.shoes_Addidas)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Nike":
            self.Price_Cat.config(value=self.shoes_nike)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Laptop
        if self.lblCombo_Catergory.get() == "Acer":
            self.Price_Cat.config(value=self.Acer)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Dell":
            self.Price_Cat.config(value=self.Dell)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Asus":
            self.Price_Cat.config(value=self.Asus)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Hp":
            self.Price_Cat.config(value=self.Hp)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Apple":
            self.Price_Cat.config(value=self.Apple)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Lenovo":
            self.Price_Cat.config(value=self.Lenovo)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        if self.lblCombo_Catergory.get() == "Boat":
            self.Price_Cat.config(value=self.Boat)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Kdm":
            self.Price_Cat.config(value=self.Kdm)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Apple":
            self.Price_Cat.config(value=self.Blue_Apple)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "OnePlus":
            self.Price_Cat.config(value=self.oneplus)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Sony":
            self.Price_Cat.config(value=self.sony)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)

        #    TV
        if self.lblCombo_Catergory.get() == "Sony":
            self.Price_Cat.config(value=self.Sony)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "LG":
            self.Price_Cat.config(value=self.Lg)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Vediocon":
            self.Price_Cat.config(value=self.Vedio)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Samsung":
            self.Price_Cat.config(value=self.Samsung)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "SanSui":
            self.Price_Cat.config(value=self.Sansui)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
            # Power Bank
        self.power = [
            "Select Option",
            "Oneplus",
            "Apple",
            "Redmi",
            "Kdm",
        ]
        self.power_oneplus = 2000
        self.power_apple = 5000
        self.power_redmi = 1500
        self.power_kdm = 2500
        # Power Bank
        if self.lblCombo_Catergory.get() == "Oneplus":
            self.Price_Cat.config(value=self.power_oneplus)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Apple":
            self.Price_Cat.config(value=self.power_apple)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Redmi":
            self.Price_Cat.config(value=self.power_redmi)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Kdm":
            self.Price_Cat.config(value=self.power_kdm)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        if self.lblCombo_Catergory.get() == "Oneplus":
            self.Price_Cat.config(value=self.tablets_oneplus)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Apple":
            self.Price_Cat.config(value=self.tablets_apple)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Realme":
            self.Price_Cat.config(value=self.tablets_realme)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Sony":
            self.Price_Cat.config(value=self.tablets_Sony)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Lenovo":
            self.Price_Cat.config(value=self.tablets_lenovo)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)

        # Biscuits
        if self.lblCombo_Catergory.get() == "Mari gold":
            self.Price_Cat.config(value=self.Bis_Mari)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Parle":
            self.Price_Cat.config(value=self.Bis_parle)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Jim Jam":
            self.Price_Cat.config(value=self.Bis_Jim)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Happy Happy":
            self.Price_Cat.config(value=self.Bis_Happy)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Shampo
        if self.lblCombo_Catergory.get() == "Dove":
            self.Price_Cat.config(value=self.sham_Dove)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Cleanic Plus":
            self.Price_Cat.config(value=self.sham_cleanic)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Sunsulk":
            self.Price_Cat.config(value=self.sham_sun)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Lux":
            self.Price_Cat.config(value=self.sham_lux)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Sugar
        if self.lblCombo_Catergory.get() == "Thin Sugar":
            self.Price_Cat.config(value=self.sugar_thin)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Fat Sugar":
            self.Price_Cat.config(value=self.sugar_fat)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Pasta
        if self.lblCombo_Catergory.get() == "Small pasta":
            self.Price_Cat.config(value=self.pas_small)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Medium Pasta":
            self.Price_Cat.config(value=self.pas_medium)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # oil
        if self.lblCombo_Catergory.get() == "Sunflow":
            self.Price_Cat.config(value=self.oil_sunflow)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Priya":
            self.Price_Cat.config(value=self.oil_priya)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Coconut oil":
            self.Price_Cat.config(value=self.oil_coco)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Peanut oil":
            self.Price_Cat.config(value=self.oil_Peanut)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Mobile Samsung
        if self.lblCombo_Catergory.get() == "S21":
            self.Price_Cat.config(value=self.mob_sam21)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "S24":
            self.Price_Cat.config(value=self.mob_sam24)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "S24 ultra":
            self.Price_Cat.config(value=self.mob_sam_ultra)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Samsung Folded":
            self.Price_Cat.config(value=self.mob_sam_fold)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        # Redmi
        if self.lblCombo_Catergory.get() == "redmi note 10":
            self.Price_Cat.config(value=self.mob_red10)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "redmi note 11":
            self.Price_Cat.config(value=self.mob_red11)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "redmi note 12":
            self.Price_Cat.config(value=self.mob_red12)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "redmi series 13":
            self.Price_Cat.config(value=self.mob_red13)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "redmi 13T 5G":
            self.Price_Cat.config(value=self.mob_red13T)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        self.mob_Apple = [
            "Select Option",
            "Iphone-12",
            "Iphone-13",
            "Iphone-14",
            "Iphone-15",
            "Iphone-15 pro",
        ]
        self.apple_12 = (40000,)
        self.apple_13 = (60000,)
        self.apple_14 = (70000,)
        self.apple_15 = (90000,)
        self.apple_15pro = (120000,)
        if self.lblCombo_Catergory.get() == "Iphone-12":
            self.Price_Cat.config(value=self.apple_12)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Iphone-13":
            self.Price_Cat.config(value=self.apple_13)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Iphone-14":
            self.Price_Cat.config(value=self.apple_14)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Iphone-15":
            self.Price_Cat.config(value=self.apple_15)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)
        elif self.lblCombo_Catergory.get() == "Iphone-15 pro":
            self.Price_Cat.config(value=self.apple_15pro)
            self.Price_Cat.current(0)
            self.c_quantity.set(1)


if __name__ == "__main__":
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
