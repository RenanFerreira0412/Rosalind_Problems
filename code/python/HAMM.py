class HAMMSolution:
    def __init__(self):
        self.dna_seq_one = None
        self.dna_seq_two = None
        self.hamming_distance = 0
        self.read_dna_seq()

    # lendo as sequências de DNA
    def read_dna_seq(self):
        with open("C:/Programming/Rosalind/input/rosalind_hamm.txt", 'r') as input_data:
            lines = input_data.readlines()
            self.dna_seq_one = lines[0].strip()
            self.dna_seq_two = lines[1].strip()
            input_data.close()

    # calculando a distância
    def get_hamming_distance(self):
        for base_one, base_two in zip(self.dna_seq_one, self.dna_seq_two):
            if base_one != base_two:
                self.hamming_distance += 1

        with open("C:\Programming\Rosalind\output/HAMM.txt", 'w') as output_data:
            output_data.write(f"{self.hamming_distance}")
            output_data.close()


if __name__ == "__main__":
    solution = HAMMSolution()
    solution.get_hamming_distance()
