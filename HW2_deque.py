from collections import deque

# Функція для перевірки паліндрома
def is_palindrome(input_string):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Створюємо двосторонню чергу
    char_deque = deque(normalized_string)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Тестування функції
test_strings = [
    "A man a plan a canal Panama",
    "racecar",
    "hello",
    "Was it a car or a cat I saw",
    "No lemon, no melon"
]

for test in test_strings:
    result = is_palindrome(test)
    print(f"'{test}' є паліндромом: {result}")
