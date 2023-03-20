# Description: Substitution Cipher

import random

def substitution_cipher(text):
    # Membuat kamus alfabet dan kamus sandi dengan karakter acak
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution_dict = {}
    random_alphabet = list(alphabet)
    random.shuffle(random_alphabet)
    for i in range(len(alphabet)):
        substitution_dict[alphabet[i]] = random_alphabet[i]
    # Mengenkripsi teks menggunakan kamus sandi
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += substitution_dict[char]
            else:
                result += substitution_dict[char.upper()].lower()
        else:
            result += char
    return result, substitution_dict

# Driver code
def main():
    text = input("Masukkan teks: ")
    print("Hasil enkripsi: ", substitution_cipher(text))

# Main
if __name__ == "__main__":
    main()