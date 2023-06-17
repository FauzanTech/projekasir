import customtkinter

# Ekstra Kredit
# Kami menerapkan program ini tidak hanya dengan struktur data yang efisien untuk toko andi
# tapi juga dengan menggunakan tampilan yang lebih modern 
# Kami menggunakan modul customtkinter untuk mengubah tampilan program ini agar lebih dinamis dan modern
# Kami menggunakan window yang bertema gelap dan widget dengan warna default biru tua
# Kami menggunakan beberapa widget seperti: Entry, Button, Tab, Label, Textbox
# Kami juga memasang ikon pada window ini


# Agar Program ini berjalan dengan baik
# Ada beberapa syarat yang harus dipenuhi yaitu:
# 1. Menginstall customtkinter pada device anda
# 2. Mendownload file yang kami sediakan yaitu store.ico
# 3. Agar tampilannya lebih baik kami sarankan untuk mendowload font Roboto


# Struktur Data 
# Hash, Queue, dan Tree

# Struktur Data Hash

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    def add_product(self, name, price, stock, code):
        index = self._hash_function(code)
        self.table[index].append({"name": name, "price": price, "stock": stock, "code": code})

    def find_product(self, code):
        index = self._hash_function(code)
        for product in self.table[index]:
            if product["code"] == code:
                return product
        return None

    def update_stock(self, code, new_stock):
        product = self.find_product(code)
        if product:
            product["stock"] = new_stock
        else:
            print("Product not found.")

    def update_price(self, code, new_price):
        product = self.find_product(code)
        if product:
            product["price"] = new_price
        else:
            print("Product not found.")

# Contoh penggunaan Hashing untuk menyimpan produk

product_hash_table = HashTable(10)
product_hash_table.add_product("Biskuit", 7000, 30, "A001")
product_hash_table.add_product("Mie Instan", 3000, 30, "B002")
product_hash_table.add_product("Cocacola", 5000, 30, "C003")
product_hash_table.add_product("Wafer", 5000, 30, "D004")
product_hash_table.add_product("Air Mineral", 4000, 30, "E005")
product_hash_table.add_product("Sprite", 5000, 30, "F006")
product_hash_table.add_product("Cokelat", 3000, 30, "G007")
product_hash_table.add_product("Kue", 2000, 30, "H008")
product_hash_table.add_product("Kerupuk", 2000, 30, "I009")
product_hash_table.add_product("Permen", 500, 30, "J010")


# Struktur Data Queue

class TransactionQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, transaction):
        self.queue.append(transaction)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

# Contoh penggunaan Queue untuk mengantri transaksi
transaction_queue = TransactionQueue()


# Struktur Data Tree

class ProductNode:
    def __init__(self, kategori, name=None, price=None, stock=None, code=None):
        self.kategori = kategori
        self.name = name
        self.price = price
        self.stock = stock
        self.code = code
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class ProductTree:
    def __init__(self, root):
        self.root = root

    def find_product(self, kategori):
        return self._find_product_recursive(self.root, kategori)

    def _find_product_recursive(self, current_node, kategori):
        if current_node.kategori == kategori:
            return current_node
        for child in current_node.children:
            found_product = self._find_product_recursive(child, kategori)
            if found_product:
                return found_product
        return None
    
    def update_stock(self, kategori, name, new_stock):
        productKategori = self.find_product(kategori)

        for child in productKategori.children:
            if child.name == name:
                product = child
                product.stock = new_stock

    def update_price(self, kategori, name, new_price):
        productKategori = self.find_product(kategori)

        for child in productKategori.children:
                if child.name == name:
                        product = child
                        product.price = new_price



# Contoh penggunaan Tree untuk mencari produk
# Pembuatan Kategori Produk
product_A = ProductNode("Makanan")

# Pembuatan Subkategori Produk
sub1_A = ProductNode("Makanan Berat")
sub2_A = ProductNode("Makanan Ringan")

product_A.add_child(sub1_A)
product_A.add_child(sub2_A)

sub1_A.add_child(ProductNode("Makanan Berat","Cokelat", 3000, 20, "G007"))
sub1_A.add_child(ProductNode("Makanan Berat","Kue", 1000, 10, "H008"))

sub2_A.add_child(ProductNode("Makanan Ringan", "Kerupuk", 1000, 30, "I009"))
sub2_A.add_child(ProductNode("Makanan Ringan", "Permen", 500, 100, "J010"))

# Pembuatan Tree
product_tree = ProductTree(product_A)



# Membuat Window dan Mengatur Tema, Title, dan Icon Window
app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app.title("Toko Andi")
app.iconbitmap("store.ico")

# Memposisikan Window agar ditengah layar

lebar = 900
tinggi = 720

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = int((screenWidth/2) - (lebar/2)+100)
y = int((screenHeight/2) - (tinggi/2)+100)

app.geometry(f"{lebar}x{tinggi}+{x}+{y}")


