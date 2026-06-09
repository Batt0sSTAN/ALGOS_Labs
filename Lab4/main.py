import string

def analyze_text(text: str):
    words = text.split()

    if not words:
        print("Empty text")
        return
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print("--- Частота слов ---")
    for word, count in word_counts.items():
        print(f"{word} -> {count}")
    
    print("-" * 20)

    most_frequent_word = max(word_counts, key=word_counts.get)
    max_count = word_counts[most_frequent_word]
    
    print(f"Most frequent word: '{most_frequent_word}' ({max_count} times)")

# Проверка работы
sample_text = "cat dog cat bird dog cat Cat dog Bird color day Big Cat Dog cat cat Bowler"
analyze_text(sample_text)