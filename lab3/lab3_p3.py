# isu % 5 -> 0
import re

s = input()
correct = re.fullmatch(r'([\w._])+@[a-z]+([.][a-z]+)+', s) # проверка на соответсвие шаблону

if bool(correct):
    print(re.split('@', s)[1]) # если соот-вие подтвердилось, выводим почтовый сервер
else:
    print('Fail!')