import re
from enum import Enum


class Color(str, Enum):
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[93m'
    GRAY = '\033[37m'


class Sewrex:
    def __init__(self, source, pattern, dilation=1, print_all=False):
        self.source = source
        self.pattern = pattern
        self.text_highlighted = None
        self.highlight_lines = list()
        self.dilation = dilation
        self.print_all = print_all

    def search(self):
        with open(file=self.source, mode='r') as f:
            text = f.read().splitlines()
            # TODO: Erro de não ler linhas

        self.text_highlighted = text.copy()

        found = list()

        for i, line in enumerate(text):
            search = re.findall(pattern=self.pattern, string=line)

            if len(search) == 0:
                continue

            iter_find = re.finditer(pattern=self.pattern, string=line)

            split = re.split(pattern=self.pattern, string=line)
            new_line = split[0]
            next_section = 1

            for result in iter_find:
                new_line += Color.YELLOW + line[result.start():result.end()] + Color.GRAY
                new_line += split[next_section]
                next_section += 1
                self.text_highlighted[i] = new_line
                self.highlight_lines.append(i)

    def print_result(self):
        len_line = str(len(str(len(self.text_highlighted))) + 9)

        print_lines = [0 for l in range(len(self.text_highlighted))]

        if self.print_all:
            print_lines = [1 for l in range(len(self.text_highlighted))]
        else:
            for line_h in self.highlight_lines:
                print_lines[line_h] = 1
                for i in range(self.dilation):
                    if (line_h + i + 1) == len(print_lines):
                        break
                    print_lines[line_h + i + 1] = 1

                for i in range(self.dilation):
                    if (line_h - i - 1) < 0:
                        break
                    print_lines[line_h - i - 1] = 1

        for i, line in enumerate(self.text_highlighted):
            if print_lines[i] == 0:
                continue

            row = Color.RESET + str(i) + Color.GRAY
            if i in self.highlight_lines:
                row = Color.YELLOW + str(i) + Color.GRAY
            line_print = '{:>' + len_line + '} {}'
            print(line_print.format(row, line))


# TODO: Comentários inglês, explicação conforme um padrão
# TODO: Adicionar Args
# TODO: Documentar funções
# TODO: Atualizar README

if __name__ == "__main__":
    s = 'test.txt'
    p = '[0-9]{4}\-[0-9]{4}'

    sewrex = Sewrex(source=s, pattern=p, dilation=3)
    sewrex.search()
    sewrex.print_result()
