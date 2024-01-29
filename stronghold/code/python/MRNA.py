import os


class MRNASolution:
    def __init__(self):
        self.protein = None
        self.codons = {
            'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
            'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
            'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
            'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
            'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
            'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
            'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
            'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
            'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
            'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
            'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',     'CAG': 'Q',
            'AAG': 'K',     'GAG': 'E',     'UGU': 'C',     'CGU': 'R',
            'AGU': 'S',     'GGU': 'G',     'UGC': 'C',     'CGC': 'R',
            'AGC': 'S',     'GGC': 'G',     'CGA': 'R',     'AGA': 'R',
            'GGA': 'G',     'UGG': 'W',     'CGG': 'R',     'AGG': 'R',
            'GGG': 'G'
        }
        self.get_protein()

    # 'pegando' a proteína
    def get_protein(self):
        try:
            path = os.path.realpath("../../input/rosalind_mrna.txt")
            input_data = open(path, 'r')
            # proteína
            self.protein = input_data.readline().strip()
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # contando a possibilidade de códons para cada aminoácido
    def count_codons(self, aminoacid: str):
        codons = [codon for codon in self.codons.keys(
        ) if self.codons[codon] == aminoacid]

        # retornando o número de códons que podem codificar para determinado aminoácido
        return len(codons)

    # Inferindo mRNA da proteína
    def infer_mRNA_from_protein(self):
        number_diff_rna = 3

        for aminoacid in self.protein:
            # calculando o número de diferentes sequências de rna
            number_diff_rna *= self.count_codons(aminoacid)

        return number_diff_rna % 1000000

    # número de sequências de rna
    def number_different_rna(self):
        number = self.infer_mRNA_from_protein()

        try:
            path = os.path.realpath("../../output/MRNA.txt")
            output_data = open(path, 'w')
            output_data.write(f"{number}")
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = MRNASolution()
    solution.number_different_rna()
