import re
import itertools
import enchant
import json
from multiprocessing import Pool, cpu_count

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    if key_length == 0:
        return ciphertext  # キーの長さが0の場合は、平文をそのまま返す
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65
            shifted_ascii = (ord(char) - ascii_offset - (ord(key[key_index % key_length]) - ascii_offset)) % 26
            plaintext += chr(shifted_ascii + ascii_offset)
            key_index += 1
        else:
            plaintext += char
    return plaintext

def analyze_text(text):
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    english_words = sum(1 for word in words if d.check(word))
    return english_words / word_count if word_count > 0 else 0

def generate_key_patterns(length):
    if length == 0:
        return ['']
    common_bigrams = ['TH', 'HE', 'IN', 'EN', 'NT', 'RE', 'ER', 'AN', 'TI', 'ES']
    common_trigrams = ['THE', 'AND', 'ING', 'ENT', 'ION', 'HER', 'FOR', 'THA', 'NTH', 'INT']
    key_chars = ''.join(set(''.join(common_bigrams + common_trigrams)))
    return [''.join(p) for p in itertools.product(key_chars, repeat=length)]

def decrypt_and_analyze(args):
    key, ciphertext = args
    if len(key) == 0:
        return key, 0
    plaintext = vigenere_decrypt(ciphertext, key)
    score = analyze_text(plaintext)
    return key, score

def find_best_key(ciphertext, key_patterns):
    pool = Pool(processes=cpu_count())
    results = pool.map(decrypt_and_analyze, [(key, ciphertext) for key in key_patterns])
    pool.close()
    pool.join()
    if not results:
        return '', 0
    best_key, best_score = max(results, key=lambda x: x[1])
    return best_key, best_score

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
key_lengths = [3, 4, 5, 6,7]  # 検証するキーの長さのリスト
d = enchant.Dict("en_US")  # 英語の辞書をロード

results = []

for length in key_lengths:
    print(f"\nKey length: {length}")
    key_patterns = generate_key_patterns(length)
    best_key, best_score = find_best_key(ciphertext, key_patterns)
    best_plaintext = vigenere_decrypt(ciphertext, best_key)
    print(f"Best key: {best_key}")
    print(f"Best score: {best_score:.2f}")
    print(f"Best plaintext: {best_plaintext}")
    
    result = {
        'key_length': length,
        'best_key': best_key,
        'best_score': best_score,
        'best_plaintext': best_plaintext
    }
    results.append(result)

# 結果をJSONファイルに保存
with open('vigenere_decryption_results.json', 'w') as f:
    json.dump(results, f, indent=2)