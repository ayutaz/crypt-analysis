def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted_ascii = (ord(char) - ascii_offset - shift) % 26
            plaintext += chr(shifted_ascii + ascii_offset)
        else:
            plaintext += char
    return plaintext

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"

for shift in range(1, 26):
    plaintext = caesar_decrypt(ciphertext, shift)
    print(f"Shift {shift}: {plaintext}")