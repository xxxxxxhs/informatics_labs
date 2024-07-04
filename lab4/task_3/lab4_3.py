import re


lines = []

with open('lab4_3.yaml', 'r') as yaml_file:
    for line in yaml_file:
        lines.append(line.rstrip())

for i in lines:
    if bool(re.fullmatch(r'\b\w*\b:', i)):
        day_of_week = i[:-1]
        lines.remove(i)

schedule = {}

key = lines.pop(0).lstrip()[:-1]
atributes = {}
for line in lines:
    if bool(re.fullmatch(r'    ([-A-Za-z0-9]| |.|/)*', line)):
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

with open('lab4_3.xml', 'w') as xml_file:
    xml_file.write(result)
