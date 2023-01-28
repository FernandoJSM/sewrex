import re
from enum import Enum


class Color(str, Enum):
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[93m'
    GREY = '\033[37m'


# TODO: Função Print

class Sewrex:
    def __init__(self, source, pattern):
        self.source = source
        self.pattern = pattern
        self.text_highlighted = None
        self.highlight_lines = list()

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
                new_line += Color.YELLOW + line[result.start():result.end()] + Color. RESET
                new_line += split[next_section]
                next_section += 1
                self.text_highlighted[i] = new_line
                self.highlight_lines.append(i)

    def print_result(self):
        len_line = str(len(str(len(self.text_highlighted))) + 9)
        for i, line in enumerate(self.text_highlighted):
            row = Color.GREY + str(i) + Color.RESET
            if i in self.highlight_lines:
                row = Color.YELLOW + str(i) + Color.RESET
            line_print = '{:>' + len_line + '} {}'
            print(line_print.format(row, line))

        # for line in text_highlighted:
        #     print(line)


# TODO: Comentários inglês, explicação conforme um padrão
# TODO: Testes com o WSL

if __name__ == "__main__":

    s = 'test.txt'
    p = '[0-9]{4}\-[0-9]{4}'

    sewrex = Sewrex(source=s, pattern=p)
    sewrex.search()
    sewrex.print_result()

