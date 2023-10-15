"""Counter"""

from collections import Counter
lst = ["red", "white", "black", "yellow", "green"]
c = Counter (lst) # передаем этрированный объект в Counter - счетсчик, выдает словарь
print(c)

print(c["yellow"]) # выводить счетчик по ключу
print(c.values()) # выводим сколько встретилось каждой машины
print(sum(c.values())) # выводим общее количество машин