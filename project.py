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

def daftar():
    for i,k in enumerate(db):
        jarak = 20 - len(k)
        spasi = " "
        index = str(i+1)+" " if i+1 < 10 else i+1
        print(f"{index}. Barang {k}{spasi*jarak}| \n\tHarga Rp.{db[k]}")