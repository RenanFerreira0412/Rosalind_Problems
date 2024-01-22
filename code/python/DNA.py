class DNASolution:
    def __init__(self):
        self.dna = None
        self.dnaBases = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        self.readDnaSeq()
        self.countDnaBases()

    # lendo a sequência do dna
    def readDnaSeq(self):
        with open('C:\Programming\Rosalind\input/rosalind_dna.txt', 'r') as input_data:
            self.dna = input_data.read()
            input_data.close()

    # contando a qtd. de cada base (A, C, G, T)
    def countDnaBases(self):
        for base in self.dna:
            if base in self.dnaBases:
                self.dnaBases[base] += 1

    # resultado da qtd. de cada base
    def numberDnaBases(self):
        bases = list(self.dnaBases.values())

        with open('C:\Programming\Rosalind\output\DNA.txt', 'w') as output_data:
            for amount in bases:
                output_data.write(f"{amount: <5}")
            output_data.close()


if __name__ == "__main__":
    DNASolution().numberDnaBases()
