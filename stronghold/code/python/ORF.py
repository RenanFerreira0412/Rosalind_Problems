class ORFSolution:
    def __init__(self):
        self.rna_seq_one = None
        self.rna_seq_two = None
        self.proteins = []
        self.start_codon = "AUG"
        self.stop_codons = ["UAA", "UAG", "UGA"]
        self.aminoacids = ['S', 'L', 'C', 'W', 'E', 'D', 'P', 'V',
                           'N', 'M', 'K', 'Y', 'I', 'Q', 'F', 'R', 'T', 'A', 'G', 'H']
        self.rna_codons = [['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], ['UGU', 'UGC'], ['UGG'], ['GAA', 'GAG'], ['GAU', 'GAC'], ['CCU', 'CCC', 'CCA', 'CCG'], ['GUU', 'GUC', 'GUA', 'GUG'], ['AAU', 'AAC'], [
            'AUG'], ['AAA', 'AAG'], ['UAU', 'UAC'], ['AUU', 'AUC', 'AUA'], ['CAA', 'CAG'], ['UUU', 'UUC'], ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], ['ACU', 'ACC', 'ACA', 'ACG'], ['GCU', 'GCC', 'GCA', 'GCG'], ['GGU', 'GGC', 'GGA', 'GGG'], ['CAU', 'CAC']]

        self.read_dna_seq()

    def transcribe_dna(self, dna: str):
        return dna.replace('T', 'U')

    def reverse(self, complement: str):
        reverseComp = ""
        for i in range(len(complement)-1, -1, -1):
            reverseComp += complement[i]
        return reverseComp

    def reverseComp(self, dna: str):
        pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        dnaComplementSeq = ""
        for base in dna:
            dnaComplementSeq += pairs[base]
        return self.reverse(dnaComplementSeq)

    def read_dna_seq(self):
        dna = ""
        with open("C:/Programming/Rosalind/input/rosalind_orf.txt", "r") as input_data:
            lines = input_data.readlines()
            for i in range(len(lines)):
                line = lines[i].strip()
                if line[0] != '>':
                    dna += line
            input_data.close()
        self.rna_seq_one = self.transcribe_dna(dna)
        reverseComp = self.reverseComp(dna)
        self.rna_seq_two = self.transcribe_dna(reverseComp)

        print(self.rna_seq_one)
        print(self.rna_seq_two)

    def translate_rna(self, rna: str):
        protein = ""
        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            for j, codons in enumerate(self.rna_codons):
                if codon in codons:
                    protein += self.aminoacids[j]
        return protein

    def open_reading_frame(self, rna):
        start = -1
        orf = ""
        i = 3
        while i < len(rna):
            if rna[i-3:i] == self.start_codon:
                start = 1
            if rna[i-3:i] in self.stop_codons:
                protein = self.translate_rna(orf)
                self.proteins.append(protein)
                print(orf)
                orf = ""
                start = 0
            if start == 1:
                orf += rna[i-3:i]
                i += 3
                continue
            i += 1

    def get_proteins(self, rna_seq):
        self.open_reading_frame(rna_seq)

        with open("C:/Programming/Rosalind/output/ORF.txt", "w") as output_data:
            for protein in self.proteins:
                output_data.write(f"{protein}\n")
            output_data.close()


if __name__ == "__main__":
    solution = ORFSolution()
    solution.get_proteins(solution.rna_seq_one)
    solution.get_proteins(solution.rna_seq_two)
