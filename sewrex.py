import re
from enum import Enum


class Color(str, Enum):
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[93m'


# TODO: Função Print

class Sewrex:
    def __init__(self, source, pattern):
        self.source = source
        self.pattern = pattern

    def search(self):
        with open(file=self.source, mode='r') as f:
            text = f.readlines()
            # TODO: Erro de não ler linhas

        text_highlighted = text.copy()

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
            print(new_line)
            a = 1


# TODO: Comentários inglês, explicação conforme um padrão
# TODO: Testes com o WSL

if __name__ == "__main__":

    s = 'test.txt'
    p = '[0-9]{4}\-[0-9]{4}'

    sewrex = Sewrex(source=s, pattern=p)
    sewrex.search()

