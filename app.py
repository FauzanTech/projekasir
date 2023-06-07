from tkinter import *
import customtkinter
import project

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app.title("Sahrul Cell")
app.geometry("1200x800+100+100")

app.columnconfigure(0,weight=1)
app.columnconfigure(1,weight=1)
app.columnconfigure(2,weight=1)
app.columnconfigure(3,weight=1)


app.rowconfigure(0,weight=1)
app.rowconfigure(1,weight=1)
app.rowconfigure(2,weight=1)
app.rowconfigure(3,weight=1)
app.rowconfigure(4,weight=1)
app.rowconfigure(5,weight=1)
app.rowconfigure(6,weight=1)
app.rowconfigure(7,weight=1)
app.rowconfigure(8,weight=1)
app.rowconfigure(9,weight=1)
app.rowconfigure(10,weight=1)
app.rowconfigure(11,weight=1)
app.rowconfigure(12,weight=1)
app.rowconfigure(13,weight=1)
app.rowconfigure(14,weight=1)

l1 = customtkinter.CTkLabel(app, text="--> SAHRUL CELL ", fg_color="transparent",font=("Roboto",40), anchor="w" , text_color="white")
l1.grid(columnspan=4, row=0, pady=20, padx=20, sticky="wens")

# Kiri
l2 = customtkinter.CTkLabel(app, text="Sabun Mandi Rp.5.000/batang", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l2.grid(row=1, column=0, pady=15, padx=(60,0), sticky="we")

e1 = customtkinter.CTkEntry(app, width=50)
e1.grid(row=1, column=1, padx=(0,0))

l3 = customtkinter.CTkLabel(app, text="Shampo Rp.1.000/Sachet", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l3.grid(row=2, column=0, pady=15, padx=(60,0), sticky="we")

e2 = customtkinter.CTkEntry(app, width=50)
e2.grid(row=2, column=1)

l4 = customtkinter.CTkLabel(app, text="Deterjen Rp.6.000/Sachet", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l4.grid(row=3, column=0, pady=15, padx=(60,0), sticky="we")

e3 = customtkinter.CTkEntry(app, width=50)
e3.grid(row=3, column=1)

l5 = customtkinter.CTkLabel(app, text="Pasta Gigi Rp.10.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l5.grid(row=4, column=0, pady=15, padx=(60,0), sticky="we")

e4 = customtkinter.CTkEntry(app, width=50)
e4.grid(row=4, column=1)

l6 = customtkinter.CTkLabel(app, text="Sikat Gigi Rp.4.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l6.grid(row=5, column=0, pady=15, padx=(60,0), sticky="we")

e5 = customtkinter.CTkEntry(app, width=50)
e5.grid(row=5, column=1)

l7 = customtkinter.CTkLabel(app, text="Sabun cuci piring Rp.12.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l7.grid(row=6, column=0, pady=15, padx=(60,0), sticky="we")

e6 = customtkinter.CTkEntry(app, width=50)
e6.grid(row=6, column=1)

l8 = customtkinter.CTkLabel(app, text="Mie instan Rp.4.000/bungkus", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l8.grid(row=7, column=0, pady=15, padx=(60,0), sticky="we")

e7 = customtkinter.CTkEntry(app, width=50)
e7.grid(row=7, column=1)

l9 = customtkinter.CTkLabel(app, text="Minyak goreng Rp.28.000/Liter", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l9.grid(row=8, column=0, pady=15, padx=(60,0), sticky="we")

e8 = customtkinter.CTkEntry(app, width=50)
e8.grid(row=8, column=1)

l10 = customtkinter.CTkLabel(app, text="Air mineral 600ml Rp.4.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l10.grid(row=9, column=0, pady=15, padx=(60,0), sticky="we")

e9 = customtkinter.CTkEntry(app, width=50)
e9.grid(row=9, column=1)

l11 = customtkinter.CTkLabel(app, text="Beras Rp.10.000/Kg", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l11.grid(row=10, column=0, pady=15, padx=(60,0), sticky="we")

e10 = customtkinter.CTkEntry(app, width=50)
e10.grid(row=10, column=1)

# Kanan

l12 = customtkinter.CTkLabel(app, text="Telur Rp.2.000/butir", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l12.grid(row=1, column=3, pady=15, sticky="we")

e11 = customtkinter.CTkEntry(app, width=50)
e11.grid(row=1, column=4, padx=(0,100))

l13 = customtkinter.CTkLabel(app, text="Sirup Rp.12.000/botol", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l13.grid(row=2, column=3, pady=15, sticky="we")

e12 = customtkinter.CTkEntry(app, width=50)
e12.grid(row=2, column=4, padx=(0,100))

l14 = customtkinter.CTkLabel(app, text="Gula pasir Rp.10.000/kg", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l14.grid(row=3, column=3, pady=15, sticky="we")

e13 = customtkinter.CTkEntry(app, width=50)
e13.grid(row=3, column=4, padx=(0,100))

l15 = customtkinter.CTkLabel(app, text="Teh Sachet Rp.5.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l15.grid(row=4, column=3, pady=15, sticky="we")

e14 = customtkinter.CTkEntry(app, width=50)
e14.grid(row=4, column=4, padx=(0,100))

l16 = customtkinter.CTkLabel(app, text="Kopi Sachet Rp.3.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l16.grid(row=5, column=3, pady=15, sticky="we")

e15 = customtkinter.CTkEntry(app, width=50)
e15.grid(row=5, column=4, padx=(0,100))

l17 = customtkinter.CTkLabel(app, text="Susu Kental Manis Rp.7.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l17.grid(row=6, column=3, pady=15, sticky="we")

e16 = customtkinter.CTkEntry(app, width=50)
e16.grid(row=6, column=4, padx=(0,100))

l18 = customtkinter.CTkLabel(app, text="Mentega Rp.8.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l18.grid(row=7, column=3, pady=15, sticky="we")

e17 = customtkinter.CTkEntry(app, width=50)
e17.grid(row=7, column=4, padx=(0,100))

l19 = customtkinter.CTkLabel(app, text="Tepung terigu Rp.17.000/Kg", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l19.grid(row=8, column=3, pady=15, sticky="we")

e18 = customtkinter.CTkEntry(app, width=50)
e18.grid(row=8, column=4, padx=(0,100))

l20 = customtkinter.CTkLabel(app, text="Kecap Rp.10.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l20.grid(row=9, column=3, pady=15, sticky="we")

e19 = customtkinter.CTkEntry(app, width=50)
e19.grid(row=9, column=4, padx=(0,100))

l21 = customtkinter.CTkLabel(app, text="Sambal Rp.10.000", fg_color="transparent",font=("Roboto",20), anchor="w", text_color="white")
l21.grid(row=10, column=3, pady=15, sticky="we")

e20 = customtkinter.CTkEntry(app, width=50)
e20.grid(row=10, column=4, padx=(0,100))

def total():
    jumlah = []
    try:
        jml_e1 = int(e1.get())*int(project.db["Sabun mandi batang"]) if e1.get() else 0
        jml_e2 = int(e2.get())*int(project.db["Shampo Sachet"]) if e2.get() else 0
        jml_e3 = int(e3.get())*int(project.db["Deterjen Sachet"]) if e3.get() else 0
        jml_e4 = int(e4.get())*int(project.db["Pasta Gigi"]) if e4.get() else 0
        jml_e5 = int(e5.get())*int(project.db["Sikat Gigi"]) if e5.get() else 0
        jml_e6 = int(e6.get())*int(project.db["Sabun cuci piring"]) if e6.get() else 0
        jml_e7 = int(e7.get())*int(project.db["Mie instan"]) if e7.get() else 0
        jml_e8 = int(e8.get())*int(project.db["Minyak goreng /Liter"]) if e8.get() else 0
        jml_e9 = int(e9.get())*int(project.db["Air mineral 600ml"]) if e9.get() else 0
        jml_e10 = int(e10.get())*int(project.db["Beras /Kg"]) if e10.get() else 0
        jml_e11 = int(e11.get())*int(project.db["Telur"]) if e11.get() else 0
        jml_e12 = int(e12.get())*int(project.db["Sirup"]) if e12.get() else 0
        jml_e13 = int(e13.get())*int(project.db["Gula pasir /Kg"]) if e13.get() else 0
        jml_e14 = int(e14.get())*int(project.db["Teh Sachet"]) if e14.get() else 0
        jml_e15 = int(e15.get())*int(project.db["Kopi Sachet"]) if e15.get() else 0
        jml_e16 = int(e16.get())*int(project.db["SKM"]) if e16.get() else 0
        jml_e17 = int(e17.get())*int(project.db["Mentega"]) if e17.get() else 0
        jml_e18 = int(e18.get())*int(project.db["Tepung terigu /Kg"]) if e18.get() else 0
        jml_e19 = int(e19.get())*int(project.db["Kecap"]) if e19.get() else 0
        jml_e20 = int(e20.get())*int(project.db["Sambal"]) if e20.get() else 0

        jumlah.append(jml_e1)
        jumlah.append(jml_e2)
        jumlah.append(jml_e3)
        jumlah.append(jml_e4)
        jumlah.append(jml_e5)
        jumlah.append(jml_e6)
        jumlah.append(jml_e7)
        jumlah.append(jml_e8)
        jumlah.append(jml_e9)
        jumlah.append(jml_e10)
        jumlah.append(jml_e11)
        jumlah.append(jml_e12)
        jumlah.append(jml_e13)
        jumlah.append(jml_e14)
        jumlah.append(jml_e15)
        jumlah.append(jml_e16)
        jumlah.append(jml_e17)
        jumlah.append(jml_e18)
        jumlah.append(jml_e19)
        jumlah.append(jml_e20)
        global jumlah_belanja
        jumlah_belanja = sum(jumlah)
    except:
        print("Masukkan angka yang benar!")

    l22.configure(text=f"Total belanja : Rp.{jumlah_belanja},-")
    l23.configure(text="Uang Tunai Rp.")
    global e21
    e21 = customtkinter.CTkEntry(app, width=100, font=("Roboto",17))
    e21.grid(row=14, column=2, sticky="w")

    b5 = customtkinter.CTkButton(app, text="Bayar", command=transaksi, font=("Roboto",20), width=100, height=37, anchor="center")
    b5.grid(row=14, column=3, sticky="w")

def transaksi():
    l24.configure(text="")
    l25.configure(text="")
    try:
        uang_tunai = int(e21.get())
    except:
        print("Masukkan angka yang benar !")

    if uang_tunai < jumlah_belanja:
        l24.configure(text="Maaf, uang anda tidak cukup !")

    elif uang_tunai > jumlah_belanja:
        l24.configure(text="Pembayaran Berhasil !..")
        kembalian = uang_tunai - jumlah_belanja
        l25.configure(text=f"Kembalian anda Rp.{kembalian},-")

    elif uang_tunai == jumlah_belanja:
        l24.configure(text="Pembayaran Berhasil !..")

b1 = customtkinter.CTkButton(app, text="Reset", command=total, font=("Roboto",20), width=100, anchor="w")
b1.grid(row=13, column=0, pady=(30,0), sticky="w", padx=60)

b2 = customtkinter.CTkButton(app, text="Statistik", command=total, font=("Roboto",20), width=100, height=40, anchor="w")
b2.grid(row=14, column=0, pady=(15,0), sticky="w", padx=60)

b3 = customtkinter.CTkButton(app, text="Struk Pembayaran", command=total, font=("Roboto",20), width=100, height=40, anchor="w")
b3.grid(row=15, column=0, pady=15, sticky="w", padx=60)

b4 = customtkinter.CTkButton(app, text="Total", command=total, font=("Roboto",20), width=100, height=40)
b4.grid(row=13, column=1, pady=(30,0))

l22 = customtkinter.CTkLabel(app, text="", fg_color="transparent",font=("Roboto",19), anchor="w")
l22.grid(row=13, column=2, pady=(30,0), sticky="we")

l23 = customtkinter.CTkLabel(app, text="", fg_color="transparent",font=("Roboto",19))
l23.grid(row=14, column=1)

l24 = customtkinter.CTkLabel(app, text="", fg_color="transparent",font=("Roboto",19), anchor="w")
l24.grid(row=15, column=1, sticky="we")

l25 = customtkinter.CTkLabel(app, text="", fg_color="transparent",font=("Roboto",19), anchor="w")
l25.grid(row=15, column=2, sticky="we")

app.mainloop()