import os


class REVCSolution:
    def __init__(self):
        self.dna = None
        self.dna_reverse_compl_seq = ""
        self.read_dna_seq()

    # lendo a sequência do dna
    def read_dna_seq(self):
        try:
            path = os.path.realpath("../../input/rosalind_revc.txt")
            input_data = open(path, 'r')
            self.dna = input_data.readline().strip()
            input_data.close()

        except IOError:
            print("Erro na leitura do arquivo!")

    # inverter sequência
    def reverse(self, complement):
        reverse_comp = ""
        for i in range(len(complement)-1, -1, -1):
            reverse_comp += complement[i]
        return reverse_comp

    # definir complemento
    def set_complement(self):
        pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

        dna_complement_seq = ""
        for base in self.dna:
            dna_complement_seq += pairs[base]

        self.dna_reverse_compl_seq = self.reverse(dna_complement_seq)

    # gerando a saída
    def get_reverse_complement(self):
        self.set_complement()

        try:
            path = os.path.realpath("../../output/REVC.txt")
            output_data = open(path, 'w')
            output_data.write(self.dna_reverse_compl_seq)
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = REVCSolution()
    solution.get_reverse_complement()
