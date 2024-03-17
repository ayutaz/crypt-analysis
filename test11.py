import string
import re
import enchant
import json

def shift_cipher_decrypt(ciphertext, shift):
    alphabet = string.ascii_uppercase
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            index = alphabet.index(char)
            plaintext += alphabet[(index - shift) % 26]
        else:
            plaintext += char
    return plaintext

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # 乗法逆元が存在しない場合はNoneを返す
    else:
        return x % m

def affine_cipher_decrypt(ciphertext, a, b):
    alphabet = string.ascii_uppercase
    plaintext = ""
    a_inv = modinv(a, 26)  # 乗法逆元を計算
    if a_inv is None:
        return None  # 乗法逆元が存在しない場合はNoneを返す
    for char in ciphertext:
        if char.isalpha():
            index = alphabet.index(char)
            plaintext += alphabet[(a_inv * (index - b)) % 26]
        else:
            plaintext += char
    return plaintext

def substitution_cipher_decrypt(ciphertext, key):
    alphabet = string.ascii_uppercase
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            index = key.index(char)
            plaintext += alphabet[index]
        else:
            plaintext += char
    return plaintext

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    english_words = sum(1 for word in words if d.check(word))
    return english_words / word_count if word_count > 0 else 0

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
d = enchant.Dict("en_US")

results = []

# シフト暗号
best_shift = 0
best_score = 0
for shift in range(1, 26):
    plaintext = shift_cipher_decrypt(ciphertext, shift)
    score = analyze_text(plaintext)
    if score > best_score:
        best_shift = shift
        best_score = score
result = {
    "cipher": "Shift Cipher",
    "best_shift": best_shift,
    "best_score": best_score,
    "decrypted_text": shift_cipher_decrypt(ciphertext, best_shift)
}
results.append(result)

# アフィン暗号
best_a = 0
best_b = 0
best_score = 0
for a in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:  # 法26と互いに素な値に限定
    for b in range(26):
        plaintext = affine_cipher_decrypt(ciphertext, a, b)
        score = analyze_text(plaintext)
        if score > best_score:
            best_a = a
            best_b = b
            best_score = score
result = {
    "cipher": "Affine Cipher",
    "best_a": best_a,
    "best_b": best_b,
    "best_score": best_score,
    "decrypted_text": affine_cipher_decrypt(ciphertext, best_a, best_b)
}
results.append(result)

# 単一換字式暗号
key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
plaintext = substitution_cipher_decrypt(ciphertext, key)
score = analyze_text(plaintext)
result = {
    "cipher": "Substitution Cipher",
    "key": key,
    "score": score,
    "decrypted_text": plaintext
}
results.append(result)

# 結果をJSONファイルに保存
with open("decryption_results_11.json", "w") as file:
    json.dump(results, file, indent=2)