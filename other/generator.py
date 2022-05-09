file = open("words.txt", mode="a", encoding="UTF-8")
while True:
    x=input("Kelime gir: ")
    file.write(f'<div class="word"><p>{x}</p></div>\n')

