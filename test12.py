# 暗号文
cipher = "DPR HIHJ XQRH BIBJ R DHX DRX"

# 暗号文を大文字に変換し、空白で分割してリストに変換
cipher_list = cipher.upper().split()

# 平文と暗号文の対応関係を格納する辞書
decrypt_dict = {}

# DPR = THEの対応関係を辞書に追加
decrypt_dict['D'] = 'T'
decrypt_dict['P'] = 'H'
decrypt_dict['R'] = 'E'

# 複数の暗号化アルゴリズムを試す関数
def try_decryption_algorithms(cipher):
    plaintext_caesar = decrypt_caesar(cipher)
    plaintext_vigenere = decrypt_vigenere(cipher, "KEY")
    
    print("シーザー暗号:", plaintext_caesar)
    print("ヴィジュネル暗号:", plaintext_vigenere)

# シーザー暗号で復号する関数
def decrypt_caesar(cipher, shift=3):
    plaintext = ""
    for char in cipher:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            plaintext += char
    return plaintext

# ヴィジュネル暗号で復号する関数
def decrypt_vigenere(cipher, key):
    plaintext = ""
    key_length = len(key)
    for i, char in enumerate(cipher):
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[i % key_length].upper()
            shift = ord(key_char) - 65
            plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            plaintext += char
    return plaintext

# 暗号文のリストに対して複数の暗号化アルゴリズムを試す
for word in cipher_list:
    try_decryption_algorithms(word)