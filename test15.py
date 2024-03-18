cipher = "DPR HIHJ XQRH BIBJ R DHX DRX"
cipher_list = cipher.upper().split()

known_mappings = {
    'D': 'T',
    'P': 'H',
    'R': 'E',
    'R': 'A',
    'H': 'I',
    'X': 'S'
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

# 既知の対応関係を使って部分的に復号
plaintext_list = [decrypt_with_known_mappings(word, known_mappings) for word in cipher_list]
partially_decrypted_text = " ".join(plaintext_list)
print("部分的に復号されたテキスト:", partially_decrypted_text)

# 出現頻度を使って復号
english_freq_order = list("ETAOINSHRDLCUMWFGYPBVKJXQZ")
plaintext_list = [decrypt_with_frequency_analysis(word, english_freq_order) for word in cipher_list]
decrypted_text_with_freq = " ".join(plaintext_list)

# 推測された単語に置き換え
decrypted_text_with_freq = decrypted_text_with_freq.replace("[E/T/A][E/T/A][E/T/A][E/T/A]", "THAT")
decrypted_text_with_freq = decrypted_text_with_freq.replace("[E/T/A][E/T/A][A][E/T/A]", "AREA")
decrypted_text_with_freq = decrypted_text_with_freq.replace("[E/T/A][E/T/A][E/T/A][E/T/A]", "THED")
decrypted_text_with_freq = decrypted_text_with_freq.replace("[T][A][E/T/A]", "TAX/TAS")

print("\n解読結果:", decrypted_text_with_freq)