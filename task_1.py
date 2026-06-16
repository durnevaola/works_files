file = open("input.txt", "r", encoding="utf-8")

line_count = 0
word_count = 0

for line in file:
    line_count += 1
    words = line.split()
    word_count += len(words)

file.close()

file = open("statistics.txt", "w", encoding="utf-8")
file.write("Количество строк: " + str(line_count) + "\n")
file.write("Количество слов: " + str(word_count) + "\n")
file.close()
