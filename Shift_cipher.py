# Description: Shift Cipher

def shift_cipher(text, shift):
    result = ""
    # traverse plaintext
    for i in range(len(text)):
        char = text[i]
        # jika karakter berada di antara huruf A dan Z
        if char.isalpha():
            # mengubah huruf menjadi angka ASCII
            ascii_code = ord(char)
            # menyesuaikan nilai ASCII sesuai dengan nilai shift
            shifted_ascii_code = ascii_code + shift
            # jika nilai ASCII setelah pergeseran melebihi 90 (huruf Z) 
            # atau 122 (huruf z), geser ke kembali ke A atau a
            if char.isupper():
                if shifted_ascii_code > 90:
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < 65:
                    shifted_ascii_code += 26
            else:
                if shifted_ascii_code > 122:
                    shifted_ascii_code -= 26
                elif shifted_ascii_code < 97:
                    shifted_ascii_code += 26
            # mengubah kembali nilai ASCII menjadi huruf
            shifted_char = chr(shifted_ascii_code)
            result += shifted_char
        else:
            # jika karakter bukan huruf, langsung ditambahkan ke hasil
            result += char
    return result

# Driver code
def main():
    text = input("Masukkan teks: ")
    # NIM L200200137
    # Menggunakan shift 37, dikarenakan 2 Digit terakhir NIM saya adalah 37
    shift = 37
    print("Hasil enkripsi: ", shift_cipher(text, shift))

# Main
if __name__ == "__main__":
    main()