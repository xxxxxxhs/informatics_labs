# https://itmo.ru/ru/schedule/0/M33001/raspisanie_zanyatiy_M33001.htm -- schedule
# YAML -> XML (Var. 34)
import time
start = time.time()
time.sleep(44)
lines = []

with open('lab4_1.yaml', 'r') as yaml_file:
    for line in yaml_file:
        lines.append(line.rstrip())


day_of_week = lines.pop(0)[:-1]
schedule = {}

key = lines.pop(0).lstrip()[:-1]
atributes = {}
for line in lines:
    if line.startswith('    '):
        atributes[line.lstrip().split(': ')[0]] = line.lstrip().split(': ')[1]
    else:
        schedule[key] = atributes
        atributes = {}
        key = line.lstrip()[:-1]
schedule[key] = atributes


result = '<' + day_of_week + '>\n'
for i in schedule:
    result += ('\t<' + i + '>\n')
    for j in schedule.get(i):
        result += ('\t\t<' + j + '>' + schedule.get(i).get(j) + '</' + j + '>\n')
    result += ('\t</' + i + '>\n')
result += '</' + day_of_week + '>'

with open('lab4_1.xml', 'w') as xml_file:
    xml_file.write(result)

end = time.time()
print((end - start) * 100)