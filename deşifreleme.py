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

# ROT13 ile şifrelenmiş metni Atbash ile deşifrele
decrypted_text = atbash(rot13(text))

print("Deşifrelenmiş metin: " + decrypted_text)