# Fungsi yang berdasarkan struktur data Hash
# Jika melakukan pengambilan data entry, program akan melakukan try 
# and exception untuk mencegah terjadinya error

def cari_kode():

    try:
        textbox.configure(state="normal") 
        textbox.delete("0.0", "end")
        kode = entry.get()
        produk = product_hash_table.find_product(kode)
        if produk:
                info = f"""
Kode Produk: {produk["code"]},
Nama Produk: {produk["name"]},
Harga: {produk["price"]},
Stok: {produk["stock"]},
"""
        textbox.insert("0.0", info)
        textbox.configure(state="disabled")

        label3.configure(text="")
        label5.configure(text="")
    except:
            print("Terjadi Error, Mungkin salah memasukkan kode ?")

def update_harga():
                
    try:
        str_entry = entry2.get()
        if str_entry: 
            entry2.delete(0,"end")
            list_entry = str_entry.split(",")
            product_hash_table.update_price(list_entry[0], list_entry[1])

            label3.configure(text="Berhasil Memperbarui Harga !")
        else:
            label3.configure(text="Silahkan diisi !")
    except:
        print("Terjadi Error, Mungkin salah memasukkan kode ?")

def update_stok():

    try:
        str_entry = entry3.get()
        if str_entry: 
            entry3.delete(0,"end")
            list_entry = str_entry.split(",")
            product_hash_table.update_stock(list_entry[0], list_entry[1])

            label5.configure(text="Berhasil Memperbarui Stok !")
        else:
            label5.configure(text="Silahkan diisi !")
    except:
        print("Terjadi Error, Mungkin salah memasukkan kode ?")

# Fungsi yang berdasarkan pada struktur data tree
def cari_kategori():

    try:
        textbox2.configure(state="normal") 
        textbox2.delete("0.0", "end")
        kategori = entry4.get()
        
        found_product = product_tree.find_product(kategori)
        if found_product:
                product = found_product.children
                for child in product:
                        info2 = f"""
Kategori: {child.kategori},
Nama Produk: {child.name},
Harga: {child.price},
Stok: {child.stock},
Kode Produk: {child.code}                       
"""
                        textbox2.insert("end", info2)
                textbox2.configure(state="disabled")
        
        label7.configure(text="")
        label9.configure(text="")
    except:
        print("Terjadi Error, Mungkin salah memasukkan kategori ?")

def update_harga_():

    try:
        str_entry = entry5.get()
        if str_entry: 
                entry5.delete(0,"end")
                list_entry = str_entry.split(",")
                product_tree.update_price(list_entry[0], list_entry[1], list_entry[2])

                label7.configure(text="Berhasil Memperbarui Harga !")
        else:
                label7.configure(text="Silahkan diisi !")
    except:
        print("Terjadi Error, Mungkin salah memasukkan kategori ?")

def update_stok_():

    try:
        str_entry = entry6.get()
        if str_entry: 
                entry6.delete(0,"end")
                list_entry = str_entry.split(",")
                product_tree.update_stock(list_entry[0], list_entry[1], list_entry[2])

                label9.configure(text="Berhasil Memperbarui Stok !")
        else:
                label9.configure(text="Silahkan diisi !")
    except:
        print("Terjadi Error, Mungkin salah memasukkan kategori ?")

# Fungsi Untuk mengelolah antrian
def tambah_antrian():

    transaction_queue.enqueue(f"Transaksi Id: {len(transaction_queue.queue)+1}")
    label10.configure(text=transaction_queue.queue)
        
def hapus_antrian():

    transaction_queue.dequeue()
    label10.configure(text=transaction_queue.queue)

    if len(transaction_queue.queue) == 0:
            label10.configure(text="Antrian Kosong")

# App

# Pembuatan Widget

label = customtkinter.CTkLabel(app, text="Toko Andi", fg_color="transparent", font=("Roboto", 25), anchor="w", text_color="white")
tabview = customtkinter.CTkTabview(master=app)
tabview.add("Tab 1")  
tabview.add("Tab 2")  
tabview.set("Tab 1")  

# Peletakan Widget

label.grid(row=0, column=0, sticky="we", pady=20, padx=20)
tabview.grid(row=1, column=0, padx=20, pady=(20,0))


# Widget Tab 1

# Pembuatan Widget

