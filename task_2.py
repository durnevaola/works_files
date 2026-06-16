word = input("Введите слово для поиска: ").lower().strip()

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

found = False
count = 0
line_numbers = []

for i, line in enumerate(lines, start=1):
    clean_line = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in line)
    words = clean_line.lower().split()
    word_count_in_line = words.count(word)

    if word_count_in_line > 0:
        found = True
        line_numbers.append(i)
        count += word_count_in_line

if found:
    print("Слово найдено")
else:
    print("Слово не найдено")

print(f"Количество: {count}")
print(f"Строки: {line_numbers}")

with open("search_results.txt", "w", encoding="utf-8") as file:
    file.write("Слово найдено\n" if found else "Слово не найдено\n")
    file.write(f"Количество: {count}\n")
    file.write(f"Строки: {line_numbers}\n")
