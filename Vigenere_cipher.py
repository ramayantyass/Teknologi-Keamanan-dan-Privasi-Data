# Description: Vigenere Chiper

def vigenere_cipher(plaintext, key):
    # Membuat list untuk menyimpan nilai ASCII dari plaintext dan key
    plaintext_ascii = []
    key_ascii = []
    # Membuat list untuk menyimpan nilai ASCII dari hasil enkripsi
    result_ascii = []
    # Membuat list untuk menyimpan hasil enkripsi
    result = []
    # Mengubah plaintext dan key menjadi list of ASCII code
    for char in plaintext:
        plaintext_ascii.append(ord(char))
    for char in key:
        key_ascii.append(ord(char))
    # Melakukan enkripsi dengan rumus Vigenere Cipher
    for i in range(len(plaintext_ascii)):
        # Mengubah nilai ASCII plaintext dan key menjadi nilai 0-25
        plaintext_ascii[i] -= 65
        key_ascii[i] -= 65
        # Melakukan operasi enkripsi
        result_ascii.append((plaintext_ascii[i] + key_ascii[i]) % 26)
        # Mengubah nilai ASCII hasil enkripsi menjadi nilai 65-90
        result_ascii[i] += 65
        # Mengubah nilai ASCII hasil enkripsi menjadi karakter
        result.append(chr(result_ascii[i]))
    # Menggabungkan list hasil enkripsi menjadi string
    result = ''.join(result)
    return result

# Driver code
def main():
    plaintext = input("Masukkan teks: ")
    # NIM L200200137
    # Menggunakan key 137, dikarenakan 3 Digit terakhir NIM saya adalah 137
    key = "137"
    print("Hasil enkripsi: ", vigenere_cipher(plaintext, key))

# Main
if __name__ == "__main__":
    main()