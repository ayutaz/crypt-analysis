import json
import re

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

def find_patterns(text, pattern_length):
    patterns = re.findall(r'(?=(.{' + str(pattern_length) + '}))', text)
    return list(set(patterns))

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
promising_keywords = ["RHX", "RHXD", "RHXDP", "RHXDRX", "RHXDPHI", "RHXDJQB"]

decryption_results = []

for keyword in promising_keywords:
    plaintext = vigenere_decrypt(ciphertext, keyword)
    analyzed_text = analyze_decrypted_text(plaintext)
    
    two_letter_patterns = find_patterns(plaintext, 2)
    three_letter_patterns = find_patterns(plaintext, 3)
    
    decryption_result = {
        "keyword": keyword,
        "plaintext": plaintext,
        "analyzed_text": analyzed_text,
        "two_letter_patterns": two_letter_patterns,
        "three_letter_patterns": three_letter_patterns
    }
    decryption_results.append(decryption_result)

with open('vigenere_decryption_results_focused.json', 'w') as f:
    json.dump(decryption_results, f, indent=2)