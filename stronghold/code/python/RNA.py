import os


class RNASolution:
    def __init__(self):
        self.dna = None
        self.read_dna_seq()

    # lendo a sequência do dna
    def read_dna_seq(self):
        try:
            path = os.path.realpath("../../input/rosalind_rna.txt")
            input_data = open(path, 'r')
            self.dna = input_data.read().strip()
            input_data.close()

        except IOError:
            print("Erro na leitura do arquivo!")

    # transcrevendo a sequência de dna para rna
    def transcribing_dna_to_rna(self):
        rna = ""

        for base in self.dna:
            if base == "T":
                rna += "U"
                continue
            rna += base

        return rna

    # sequência rna
    def getRnaSeq(self):
        rna = self.transcribing_dna_to_rna()

        try:
            path = os.path.realpath("../../output/RNA.txt")
            output_data = open(path, 'w')
            output_data.write(rna)
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = RNASolution()
    solution.getRnaSeq()
