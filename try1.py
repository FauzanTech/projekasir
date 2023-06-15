db = {
"Mie instan" : "4000", 
"Minyak goreng /Liter" : "28000",
"Tepung terigu /Kg" : "17000",
"Sabun mandi batang" : "5000",
"Shampo Sachet" : "1000",
"Deterjen Sachet": "6000",
"Pasta Gigi" : "10000",
"Sikat Gigi" : "4000",
"Beras /Kg" : "10000",
"Telur" : "2000",
"Sirup" : "12000",
"Gula pasir /Kg" : "10000",
"Teh Sachet" : "5000",
"Kopi Sachet" : "3000",
"SKM" : "7000",
"Mentega" : "8000",
"Sabun cuci piring" : "12000",
"Kecap" : "10000",
"Sambal" : "10000",
"Air mineral 600ml" : "4000"
}

db2 = [
    [],
]

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

    def update_name(self, code, new_name):
        product = self.find_product(code)
        if product:
            product["name"] = new_name
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
product_hash_table.add_product("Makanan A", 10, 50, "A001")
product_hash_table.add_product("Makanan B", 20, 30, "B002")
product_hash_table.add_product("Minuman A", 5, 100, "C003")


# Mencari dan memperbarui stok produk
product_A = product_hash_table.find_product("A001")
print(product_A)
if product_A:
    print("Product found:", product_A["name"])
    product_hash_table.update_stock("A001", 40)
else:
    print("Product not found.")


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
transaction_queue.enqueue("Transaction A")
transaction_queue.enqueue("Transaction B")
transaction_queue.enqueue("Transaction C")

# Memproses transaksi yang masuk pertama
current_transaction = transaction_queue.dequeue()
if current_transaction:
    print("Processing transaction:", current_transaction)
else:
    print("No transaction to process.")

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
    
    def update_stock(self, kategori, name, stock):
        productKategori = self.find_product(kategori)

        for child in productKategori.children:
            if child.name == name:
                product = child
                product.stock = stock

    def update_price(self, kategori, name, price):
        productKategori = self.find_product(kategori)

        for child in productKategori.children:
            if child.name == name:
                product = child
                product.price = price



# Contoh penggunaan Tree untuk mencari produk
product_A = ProductNode("Makanan")
product_B = ProductNode("Makanan B", 20, 30, "B002")
product_C = ProductNode("Minuman A", 5, 100, "C003")

sub1_A = ProductNode("Makanan Berat")
sub2_A = ProductNode("Makanan Ringan")

product_A.add_child(sub1_A)
product_A.add_child(sub2_A)

sub1_A.add_child(ProductNode("Makanan Berat","Cokelat", 15, 20, "D004"))
sub1_A.add_child(ProductNode("Makanan Berat","Kue", 10, 10, "E005"))

product_tree = ProductTree(product_A)

# found_product = product_tree.find_product("Makanan Berat")
# print(found_product.kategori)
# if found_product:
#     product = found_product.children
#     for i in product:
#         print(f"Nama Product: {i.name}, Harga: {i.price}, Stock:{i.stock}")

# else:
#     print("Product not found.")
# print()

# product_tree.update_stock("Makanan Berat", "Cokelat", 15)
# product_tree.update_price("Makanan Berat", "Cokelat", 100)
# for i in sub1_A.children:
#     print(f"Nama Product: {i.name}, Harga: {i.price}, Stock:{i.stock}")