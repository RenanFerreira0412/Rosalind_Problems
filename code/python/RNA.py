class RNASolution:
    def __init__(self):
        self.dna = None
        self.readDnaSeq()

    # lendo a sequência do dna
    def readDnaSeq(self):
        with open('C:\Programming\Rosalind\input/rosalind_rna.txt', 'r') as input_data:
            self.dna = input_data.read()
            input_data.close()

    # transcrevendo a sequência de dna para rna
    def transcribingDnaToRna(self):
        rna = ""

        for base in self.dna:
            if base == "T":
                rna += "U"
                continue
            rna += base

        return rna

    # sequência rna
    def getRnaSeq(self):
        rna = self.transcribingDnaToRna()

        with open('C:\Programming\Rosalind\output/RNA.txt', 'w') as output_data:
            output_data.write(rna)
            output_data.close()


if __name__ == "__main__":
    solution = RNASolution()
    solution.getRnaSeq()
