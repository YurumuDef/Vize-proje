def atbash(text):
    # Atbash algoritması ile metni şifrele
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    reverse_alphabet = alphabet[::-1]
    result = ""
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            result += reverse_alphabet[index]
        else:
            result += char
    return result

def rot13(text):
    # ROT13 algoritması ile metni şifrele
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            result += char
    return result

# Metin girdisini al
text = input("Metni girin: ")

# Atbash ile şifrele
atbash_text = atbash(text)

# Atbash ile şifrelenmiş metni ROT13 ile şifrele
encrypted_text = rot13(atbash_text)

print("Şifrelenmiş metin: " + encrypted_text)