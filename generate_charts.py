# coding: utf-8


def main():
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


if __name__ == "__main__":
    main()
