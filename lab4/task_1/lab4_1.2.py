lines = []
result = ''
i = 0

def sub_list(tag, spaces, body):
    i = 0
    sub = []
    result = ''
    while i < len(body):
        if body[i].endswith(':\n'):
            if body[i].lstrip().startswith('-'):
                body[i] = body[i].replace('-', ' ', 1)
            cont = 0
            sub = []
            for j in range(i + 1, len(body)):
                if body[j].startswith(' ' * (spaces + 2)):
                    cont += 1
                    sub.append(body[j])
                else:
                    break
            result += sub_list(body[i][:body[i].find(':')].lstrip(), spaces + 2, sub)
            i += cont
        elif body[i].lstrip().startswith('-') and ':' not in body[i]:
            body[i] = body[i].replace('-', ' ', 1)
            result += body[i][:body[i].find(body[i].lstrip()[0]) - 2] + '<' + body[i].strip() + ' type=listelement>\n'
        elif body[i].strip() != '':
            if body[i].lstrip().startswith('-'):
                body[i] = body[i].replace('-', ' ', 1)
                body[i] = body[i][2:]
            result += body[i][:body[i].find(body[i].lstrip()[0])] + '<' + body[i].lstrip()[:body[i].find(':') - spaces] + '>' + body[i][body[i].find(':') + 2 : -1] + '</' + body[i].lstrip()[:body[i].find(':') - spaces] + '>\n'
        i += 1
    return ' ' * (spaces - 2) + '<' + tag + '>\n' + result + ' ' * (spaces - 2) + '</' + tag + '>\n'

with open('lab4_1.yaml', 'r') as yaml_file:
    for line in yaml_file: #добавляя, убираем коммы
        if '#' in line:
            line = line[:line.find('#')]
        line = line.replace('{', '')
        line = line.replace('}', '')
        if line.strip() != '':
            lines.append(line.rstrip())

for h in range(len(lines)): # убираем кавычки, если они есть
    if '\"' in lines[h]:
        lines[h] = lines[h].replace('\"', '')

while i < len(lines):
    if lines[i].endswith(':'):
        sub = []
        cont = 0
        for j in range(i + 1, len(lines)):
            if lines[j].startswith('  '):
                sub.append(lines[j] + '\n')
                cont += 1
            else:
                break
        result += sub_list(lines[i][:lines[i].find(':')], 2, sub)
        i += cont
    elif lines[i].strip() != '':
        result += '<' + lines[i][:lines[i].find(':')] + '>' + lines[i][lines[i].find(':') + 2:] + '</' + lines[i][:lines[i].find(':')] + '>\n'
    
    i += 1

with open('lab4_1.xml', 'w') as xml_file:
    xml_file.write(result)