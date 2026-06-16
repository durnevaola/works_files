def caesar_encrypt(text, shift=3):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)

with open("secret.txt", "r", encoding="utf-8") as file:
    text = file.read()

encrypted_text = caesar_encrypt(text, 3)

with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, 3)

with open("decrypted.txt", "w", encoding="utf-8") as file:
    file.write(decrypted_text)
