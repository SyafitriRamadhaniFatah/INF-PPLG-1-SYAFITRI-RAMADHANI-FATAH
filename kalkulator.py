# MULAI

# Deklarasi variabel
a = 0
b = 0
op = ''
hasil = 0

# Input nilai a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Input operator
op = input("Masukkan operator (+, -, *, /): ")

# Proses perhitungan berdasarkan operator
if op == '+':
    hasil = a + b
elif op == '-':
    hasil = a - b
elif op == '*':
    hasil = a * b
elif op == '/':
    if b != 0:
        hasil = a / b
    else:
        hasil = "Error: Pembagian dengan nol!"
else:
    hasil = "Operator tidak dikenali!"

# Cetak hasil
print("Hasil:", hasil)

# SELESAI
