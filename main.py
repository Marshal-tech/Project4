def create_file(filename):
    text_data = [
        "Це   перший рядок,   в якому  є   зайві пробіли.",
        "А тут є слова з однієї букви: я, і, в, з, а також звичайні слова.",
        "  Ще     один    тестовий    рядок  для    перевірки.  ",
        "Одне слово",
        "я"
    ]

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for line in text_data:
                file.write(line + '\n')
        print(f"[+] Файл '{filename}' успішно створено.")
    except IOError as e:
        print(f"[-] Помилка створення файлу '{filename}': {e}")


def process_text_files(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
                open(output_filename, 'w', encoding='utf-8') as outfile:

            for line in infile:
                words = line.split()

                filtered_words = [word for word in words if len(word.strip('.,!?:;"\'')) > 1]

                processed_line = " ".join(filtered_words)

                outfile.write(processed_line + '\n')

        print(f"[+] Файл '{output_filename}' успішно згенеровано та збережено.")

    except FileNotFoundError:
        print(f"[-] Помилка: Вхідний файл '{input_filename}' не знайдено.")
    except IOError as e:
        print(f"[-] Помилка вводу-виводу під час оброблення: {e}")


def read_and_print_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"\n--- Вміст файлу '{filename}' ---")
            for line in file:
                print(line.strip())
            print("---------------------------------\n")
    except FileNotFoundError:
        print(f"[-] Помилка: Файл '{filename}' не знайдено.")
    except IOError as e:
        print(f"[-] Помилка читання файлу: {e}")


if __name__ == "__main__":
    file_1 = "TF19_1.txt"
    file_2 = "TF19_2.txt"

    create_file(file_1)

    process_text_files(file_1, file_2)

    read_and_print_file(file_2)