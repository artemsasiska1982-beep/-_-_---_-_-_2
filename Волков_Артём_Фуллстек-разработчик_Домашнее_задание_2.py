import random

# Словарь для перевода символов в азбуку Морзе
MORSE_MAP = {
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
    "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
    "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
    "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
    "'": ".----.", "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.",
    "-": "-....-", "_": "..--.-", '"': ".-..-.", "$": "...-..-", "@": ".--.-.",
    " ": "/"
}

WORDS_POOL = ["code", "bit", "list", "soul", "next", "little", "snake", "mouse"]


def encode_to_morse(plain_text):
    """
    Преобразует английский текст в последовательность кодов Морзе.

    Args:
        plain_text (str): Исходная строка на английском языке.

    Returns:
        str: Строка, состоящая из кодов Морзе, разделённых пробелами.
    """
    symbols = []
    for symbol in plain_text.lower():
        if symbol in MORSE_MAP:
            symbols.append(MORSE_MAP[symbol])
    return " ".join(symbols)


def decode_from_morse(morse_sequence):
    """
    Восстанавливает английский текст из последовательности кодов Морзе.

    Args:
        morse_sequence (str): Строка с кодами Морзе, разделёнными пробелами.

    Returns:
        str: Расшифрованный английский текст (без пробелов между буквами).
    """
    inverse_map = {code: char for char, code in MORSE_MAP.items()}
    letters = []
    for code in morse_sequence.split():
        if code in inverse_map:
            letters.append(inverse_map[code])
    return "".join(letters)


def pick_random_word():
    """
    Выбирает случайное слово из предопределённого списка.

    Returns:
        str: Случайное слово из WORDS_POOL.
    """
    return random.choice(WORDS_POOL)


def show_results(flags):
    """
    Выводит итоговую статистику по ответам пользователя.

    Args:
        flags (list): Список булевых значений (True — верно, False — неверно).

    Returns:
        None
    """
    total = len(flags)
    right = sum(flags)
    wrong = total - right
    print(f"\nВсего вопросов: {total}")
    print(f"Верных ответов: {right}")
    print(f"Неверных ответов: {wrong}")


def run_quiz():
    """
    Запускает игровой режим «Угадай слово» из пяти вопросов.

    Returns:
        None
    """
    results = []
    for attempt in range(1, 6):
        secret = pick_random_word()
        encrypted = encode_to_morse(secret)
        print(f"Слово {attempt}: {encrypted}")
        user_guess = input().strip().lower()
        if user_guess == secret:
            print(f"Верно, это слово: {secret}")
            results.append(True)
        else:
            print(f"Неверно! Зашифрованное слово было: {secret}")
            results.append(False)
    show_results(results)


def main():
    """
    Точка входа. Управляет приветствием, меню и вызовом режимов.

    Returns:
        None
    """
    print("Добрый день! Введите ваше имя:")
    username = input().strip()
    print(f"Отлично, {username}! Выберите режим работы:")
    print("1 - шифрование (английский -> Морзе)")
    print("2 - дешифрование (Морзе -> английский)")
    print("3 - Игра «Угадай слово» (5 вопросов)")
    print("4 - Выход")

    while True:
        choice = input("Ваш выбор: ").strip()
        if choice == "1":
            text = input("Введите текст на английском: ")
            print(encode_to_morse(text))
        elif choice == "2":
            morse = input("Введите код Морзе: ")
            print(decode_from_morse(morse))
        elif choice == "3":
            run_quiz()
        elif choice == "4":
            print(f"До свидания, {username}!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()