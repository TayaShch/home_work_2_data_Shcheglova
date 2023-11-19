"""Counter"""

from collections import Counter
counter_Moscow = ["red", "white", "black", "yellow", "green"]
counter_SPB = ["red", "white", "black", "yellow", "red", "red", "red"]
c = Counter (counter_Moscow) # передаем этрированный объект в Counter - счетсчик, выдает словарь
print(c)
c1 = Counter(counter_SPB)
print(c["yellow"]) # выводить счетчик по ключу
print(c.values()) # выводим сколько встретилось каждой машины
print(sum(c.values())) # выводим общее количество машин
print(Counter(counter_Moscow) + Counter(counter_SPB)) # сложение счтечиков
print(Counter(counter_Moscow) - Counter(counter_SPB)) # вычитание счетчиков
print(c1.subtract(c)) #  вычитание счетчиков
print(c1.most_common(2))# 2 самые часто встречающиеся по частоте счетчика
