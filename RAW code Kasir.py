class Product:
    def __init__(self, name, price, stock, code):
        self.name = name
        self.price = price
        self.stock = stock
        self.code = code
        self.next = None

class ProductList:
    def __init__(self):
        self.head = None

    def add_product(self, name, price, stock, code):
        new_product = Product(name, price, stock, code)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_product

    def find_product(self, code):
        current = self.head
        while current:
            if current.code == code:
                return current
            current = current.next
        return None

    def update_stock(self, code, new_stock):
        product = self.find_product(code)
        if product:
            product.stock = new_stock
        else:
            print("Product not found.")

# Contoh penggunaan Linked List untuk menyimpan produk
product_list = ProductList()
product_list.add_product("Makanan A", 10, 50, "A001")
product_list.add_product("Makanan B", 20, 30, "B002")
product_list.add_product("Minuman A", 5, 100, "C003")

# Mencari dan memperbarui stok produk
product_A = product_list.find_product("A001")
if product_A:
    print("Product found:", product_A.name)
    product_list.update_stock("A001", 40)
else:
    print("Product not found.")

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

# Contoh penggunaan Hashing untuk menyimpan produk
product_hash_table = HashTable(10)
product_hash_table.add_product("Makanan A", 10, 50, "A001")
product_hash_table.add_product("Makanan B", 20, 30, "B002")
product_hash_table.add_product("Minuman A", 5, 100, "C003")

# Mencari dan memperbarui stok produk
product_A = product_hash_table.find_product("A001")
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
    def __init__(self, name, price, stock, code):
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

    def find_product(self, code):
        return self._find_product_recursive(self.root, code)

    def _find_product_recursive(self, current_node, code):
        if current_node.code == code:
            return current_node
        for child in current_node.children:
            found_product = self._find_product_recursive(child, code)
            if found_product:
                return found_product
        return None

# Contoh penggunaan Tree untuk mencari produk
product_A = ProductNode("Makanan A", 10, 50, "A001")
product_B = ProductNode("Makanan B", 20, 30, "B002")
product_C = ProductNode("Minuman A", 5, 100, "C003")

product_B.add_child(ProductNode("Cokelat", 15, 20, "D004"))
product_B.add_child(ProductNode("Kue", 10, 10, "E005"))

product_tree = ProductTree(product_A)
product_A.add_child(product_B)
product_A.add_child(product_C)

found_product = product_tree.find_product("D004")
if found_product:
    print("Product found:", found_product.name)
else:
    print("Product not found.")
