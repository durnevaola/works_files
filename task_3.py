with open("file1.txt", "r", encoding="utf-8") as f1:
    content1 = f1.read()

with open("file2.txt", "r", encoding="utf-8") as f2:
    content2 = f2.read()

with open("file3.txt", "r", encoding="utf-8") as f3:
    content3 = f3.read()

with open("combined.txt", "w", encoding="utf-8") as out:
    out.write("--- Содержимое file1.txt ---\n")
    out.write(content1)
    out.write("\n\n")

    out.write("--- Содержимое file2.txt ---\n")
    out.write(content2)
    out.write("\n\n")

    out.write("--- Содержимое file3.txt ---\n")
    out.write(content3)
    out.write("\n")
