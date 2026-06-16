with open("words.txt", "r", encoding="utf-8") as file:
    words = file.read().splitlines()

alphabetical = sorted(words)
with open("sorted_alphabetically.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(alphabetical))

by_length = sorted(words, key=len)
with open("sorted_by_length.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(by_length))

reverse = sorted(words, reverse=True)
with open("sorted_reverse.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(reverse))
