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

        found = list()

        for line in text:
            search = re.finditer(pattern=self.pattern, string=line)

            for result in search:

                # line[result.start():result.end()]
                a = 1
            a = 1


# TODO: Comentários inglês, explicação conforme um padrão


if __name__ == "__main__":

    s = 'test.txt'
    p = '[0-9]{4}\-[0-9]{4}'

    sewrex = Sewrex(source=s, pattern=p)
    sewrex.search()

