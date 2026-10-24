import re
from collections import Counter
from datetime import datetime

# Функції для базових операцій з рядками

def find_substring(text, substring):
    """
    Пошук підрядка в тексті.
    Повертає індекс першого входження або -1, якщо підрядок не знайдено.
    """
    return text.find(substring)

def replace_substring(text, old, new):
    """
    Заміна підрядка в тексті.
    """
    return text.replace(old, new)

def split_text(text, delimiter=' '):
    """
    Розділення тексту за роздільником.
    """
    return text.split(delimiter)

def format_string_f(name, age):
    """
    Форматування рядка з використанням f-string.
    Приклад: "Мене звати [name] і мені [age] років."
    """
    return f"Мене звати {name} і мені {age} років."

def format_string_method(name, age):
    """
    Форматування рядка з використанням методу .format().
    Приклад: "Мене звати [name] і мені [age] років."
    """
    return "Мене звати {} і мені {} років.".format(name, age)

# Функції для роботи з регулярними виразами та валідації

def extract_emails(text):
    """
    Витяг email адрес з тексту.
    """
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

def validate_email(email):
    """
    Валідація email за допомогою регулярного виразу.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))

def validate_password(password):
    """
    Валідація пароля: мінімум 8 символів, цифри, великі/малі літери та спецсимволи.
    """
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False
    return True

def validate_date(date_str):
    """
    Валідація дати у форматі DD.MM.YYYY або DD-MM-YYYY з обробкою винятків.
    """
    try:
        datetime.strptime(date_str, '%d.%m.%Y')
        return True
    except ValueError:
        try:
            datetime.strptime(date_str, '%d-%m-%Y')
            return True
        except ValueError:
            return False

def validate_phone_number(number):
    """
    Валідація українського телефонного номера.
    Формат: +380xxxxxxxxx
    """
    pattern = r'^\+380\d{9}$'
    return bool(re.match(pattern, number))

def extract_hashtags(text):
    """
    Витяг хештегів з тексту.
    """
    pattern = r'#\w+'
    return re.findall(pattern, text)

def extract_mentions(text):
    """
    Витяг згадувань користувачів з тексту (напр. @user).
    """
    pattern = r'@\w+'
    return re.findall(pattern, text)

# Функції для аналізу тексту

def count_words(text):
    """
    Підрахунок кількості слів у тексті.
    """
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def count_sentences(text):
    """
    Підрахунок кількості речень у тексті.
    """
    sentences = re.split(r'[.!?]+', text)
    return len([s for s in sentences if s.strip()])

def word_frequency(text):
    """
    Підрахунок частоти слів у тексті.
    Повертає об'єкт Counter.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def analyze_text(text):
    """
    Комплексний аналіз тексту.
    Повертає словник з результатами аналізу.
    """
    freq = word_frequency(text)
    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'word_frequency': freq.most_common(5),
        'emails': extract_emails(text),
        'hashtags': extract_hashtags(text)
    }

def format_analysis_results(results):
    """
    Форматування результатів аналізу для зручного виведення.
    """
    output = "Результати аналізу тексту:\n"
    output += f"- Кількість слів: {results.get('word_count', 0)}\n"
    output += f"- Кількість речень: {results.get('sentence_count', 0)}\n"
    output += f"- Топ-5 найчастіших слів: {results.get('word_frequency', [])}\n"
    output += f"- Знайдені email: {results.get('emails', [])}\n"
    output += f"- Знайдені хештеги: {results.get('hashtags', [])}\n"
    return output

# Функція для вилучення даних за варіантом

def extract_variant_data(text, variant_pattern):
    """
    Вилучає дані з тексту за допомогою патерну, специфічного для варіанту.
    """
    return re.findall(variant_pattern, text)

# Головна частина програми

def read_file_content(filepath):
    """
    Читає вміст файлу з обробкою винятків.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None

def main():
    """
    Головна функція, що керує виконанням програми.
    """
    print("Ласкаво просимо до аналізатора тексту!")

    # Шлях до файлу з текстом
    text_filepath = 'src/data/neoterra_text.txt'

    # Читання тексту з файлу
    text_to_analyze = read_file_content(text_filepath)
    if not text_to_analyze:
        return # Завершити, якщо файл не прочитано

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Валідація форми (Email, Пароль, Дата)")
            print("4. Вилучення моделей реакторів")
            print("5. Вихід")
            choice = input("Ваш вибір: ")

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону для валідації (формат +380xxxxxxxxx): ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                print("--- Валідація форми ---")
                email = input("Введіть email: ")
                password = input("Введіть пароль (мін. 8 символів, цифри, літери, спецсимвол): ")
                date_str = input("Введіть дату (формат DD.MM.YYYY): ")

                if validate_email(email):
                    print(" Email валідний.")
                else:
                    print("Email невалідний.")

                if validate_password(password):
                    print(" Пароль валідний.")
                else:
                    print("Пароль занадто слабкий або не відповідає вимогам.")

                if validate_date(date_str):
                    print(" Дата валідна.")
                else:
                    print("Дата неваільдна або невірний формат.")

            elif choice == '4':
                # Вилучення моделей термоядерних реакторів
                pattern = r'\b[A-Z]{2}-\d+\b'
                variant_data = extract_variant_data(text_to_analyze, pattern)
                print(f"Знайдені моделі термоядерних реакторів: {variant_data}")

            elif choice == '5':
                print("Дякуємо за використання аналізатора!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()