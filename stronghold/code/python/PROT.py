import os


class PROTSolution:
    def __init__(self):
        self.strand_mRNA = None
        self.protein = ""
        # não codificam para nenhum aminoácido
        self.stop_codons = ["UAA", "UAG", "UGA"]
        self.aminoacids = ['S', 'L', 'C', 'W', 'E', 'D', 'P', 'V',
                           'N', 'M', 'K', 'Y', 'I', 'Q', 'F', 'R', 'T', 'A', 'G', 'H']
        # codificam para algum aminoácido
        self.rna_codons = [['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], ['UGU', 'UGC'], ['UGG'], ['GAA', 'GAG'], ['GAU', 'GAC'], ['CCU', 'CCC', 'CCA', 'CCG'], ['GUU', 'GUC', 'GUA', 'GUG'], ['AAU', 'AAC'], [
            'AUG'], ['AAA', 'AAG'], ['UAU', 'UAC'], ['AUU', 'AUC', 'AUA'], ['CAA', 'CAG'], ['UUU', 'UUC'], ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], ['ACU', 'ACC', 'ACA', 'ACG'], ['GCU', 'GCC', 'GCA', 'GCG'], ['GGU', 'GGC', 'GGA', 'GGG'], ['CAU', 'CAC']]

        self.read_strand_mRNA()
        self.translate_rna_into_protein()

    # lendo a fita de mRNA
    def read_strand_mRNA(self):
        try:
            path = os.path.realpath("../../input/rosalind_prot.txt")
            input_data = open(path, 'r')
            self.strand_mRNA = input_data.read()
            input_data.close()

        except IOError:
            print("Erro na leitura do arquivo!")

    # traduzir sequência de dna em proteína
    def translate_rna_into_protein(self):
        for i in range(0, len(self.strand_mRNA), 3):
            codon = self.strand_mRNA[i:i+3]

            # códon codifica para algum aminoácido
            if codon not in self.stop_codons:
                for j, codons in enumerate(self.rna_codons):
                    if codon in codons:
                        self.protein += self.aminoacids[j]

    def get_protein(self):
        try:
            path = os.path.realpath("../../output/PROT.txt")
            output_data = open(path, 'w')
            output_data.write(self.protein)
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = PROTSolution()
    solution.get_protein()
