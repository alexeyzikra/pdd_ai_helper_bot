# в цикле извлекаем текст всего ПДД, типа такого:

with open("glava_1.txt", "r", encoding="utf-8") as f:
    glava_1 = f.read()


text_system_promt = "Ты консуульант по ПДД РБ, должен отвечать только на основе текста ниже и тд... вот текст ПДД:"

system_promt = text_system_promt + glava_1 + glava_2 + ...