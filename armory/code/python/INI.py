import os

class INISolution:
    def __init__(self) -> None:
        # DNA
        self.dna = None

        self.__get_dna_sequence()

    # lendo a sequência de DNA
    def __get_dna_sequence(self):
        try:
            path = os.path.realpath("../../input/rosalind_ini.txt")
            input_data = open(path, 'r')
            self.dna = input_data.readline().strip()
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # contando a quantidade de cada nucleotídeo
    def __count_dna_nucleotides(self):
        count = dict()

        # contando a quantidade de cada base
        for base in self.dna:
            if base in count:
                count[base] += 1
                continue
            count[base] = 1

        # ordenando o dicionário pelas chaves
        values = [value[1] for value in sorted(count.items())]

        return values

    # retornando resultado
    def dna_nucleotides(self):
        values = self.__count_dna_nucleotides()

        try:
            path = os.path.realpath("../../output/INI.txt")
            output_data = open(path, 'w')
            output_data.write(' '.join(map(str, values)))
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = INISolution()
    solution.dna_nucleotides()
