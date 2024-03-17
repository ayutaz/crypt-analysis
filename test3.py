def vigenere_decrypt(ciphertext, keyword):
    plaintext = ""
    keyword_length = len(keyword)
    keyword_index = 0
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65
            shifted_ascii = (ord(char) - ascii_offset - (ord(keyword[keyword_index % keyword_length]) - ascii_offset)) % 26
            plaintext += chr(shifted_ascii + ascii_offset)
            keyword_index += 1
        else:
            plaintext += char
    return plaintext

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
keywords = ["RH", "RHXD"]

for keyword in keywords:
    plaintext = vigenere_decrypt(ciphertext, keyword)
    print(f"Keyword {keyword}: {plaintext}")