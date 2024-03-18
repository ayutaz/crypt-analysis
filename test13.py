cipher = "DPR HIHJ XQRH BIBJ R DHX DRX"
cipher_list = cipher.upper().split()

known_mappings = {
    'D': 'T',
    'P': 'H',
    'R': 'E',
    'R': 'A'  # 2つ目の'R'が'A'に対応するという情報を追加
}

def decrypt_with_known_mappings(cipher, mappings):
    plaintext = ""
    for char in cipher:
        if char in mappings:
            plaintext += mappings[char]
        else:
            plaintext += "_"
    return plaintext

def analyze_frequency(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

plaintext_list = [decrypt_with_known_mappings(word, known_mappings) for word in cipher_list]
partially_decrypted_text = " ".join(plaintext_list)
print("部分的に復号されたテキスト:", partially_decrypted_text)

frequency = analyze_frequency(cipher)
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print("\n文字の出現頻度:")
for char, count in sorted_frequency:
    print(f"{char}: {count}")