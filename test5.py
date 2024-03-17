from collections import Counter

def frequency_based_decrypt(ciphertext, freq_map):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            plaintext += freq_map[char]
        else:
            plaintext += char
    return plaintext

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
ciphertext_freq = Counter(ciphertext)
english_freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

freq_map = {}
for cipher_char, eng_char in zip(sorted(ciphertext_freq, key=ciphertext_freq.get, reverse=True), english_freq):
    freq_map[cipher_char] = eng_char

plaintext = frequency_based_decrypt(ciphertext, freq_map)
print(f"Frequency-based decryption: {plaintext}")