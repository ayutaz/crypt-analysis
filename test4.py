def playfair_decrypt(ciphertext, keyword):
    # Playfair暗号の解読関数（実装が長くなるため、擬似コードで表現）
    # 1. キーワードからキーマトリックスを生成
    # 2. 暗号文を2文字ずつのペアに分割
    # 3. 各ペアについて、キーマトリックスを使って復号
    # 4. 復号された文字列を返す
    pass

ciphertext = "DPRHIHJXQRHBIBJRDHXDRX"
keywords = ["RHXD"]

for keyword in keywords:
    plaintext = playfair_decrypt(ciphertext, keyword)
    print(f"Keyword {keyword}: {plaintext}")