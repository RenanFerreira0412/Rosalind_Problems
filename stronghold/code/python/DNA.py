import os



class DNASolution:
    def __init__(self):
        self.dna = None
        self.dna_bases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        self.read_dna_seq()
        self.count_dna_bases()

    # lendo a sequência do dna
    def read_dna_seq(self):
        try:
            path = os.path.realpath("../../input/rosalind_dna.txt")
            input_data = open(path, 'r')
            self.dna = input_data.read().strip()
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # contando a qtd. de cada base (A, C, G, T)
    def count_dna_bases(self):
        for base in self.dna:
            self.dna_bases[base] += 1

    # resultado da qtd. de cada base
    def number_dna_bases(self):
        bases = list(self.dna_bases.values())

        try:
            path = os.path.realpath("../../output/DNA.txt")
            output_data = open(path, 'w')
            output_data.write(' '.join(map(str, bases)))
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = DNASolution()
    solution.number_dna_bases()
