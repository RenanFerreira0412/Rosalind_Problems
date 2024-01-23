class REVCSolution:
    def __init__(self):
        self.dna = None
        self.dnaReverseComplSeq = ""
        self.read_dna_seq()

    # lendo a sequência do dna
    def read_dna_seq(self):
        with open('C:\Programming\Rosalind\input/rosalind_revc.txt', 'r') as input_data:
            self.dna = input_data.read()
            input_data.close()

    # inverter sequência
    def reverse(self, complement):
        reverseComp = ""
        for i in range(len(complement)-1, -1, -1):
            reverseComp += complement[i]
        return reverseComp

    # definir complemento
    def set_complement(self):
        pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

        dnaComplementSeq = ""
        for base in self.dna:
            if base in pairs:
                dnaComplementSeq += pairs[base]

        self.dnaReverseComplSeq = self.reverse(dnaComplementSeq)

    # gerando a saída
    def get_reverse_complement(self):
        self.set_complement()
        with open('C:\Programming\Rosalind\output/REVC.txt', 'w') as output_data:
            output_data.write(self.dnaReverseComplSeq)
            output_data.close()


if __name__ == "__main__":
    solution = REVCSolution()
    solution.get_reverse_complement()
