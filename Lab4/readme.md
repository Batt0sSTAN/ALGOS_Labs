# Лабораторная работа 4
## Подсчёт слов в тексте
### Описание задачи

Необходимо реализовать программу, которая анализирует текст и считает, сколько раз встречается каждое слово.

Например, для строки:

`"cat dog cat bird dog cat"`

результат может быть таким:

- `cat -> 3`
- `dog -> 2`
- `bird -> 1`

Это одна из самых классических задач на использование словаря.

### Обязательная часть

Реализовать:

- чтение строки или текста
- разбиение текста на слова
- подсчёт количества повторений каждого слова
- вывод результата в формате `слово -> количество`

### Вариативная часть
3. Находить самое частое слово
---

### 1. Функция анализа текста
```python
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
```

---

### 2. Проверка работы
```python
sample_text = "cat dog cat bird dog cat Cat dog Bird color day Big Cat Dog cat cat Bowler"
analyze_text(sample_text)
```

---
### 3. Вывод в консоль

```
--- Частота слов ---
cat -> 5
dog -> 3
bird -> 1
Cat -> 2
Bird -> 1
color -> 1
day -> 1
Big -> 1
Dog -> 1
Bowler -> 1
--------------------
Most frequent word: 'cat' (5 times)
```