from pathlib import Path
import os

texts_list = []
folder = Path("text_pdd/glavy_ppd")

# в цикле извлекаем текст всего ПДД:
for path in sorted(folder.glob("glava_*.txt")):
    text = path.read_text(encoding="utf-8")
    texts_list.append(text)

texts = tuple(texts_list)


system_promt = "Ты консуульант по ПДД РБ, должен отвечать только на основе текста ниже и тд... вот текст ПДД:"

for elem in texts_list:
    system_promt = system_promt + "\n\n" + elem
