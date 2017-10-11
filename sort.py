# coding: utf-8

def generate_charts():
    mapa_tecnologias = filtra_tecnologias('README.md')
    nomes_tecnologias = sorted(mapa_tecnologias, key=mapa_tecnologias.get, reverse=True)
    with open('technology_usage.md', 'w+', encoding='UTF-8') as f:
        f.write('|+Tecnologia  | Quantidade |\n')
        f.write('|------------ | -----------|\n')
        for tecnologia in nomes_tecnologias:
            f.write('|{} |{} |\n'.format(tecnologia, mapa_tecnologias[tecnologia]))

def filtra_tecnologias(readme_file):
    mapa_tecnologias = {}
    with open(readme_file, 'r', encoding='UTF-8') as read_me_file:
        for line in read_me_file:
            s_line = line.lstrip()
            if any([s_line.startswith(s) for s in ['| '] if s not in ('|+')]):
                coluna_tecnologias = s_line.split('|')[4]
                tecnologias = coluna_tecnologias.split(',')
                tecnologias = list(map(str.strip, tecnologias))
                tecnologias = list(filter(lambda x: x != '-', tecnologias))
                for tecnologia in tecnologias:
                    if tecnologia in mapa_tecnologias:
                        mapa_tecnologias[tecnologia] += 1
                    else:
                        mapa_tecnologias[tecnologia] = 1
    return mapa_tecnologias

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
    generate_charts()

if __name__ == "__main__":
    main()
