import argparse
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
                new_line += (
                    Color.YELLOW + line[result.start() : result.end()] + Color.GRAY
                )
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
            print(f'{row} {line}')


# TODO: Comentários inglês, explicação conforme um padrão
# TODO: Adicionar Args
# TODO: Documentar funções
# TODO: Atualizar README
# TODO: Erros (Regex falso;Erro no arquivo; Não encontrou nada)
# TODO: Printar quantos resultados encontrados

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Sewrex (Search With Regular Expression) is a python script to be executed in the console,'
        'performing search in text files with regular expression. Sewrex uses only python built-in'
        ' libraries.'
    )

    parser.add_argument('-s', metavar='--source', type=str, help='Source text file')

    parser.add_argument(
        '-re', metavar='--regex', type=str, help='Regular expression pattern'
    )

    parser.add_argument(
        '-d',
        metavar='--dilation',
        type=int,
        help='(Optional) Defines how many lines will be printed with dilation up to 10 lines. Default is 1 line',
        default=1,
        choices=range(1, 10),
    )

    parser.add_argument(
        '-p',
        metavar='--print',
        type=bool,
        help='(Optional) Boolean flag to print all the text, default is False',
        default=False,
        choices=[True, False],
    )

    args = parser.parse_args()

    sewrex = Sewrex(
        source=args.s,
        pattern=args.re,
        dilation=args.d,
        print_all=args.p,
    )
    sewrex.search()
    sewrex.print_result()
