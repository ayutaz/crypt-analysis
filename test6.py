import json
from itertools import permutations, product

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

def analyze_decrypted_text(plaintext):
    double_letters = ["AA", "KK", "MM", "OO", "QQ", "UU", "SS"]
    for dl in double_letters:
        if dl in plaintext:
            analyzed_text = plaintext.replace(dl, dl[0] + " ")
            return analyzed_text
    return None

def generate_keywords(length, chars):
    return [''.join(p) for p in product(chars, repeat=length)]

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
keyword_chars = "RHXDPQBIJ"

decryption_results = []

for length in range(1, 6):
    keywords = generate_keywords(length, keyword_chars)
    for keyword in keywords:
        plaintext = vigenere_decrypt(ciphertext, keyword)
        analyzed_text = analyze_decrypted_text(plaintext)
        
        decryption_result = {
            "keyword": keyword,
            "plaintext": plaintext,
            "analyzed_text": analyzed_text
        }
        decryption_results.append(decryption_result)

with open('vigenere_decryption_results.json', 'w') as f:
    json.dump(decryption_results, f, indent=2)