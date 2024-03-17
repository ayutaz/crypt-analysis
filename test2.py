from collections import Counter

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"

frequency = Counter(ciphertext)
print("文字の頻度:")
for char, count in frequency.items():
    print(f"{char}: {count}")