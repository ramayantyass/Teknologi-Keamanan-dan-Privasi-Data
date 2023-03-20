# Description : Transposition Cipher

def transposition_cipher(text, key):
    # Membuat list untuk menyimpan hasil enkripsi
    result = []
    # Membuat list untuk menyimpan nilai ASCII dari plaintext
    plaintext_ascii = []
    # Membuat list untuk menyimpan nilai ASCII dari hasil enkripsi
    result_ascii = []
    # Membuat list untuk menyimpan nilai ASCII dari key
    key_ascii = []
    # Membuat list untuk menyimpan nilai ASCII dari key yang sudah diurutkan
    sorted_key_ascii = []
    # Membuat list untuk menyimpan index dari key yang sudah diurutkan
    sorted_key_index = []
    # Membuat list untuk menyimpan nilai ASCII dari hasil enkripsi yang sudah diurutkan
    sorted_result_ascii = []
    # Mengubah plaintext dan key menjadi list of ASCII code
    for char in text:
        plaintext_ascii.append(ord(char))
    for char in key:
        key_ascii.append(ord(char))
    # Mengurutkan key
    sorted_key_ascii = sorted(key_ascii)
    # Mencari index dari key yang sudah diurutkan
    for i in range(len(sorted_key_ascii)):
        sorted_key_index.append(key_ascii.index(sorted_key_ascii[i]))
    # Melakukan enkripsi dengan rumus Transposition Cipher
    for i in range(len(plaintext_ascii)):
        # Mengubah nilai ASCII plaintext menjadi nilai 0-25
        plaintext_ascii[i] -= 65
        # Melakukan operasi enkripsi
        result_ascii.append((plaintext_ascii[i] + key_ascii[i]) % 26)
        # Mengubah nilai ASCII hasil enkripsi menjadi nilai 65-90
        result_ascii[i] += 65
    # Mengurutkan hasil enkripsi berdasarkan index key yang sudah diurutkan
    for i in range(len(sorted_key_index)):
        sorted_result_ascii.append(result_ascii[sorted_key_index[i]])
    # Mengubah nilai ASCII hasil enkripsi menjadi karakter
    for i in range(len(sorted_result_ascii)):
        result.append(chr(sorted_result_ascii[i]))
    # Menggabungkan list hasil enkripsi menjadi string
    result = ''.join(result)
    return result

# Driver code
def main():
    text = input('Masukkan teks: ')
    key = input('Masukkan key: ')
    print('Hasil enkripsi: ', transposition_cipher(text, key))

# Main
if __name__ == '__main__':
    main()