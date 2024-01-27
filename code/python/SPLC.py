import os


class SPLCSolution:
    def __init__(self):
        self.pre_mRNA = None
        self.strand_mRNA = None
        self.protein = ""
        self.introns = []
        # não codificam para nenhum aminoácido
        self.stop_codons = ["UAA", "UAG", "UGA"]
        self.aminoacids = ['S', 'L', 'C', 'W', 'E', 'D', 'P', 'V',
                           'N', 'M', 'K', 'Y', 'I', 'Q', 'F', 'R', 'T', 'A', 'G', 'H']
        # codificam para algum aminoácido
        self.rna_codons = [['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], ['UGU', 'UGC'], ['UGG'], ['GAA', 'GAG'], ['GAU', 'GAC'], ['CCU', 'CCC', 'CCA', 'CCG'], ['GUU', 'GUC', 'GUA', 'GUG'], ['AAU', 'AAC'], [
            'AUG'], ['AAA', 'AAG'], ['UAU', 'UAC'], ['AUU', 'AUC', 'AUA'], ['CAA', 'CAG'], ['UUU', 'UUC'], ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], ['ACU', 'ACC', 'ACA', 'ACG'], ['GCU', 'GCC', 'GCA', 'GCG'], ['GGU', 'GGC', 'GGA', 'GGG'], ['CAU', 'CAC']]

        self.read_dna_and_introns()
        self.remove_introns()

    # transcrever DNA
    def transcribe_dna(self, dna: str):
        return dna.replace('T', 'U')

    # lendo a sequência de DNA e os íntrons
    def read_dna_and_introns(self):
        is_label = 1
        line_val = ""

        try:
            path = os.path.realpath("../../input/rosalind_splc.txt")
            input_data = open(path, 'r')
            # linhas de texto do arquivo
            lines = input_data.readlines()

            for i in range(len(lines)):
                # linha de texto
                line = lines[i].strip()

                if line[0] == '>':
                    if is_label == 2:
                        self.pre_mRNA = self.transcribe_dna(line_val)

                    if is_label >= 3:
                        self.introns.append(self.transcribe_dna(line_val))

                    line_val = ""
                    is_label += 1
                    continue

                line_val += line

            # adicionando a última sequência íntrons
            self.introns.append(self.transcribe_dna(line_val))

            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # traduzir mRNA em sequência de aminoácidos - proteína
    def translate_mRNA(self, mRNA: str):
        for i in range(0, len(self.strand_mRNA), 3):
            codon = self.strand_mRNA[i:i+3]

            # códon codifica para algum aminoácido
            if codon not in self.stop_codons:
                for j, codons in enumerate(self.rna_codons):
                    if codon in codons:
                        self.protein += self.aminoacids[j]

    # remover os íntrons da sequência a ser traduzida
    def remove_introns(self):
        for intron in self.introns:
            self.pre_mRNA = self.pre_mRNA.replace(intron, "")
        self.strand_mRNA = self.pre_mRNA

    # retornar a proteína
    def get_protein(self):
        self.translate_mRNA(self.strand_mRNA)

        try:
            path = os.path.realpath("../../output/SPLC.txt")
            output_data = open(path, 'w')
            output_data.write(self.protein)
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = SPLCSolution()
    solution.get_protein()
