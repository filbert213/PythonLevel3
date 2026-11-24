import sqlite3 

# Membuka file basis data
con = sqlite3.connect('marvel.db')

# Membuat tabel
# with con:
#     con.execute("""
#         CREATE TABLE marvel (
#             ID INTEGER PRIMARY KEY,
#             name TEXT,
#             superpower TEXT,
#             status TEXT
#         );
#     """)

# Mempersiapkan kueri
# sql = 'INSERT INTO marvel (ID, name, superpower, status) values(?, ?, ?, ?)'

# Menentukan data untuk kueri
# data = [
#     (1, 'Iron Man', 'Iron Suit', 'Good'),
#     (2, 'Thor', 'Mjolnir', 'Good'),
#     (3, 'Hulk', 'Super Strength', 'Good'),
#     (4, 'Magneto', 'Metal Control', 'Bad'),
#     (5, 'Doom', 'Magic', 'Bad'),
# ]

# Menambahkan semua data sekaligus menggunakan kueri iteratif
# with con:
#     con.executemany(sql, data)

# Memperbarui status Hulk
# with con:
#     con.execute("UPDATE marvel SET status = 'Deceased' WHERE name = ?",('Iron Man',))
#     con.execute("UPDATE marvel SET name = 'Dr. Doom' WHERE name = ?",('Doom',))

# Menghapus entri dengan nama Thor
with con:
    con.execute("DELETE FROM marvel WHERE name = ?",('Hulk',))