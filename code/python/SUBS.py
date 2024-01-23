class SUBSSolutions:
    def __init__(self):
        self.dna_seq_one = None
        self.dna_seq_two = None
        self.locations = []

        self.read_dna_seq()
        self.check_locations()

    # lendo as sequências de DNA
    def read_dna_seq(self):
        with open("C:/Programming/Rosalind/input/rosalind_subs.txt", 'r') as input_data:
            lines = input_data.readlines()
            self.dna_seq_one = lines[0].strip()
            self.dna_seq_two = lines[1].strip()
            input_data.close()

    # verificando as localizações da substring
    def check_locations(self):
        substr_size = len(self.dna_seq_two)

        for i in range(len(self.dna_seq_one)-substr_size+1):
            if self.dna_seq_one[i:i+substr_size] == self.dna_seq_two:
                self.locations.append(i+1)

    def get_locations(self):
        with open("C:/Programming/Rosalind/output/SUBS.txt", 'w') as output_data:
            for location in self.locations:
                output_data.write(' '.join(map(str, self.locations)))
            output_data.close()


if __name__ == "__main__":
    solution = SUBSSolutions()
    solution.get_locations()
