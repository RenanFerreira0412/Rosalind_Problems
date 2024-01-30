import os
import json


class ORFSolution:
    def __init__(self):
        self.dna = None
        self.dna_reverse_comple = None
        self.proteins = set()
        self.codons = {}

        self.get_dna_sequence()
        self.get_codons()
        self.open_reading_frame()

    def get_complement_of(self, dna: str):
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

        c = ""
        for base in dna:
            c += complement[base]

        # retornando o complemento
        return c

    # complemento reverso
    def reverse(self, complement: str):
        # tamanho do complemento
        comple_size = len(complement)

        aux = [None] * comple_size

        for i in range(comple_size//2+1):
            j = comple_size - i - 1
            # trocando as posições
            aux[j], aux[i] = complement[i], complement[j]

        return ''.join(aux)

    # lendo a tabela de códons
    def get_codons(self):
        try:
            path = os.path.realpath("../../../utils/codons.json")
            input_data = open(path, 'r')
            self.codons = json.load(input_data)
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo .json!")

    # recebendo a sequência de DNA
    def get_dna_sequence(self):
        try:
            path = os.path.realpath("../../input/rosalind_orf.txt")
            input_data = open(path, 'r')
            # linhas de texto do arquivo
            lines = [line.strip() for line in input_data.readlines()]
            # sequência de DNA
            dna = ''.join(lines[1::])
            self.dna = dna
            # complemento
            complement = self.get_complement_of(dna)
            # complemento reverso
            self.dna_reverse_comple = self.reverse(complement)
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # lendo os frames
    def reading_frames(self, sequence):
        start_codon = "ATG"
        stop_codon = ["TAG", "TGA", "TAA"]
        begins = []
        ends = []

        for start in range(3):
            # tamanho da sequência
            seq_size = len(sequence[start::])
            end = seq_size - seq_size % 3
            orf_starts = []

            for i in range(start, end, 3):
                codon = sequence[i:i+3]

                if codon == start_codon:
                    # adicionando as posições iniciais de cada ORF
                    orf_starts.append(i)

                if codon in stop_codon:
                    # verificando se alguma posição inicial foi adicionada
                    if len(orf_starts) != 0:
                        begins.append(orf_starts)
                        ends.append(i)
                    # limpando as posições iniciais
                    orf_starts = []

        positions = {"begins": begins, "ends": ends}

        return positions

    # DNA -> RNA

    def transcribe_dna(self, dna: str):
        return dna.replace('T', 'U')

    # RNA -> PROTEÍNA
    def translate_rna(self, rna: str):
        protein = ""
        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            protein += self.codons[codon]
        return protein

    def get_orf(self, sequence: str, positions: dict):
        begins = positions['begins']
        ends = positions['ends']

        for begin, end in zip(begins, ends):
            for i in begin:
                dna = sequence[i:end]
                rna = self.transcribe_dna(dna)
                protein = self.translate_rna(rna)
                self.proteins.add(protein)

    def open_reading_frame(self):
        # dna
        positions_one = self.reading_frames(self.dna)
        # complemento reverso do DNA
        positions_two = self.reading_frames(self.dna_reverse_comple)

        self.get_orf(self.dna, positions_one)
        self.get_orf(self.dna_reverse_comple, positions_two)

    def get_protein(self):
        try:
            path = os.path.realpath("../../output/ORF.txt")
            output_data = open(path, 'w')
            for protein in self.proteins:
                output_data.write(f"{protein}\n")
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = ORFSolution()
    solution.get_protein()

