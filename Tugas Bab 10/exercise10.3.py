# 10-3_simpler_code.py
# Versi ringkas: tidak memakai variabel sementara, langsung loop
# pada list hasil splitlines().

nama_file = "learning_python.txt"

print("Versi ringkas dengan splitlines():")
print("=" * 50)

with open(nama_file) as file:
    for baris in file.read().splitlines():
        print(baris)