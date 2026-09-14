def wordCount(S):
    with open(S, "r", encoding="utf-8") as file:
        text = file.read()

    lines_count = len(text.splitlines())
    word_count = len(text.split())

    with open (S, "rb") as file:
        bytes_count = len(file.read())

    return (lines_count, word_count, bytes_count)

print(wordCount("words-list-russian.txt")) #а где этот файл найти-то ЁмоЁ, а нашла
# ура победа