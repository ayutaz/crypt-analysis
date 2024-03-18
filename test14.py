cipher = "DPR HIHJ XQRH BIBJ R DHX DRX"
cipher_list = cipher.upper().split()

known_mappings = {
    'D': 'T',
    'P': 'H',
    'R': 'E',
    'R': 'A',
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

def get_possible_mappings(cipher_char, freq_order):
    if cipher_char in known_mappings:
        return [known_mappings[cipher_char]]
    else:
        return freq_order[:3]

def decrypt_with_frequency_analysis(cipher, freq_order):
    plaintext = ""
    for char in cipher:
        if char.isalpha():
            possible_mappings = get_possible_mappings(char, freq_order)
            plaintext += f"[{'/'.join(possible_mappings)}]"
        else:
            plaintext += char
    return plaintext

def apply_known_mappings(plaintext_list, known_mappings):
    for i in range(len(plaintext_list)):
        for char, mapping in known_mappings.items():
            plaintext_list[i] = plaintext_list[i].replace(f"[{char}]", mapping)
    return plaintext_list

# 既知の対応関係を使って部分的に復号
plaintext_list = [decrypt_with_known_mappings(word, known_mappings) for word in cipher_list]
partially_decrypted_text = " ".join(plaintext_list)
print("部分的に復号されたテキスト:", partially_decrypted_text)

# 文字の出現頻度を分析
frequency = analyze_frequency(cipher)
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print("\n文字の出現頻度:")
for char, count in sorted_frequency:
    print(f"{char}: {count}")

# 英語の文字の出現頻度順
english_freq_order = list("ETAOINSHRDLCUMWFGYPBVKJXQZ")

# 出現頻度を使って復号
plaintext_list = [decrypt_with_frequency_analysis(word, english_freq_order) for word in cipher_list]

# 既知の対応関係を適用
plaintext_list = apply_known_mappings(plaintext_list, known_mappings)

decrypted_text_with_freq = " ".join(plaintext_list)
print("\n出現頻度を使って復号されたテキスト:", decrypted_text_with_freq)