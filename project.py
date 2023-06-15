import try1
import customtkinter

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app.title("Toko Andi")
app.iconbitmap("store.ico")

lebar = 900
tinggi = 700

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = int((screenWidth/2) - (lebar/2)+100)
y = int((screenHeight/2) - (tinggi/2)+100)

app.geometry(f"{lebar}x{tinggi}+{x}+{y}")

def cari_kode():
    textbox.configure(state="normal") 
    textbox.delete("0.0", "end")
    kode = entry.get()
    entry.delete(0,"end")
    produk = try1.product_hash_table.find_product(kode)
    if produk:
        info = f"""
Nama Produk: {produk["name"]},
Harga: {produk["price"]},
Stok: {produk["stock"]}
"""
        textbox.insert("0.0", info)
        textbox.configure(state="disabled")  # configure textbox to be read-only

entry = customtkinter.CTkEntry(app, placeholder_text="Kode Barang", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16))
entry.grid(row=0, column=0)

button = customtkinter.CTkButton(app, text="Cari", height=30, command=cari_kode)
button.grid(row=0, column=1)

textbox = customtkinter.CTkTextbox(app, font=("Roboto", 15), text_color="white", state="disabled")

# txt = """
# Nama Produk\t: Cokelat
# Harga\t: Rp.5.000
# Stock\t: 20
# """

# textbox.insert("0.0", txt)  # insert at line 0 character 0
# text = textbox.get("0.0", "end")  # get text from line 0 character 0 till the end
# # textbox.delete("0.0", "end")  # delete all text
# configure textbox to be read-only
textbox.grid(row=1, column=0)

app.mainloop()




