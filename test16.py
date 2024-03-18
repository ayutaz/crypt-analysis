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

def decrypt_with_frequency_analysis(cipher, freq_order):
    plaintext = ""
    for char in cipher:
        if char.isalpha():
            if char in known_mappings:
                plaintext += known_mappings[char]
            else:
                plaintext += f"[{freq_order[0]}/{freq_order[1]}/{freq_order[2]}]"
        else:
            plaintext += char
    return plaintext

# 既知の対応関係を使って部分的に復号
plaintext_list = [decrypt_with_known_mappings(word, known_mappings) for word in cipher_list]
partially_decrypted_text = " ".join(plaintext_list)
print("部分的に復号されたテキスト:", partially_decrypted_text)

# 出現頻度を使って復号
english_freq_order = list("ETAOINSHRDLCUMWFGYPBVKJXQZ")
plaintext_list = [decrypt_with_frequency_analysis(word, english_freq_order) for word in plaintext_list]
decrypted_text_with_freq = " ".join(plaintext_list)

# 推測されたパターンに置き換え
decrypted_text_with_freq = decrypted_text_with_freq.replace("T", "[T]")
decrypted_text_with_freq = decrypted_text_with_freq.replace("H", "[H]")
decrypted_text_with_freq = decrypted_text_with_freq.replace("A", "[A]")
decrypted_text_with_freq = decrypted_text_with_freq.replace("I[E/T/A]I[E/T/A]", "[IEIE/IAIA]")
decrypted_text_with_freq = decrypted_text_with_freq.replace("S[E/T/A][A]I", "[SEAI/SAAI/STAI]")
decrypted_text_with_freq = decrypted_text_with_freq.replace("TIS", "[TIS/THIS]")
decrypted_text_with_freq = decrypted_text_with_freq.replace("TAS", "[TAS/TAX]")

print("\n解読結果:", decrypted_text_with_freq)