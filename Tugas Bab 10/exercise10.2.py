# Mengganti kata "Python" dengan bahasa lain (misal: C).
nama_file = "learning_python.txt"

with open(nama_file) as file:
    for baris in file:
        baris_baru = baris.replace("Python", "C")
        print(baris_baru.rstrip())