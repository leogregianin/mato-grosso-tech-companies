# coding: utf-8
from collections import Counter
import json

stats = {'city': 3, 'technology': 4, 'database': 5, 'cloud': 6}

def generate_charts(chart_type):
    columns = filter_columns('README.md', stats[chart_type])
    sorted_columns_names = sorted(columns, key=columns.get, reverse=True)
    
    with open(f'{chart_type}_usage.md', 'w+', encoding='UTF-8') as f:
        f.write('|+%s | Count |\n' % chart_type.capitalize())
        f.write('|------------ | -----------|\n')
        for columns_name in sorted_columns_names:
            count = columns[columns_name]
            f.write(f'| {columns_name} | {count} |\n')
    with open(f'{chart_type}_usage.json', 'w+', encoding='UTF-8') as f:
        json.dump(columns, f, sort_keys=True, indent=2, ensure_ascii=False)

def filter_columns(readme_file, column_number):
    counter = Counter()
    with open(readme_file, 'r', encoding='UTF-8') as read_me_file:
        for line in read_me_file:
            s_line = line.lstrip()
            if any([s_line.startswith(s) for s in ['| '] if s not in ('|+')]):
                tech_column = s_line.split('|')[column_number]
                columns = tech_column.split(',')
                columns = list(map(str.strip, columns))
                columns = list(filter(lambda x: x != '-', columns))
                columns = list(filter(lambda x: x, columns)) # filter empty items
                for column in columns:
                    counter[column] += 1
    return counter

def sort():
    with open('README.md', 'r', encoding='UTF-8') as read_me_file:
        read_me = read_me_file.readlines()

    blocks = []
    last_indent = None
    for line in read_me:
        s_line = line.lstrip()
        indent = len(line) - len(s_line)

        if any([s_line.startswith(s) for s in ['| '] if s not in ('|+') ]):
            if indent == last_indent:
                blocks[-1].append(line)
            else:
                blocks.append([line])
            last_indent = indent
        else:
            blocks.append([line])
            last_indent = None

    with open('README.md', 'w+', encoding='UTF-8') as sorted_file:
        blocks = [''.join(sorted(block, key=lambda s: s.lower())) for block in blocks]
        sorted_file.write(''.join(blocks))
    
        with open(f'empresas.json', 'w+', encoding='UTF-8') as f:
        for block in blocks:
            if block.startswith('| '):
                l_block = block.splitlines()
        ciaList = {}
        for cia in l_block:
            ciacol = (cia.split('|'))
            name = ciacol[1].strip()
            site = ciacol[2].strip().replace('[Site](','').replace(')','')
            city = None if ciacol[3].strip() == '-' else ciacol[3].strip()
            technology = None if ciacol[4].strip() == '-' else ciacol[4].strip().split(', ')
            database = None if ciacol[5].strip() == '-' else ciacol[5].strip().split(', ')
            cloud = None if ciacol[6].strip() == '-' else ciacol[6].strip().split(', ')
            tipo = ciacol[7].strip()
            ciaList[name] = {'site': site, 'city': city, 'technology': technology , 'database': database ,'cloud': cloud ,'type': tipo}
        json.dump(ciaList, f, sort_keys=True, indent=2, ensure_ascii=False)

    for chart_type in stats.keys():
        generate_charts(chart_type)

if __name__ == "__main__":
    sort()
