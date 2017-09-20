# coding: utf-8

def main():
    with open('README.md', 'r', encoding='UTF-8') as read_me_file:
        read_me = read_me_file.readlines()

    blocks = []
    last_indent = None
    for line in read_me:
        s_line = line.lstrip()
        indent = len(line) - len(s_line)

        if any([s_line.startswith(s) for s in ['| '] if s not in ('|-') ]):
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

if __name__ == "__main__":
    main()