entry = customtkinter.CTkEntry(master=tabview.tab("Tab 1"), placeholder_text="Kode Produk", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16))
button = customtkinter.CTkButton(master=tabview.tab("Tab 1"), text="Cari", height=30, command=cari_kode, width=20)
textbox = customtkinter.CTkTextbox(master=tabview.tab("Tab 1"), font=("Roboto", 15), text_color="white", state="disabled")
label2 = customtkinter.CTkLabel(master=tabview.tab("Tab 1"), text="Perbarui Harga", fg_color="transparent", font=("Roboto", 17), text_color="white")
entry2 = customtkinter.CTkEntry(master=tabview.tab("Tab 1"), placeholder_text="KodeProduk,HargaBaru", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16), width=200)
button2 = customtkinter.CTkButton(master=tabview.tab("Tab 1"), text="Update", height=30, command=update_harga, width=60)
label3 = customtkinter.CTkLabel(master=tabview.tab("Tab 1"), text="", fg_color="transparent", font=("Roboto", 15), text_color="white")
label4 = customtkinter.CTkLabel(master=tabview.tab("Tab 1"), text="Perbarui Stok", fg_color="transparent", font=("Roboto", 17), text_color="white")
entry3 = customtkinter.CTkEntry(master=tabview.tab("Tab 1"), placeholder_text="KodeProduk,StokBaru", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16), width=200)
button3 = customtkinter.CTkButton(master=tabview.tab("Tab 1"), text="Update", height=30, command=update_stok, width=60)
label5 = customtkinter.CTkLabel(master=tabview.tab("Tab 1"), text="", fg_color="transparent", font=("Roboto", 15), text_color="white")

# Peletakan Widget

entry.grid(row=1, column=0)
button.grid(row=1, column=1)
textbox.grid(row=2, column=0, pady=20, padx=20)
label2.grid(row=3, column=0, columnspan=2, pady=(10,0))
entry2.grid(row=4, column=0)
button2.grid(row=4, column=1)
label3.grid(row=5, column=0, columnspan=2)
label4.grid(row=6, column=0, columnspan=2, pady=(10,0))
entry3.grid(row=7, column=0)
button3.grid(row=7, column=1)
label5.grid(row=8, column=0, columnspan=2)  



# Widget Tab 2

# Pembuatan Widget

entry4 = customtkinter.CTkEntry(master=tabview.tab("Tab 2"), placeholder_text="Kategori Produk", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16))
button4 = customtkinter.CTkButton(master=tabview.tab("Tab 2"), text="Cari", height=30, command=cari_kategori, width=40)
textbox2 = customtkinter.CTkTextbox(master=tabview.tab("Tab 2"), font=("Roboto", 15), text_color="white", state="disabled")
label6 = customtkinter.CTkLabel(master=tabview.tab("Tab 2"), text="Perbarui Harga", fg_color="transparent", font=("Roboto", 17), text_color="white")
entry5 = customtkinter.CTkEntry(master=tabview.tab("Tab 2"), placeholder_text="Kategori,Nama,HargaBaru", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16), width=200)
button5 = customtkinter.CTkButton(master=tabview.tab("Tab 2"), text="Update", height=30, command=update_harga_, width=60)
label7 = customtkinter.CTkLabel(master=tabview.tab("Tab 2"), text="", fg_color="transparent", font=("Roboto", 15), text_color="white")
label8 = customtkinter.CTkLabel(master=tabview.tab("Tab 2"), text="Perbarui Stok", fg_color="transparent", font=("Roboto", 17), text_color="white")
entry6 = customtkinter.CTkEntry(master=tabview.tab("Tab 2"), placeholder_text="Kategori,Nama,StokBaru", corner_radius=5, border_width=1, border_color="grey", text_color="white", height=30, font=("Roboto",16), width=200)
button6 = customtkinter.CTkButton(master=tabview.tab("Tab 2"), text="Update", height=30, command=update_stok_, width=60)
label9 = customtkinter.CTkLabel(master=tabview.tab("Tab 2"), text="", fg_color="transparent", font=("Roboto", 15), text_color="white")

# Peletakan Widget

entry4.grid(row=1, column=0)
button4.grid(row=1, column=1)
textbox2.grid(row=2, column=0, pady=20, padx=20)
label6.grid(row=3, column=0, columnspan=2, pady=(10,0))
entry5.grid(row=4, column=0)
button5.grid(row=4, column=1)
label7.grid(row=5, column=0, columnspan=2,pady=5)
label8.grid(row=6, column=0, columnspan=2, pady=(10,0))
entry6.grid(row=7, column=0)
button6.grid(row=7, column=1)
label9.grid(row=8, column=0, columnspan=2)


# Mengelola Transaksi

# Pembuatan Widget

label10 = customtkinter.CTkLabel(app, text="Antrian Kosong", fg_color="transparent", font=("Roboto", 14), anchor="w", text_color="white")
label11 = customtkinter.CTkLabel(app, text="Tambah Antrian", fg_color="transparent", font=("Roboto", 17), text_color="white")
label12 = customtkinter.CTkLabel(app, text="Keluarkan Antrian", fg_color="transparent", font=("Roboto", 17), text_color="white")
button7 = customtkinter.CTkButton(app, text="Tambah", height=30, command=tambah_antrian, width=30)
button8 = customtkinter.CTkButton(app, text="Hapus", height=30, command=hapus_antrian, width=30)

# Peletakan Widget

label10.grid(row=1, column=2, columnspan=2, padx=20)
label11.grid(row=9, column=0, padx=20, pady=(10,0))
label12.grid(row=9, column=1, padx=20, pady=(10,0))
button7.grid(row=10, column=0, pady=(20,0))
button8.grid(row=10, column=1, pady=(20,0))


app.mainloop()




