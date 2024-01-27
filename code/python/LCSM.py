import os


class LCSMSolution:
    def __init__(self):
        self.sequences_of_dna = []
        self.read_dna_sequences()

    # lendo as sequências de DNA
    def read_dna_sequences(self):
        try:
            path = os.path.realpath("../../input/rosalind_lcsm.txt")
            input_data = open(path, 'r')
            lines = input_data.readlines()
            dna = ""
            for line in lines:
                if line[0] != '>':
                    dna += line.strip()
                    # verificando se é a última linha de texto
                    if line == lines[-1]:
                        self.sequences_of_dna.append(dna)
                    continue

                if dna:
                    self.sequences_of_dna.append(dna)
                dna = ""

            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

        print(self.sequences_of_dna)


if __name__ == "__main__":
    solution = LCSMSolution()
