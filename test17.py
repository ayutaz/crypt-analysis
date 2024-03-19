import random
import itertools
import nltk
import json
from multiprocessing import Pool, cpu_count

def generate_sentence(alphabet, length):
    sentence = ''.join(random.choices(alphabet, k=length))
    return sentence

def is_meaningful(sentence):
    words = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(words)
    
    has_noun = any(tag.startswith('NN') for _, tag in tagged)
    has_verb = any(tag.startswith('VB') for _, tag in tagged)
    
    return has_noun and has_verb

def process_alphabet(alphabet):
    while True:
        # 22文字の英文を生成
        sentence = generate_sentence(alphabet, 22)
        
        # 英文が意味が通っているかどうかを判定
        if is_meaningful(sentence):
            return (alphabet, sentence)

if __name__ == '__main__':
    # アルファベットの全組み合わせを生成
    alphabets = list(itertools.combinations('abcdefghijklmnopqrstuvwxyz', 9))

    # プロセス数を設定（CPUコア数に基づく）
    num_processes = cpu_count()

    # マルチプロセスを使用して並列処理
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_alphabet, alphabets)

    # 結果をJSONファイルに保存
    data = []
    for alphabet, sentence in results:
        item = {
            'alphabet': ''.join(alphabet),
            'sentence': sentence
        }
        data.append(item)

    with open('meaningful_sentences.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("意味が通る文章がJSONファイルに保存されました。")