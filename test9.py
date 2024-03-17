import json
import re
from collections import Counter

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
    space_patterns = ["AA", "UU", "SS"]
    for pattern in space_patterns:
        plaintext = plaintext.replace(pattern, pattern[0] + " ")
    return plaintext

def find_patterns(text, pattern_length):
    patterns = re.findall(r'(?=(.{' + str(pattern_length) + '}))', text)
    return Counter(patterns)

def substitute_letters(text, substitution_map):
    for old_char, new_char in substitution_map.items():
        text = text.replace(old_char, new_char)
    return text

def generate_substitution_map(frequent_patterns):
    substitution_map = {}
    for pattern, _ in frequent_patterns:
        if len(pattern) == 2:
            substitution_map[pattern] = pattern.lower()
        elif len(pattern) == 3:
            substitution_map[pattern] = pattern.capitalize()
    return substitution_map

def substitute_patterns(text, substitution_map):
    for old_pattern, new_pattern in substitution_map.items():
        text = text.replace(old_pattern, new_pattern)
    return text

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
promising_keywords = ["RHX", "RHXD", "RHXDP", "RHXDRX", "RHXDPHI", "RHXDJQB"]

decryption_results = []

for keyword in promising_keywords:
    plaintext = vigenere_decrypt(ciphertext, keyword)
    analyzed_text = analyze_decrypted_text(plaintext)
    
    two_letter_patterns = find_patterns(plaintext, 2)
    three_letter_patterns = find_patterns(plaintext, 3)
    
    substitution_map = generate_substitution_map(two_letter_patterns.most_common(5))
    substitution_map.update(generate_substitution_map(three_letter_patterns.most_common(5)))
    
    substituted_text = substitute_patterns(analyzed_text, substitution_map)
    
    decryption_result = {
        "keyword": keyword,
        "plaintext": plaintext,
        "analyzed_text": analyzed_text,
        "substituted_text": substituted_text,
        "two_letter_patterns": two_letter_patterns.most_common(5),
        "three_letter_patterns": three_letter_patterns.most_common(5)
    }
    decryption_results.append(decryption_result)

with open('vigenere_decryption_results_automated.json', 'w') as f:
    json.dump(decryption_results, f, indent=2)