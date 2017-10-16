# coding: utf-8
from collections import Counter


def generate_charts(chart_type):
    technologies = filter_technologies('README.md', {'technology': 4, 'database': 5, 'cloud': 6}[chart_type])
    sorted_technology_names = sorted(technologies, key=technologies.get, reverse=True)
    with open(f'{chart_type}_usage.md', 'w+', encoding='UTF-8') as f:
        f.write('|+Tecnologia  | Quantidade |\n')
        f.write('|------------ | -----------|\n')
        for technology_name in sorted_technology_names:
            count = technologies[technology_name]
            f.write(f'|{technology_name} |{count} |\n')

def filter_technologies(readme_file, column_number):
    counter = Counter()
    with open(readme_file, 'r', encoding='UTF-8') as read_me_file:
        for line in read_me_file:
            s_line = line.lstrip()
            if any([s_line.startswith(s) for s in ['| '] if s not in ('|+')]):
                tech_column = s_line.split('|')[column_number]
                technologies = tech_column.split(',')
                technologies = list(map(str.strip, technologies))
                technologies = list(filter(lambda x: x != '-', technologies))
                technologies = list(filter(lambda x: x, technologies)) # filter empty items
                for technology in technologies:
                    counter[technology] += 1
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


def main():
    sort()
    generate_charts('technology')
    generate_charts('database')
    generate_charts('cloud')


if __name__ == "__main__":
    main()
