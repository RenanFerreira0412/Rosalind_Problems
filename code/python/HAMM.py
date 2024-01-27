import os


class HAMMSolution:
    def __init__(self):
        self.dna_seq_one = None
        self.dna_seq_two = None
        self.distance = 0

        self.read_dna_seq()
        self.get_hamming_distance()

    # lendo as sequências de DNA
    def read_dna_seq(self):
        try:
            path = os.path.realpath("../../input/rosalind_hamm.txt")
            input_data = open(path, 'r')
            lines = input_data.readlines()
            self.dna_seq_one = lines[0].strip()
            self.dna_seq_two = lines[1].strip()
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # calculando a distância
    def get_hamming_distance(self):
        for base_one, base_two in zip(self.dna_seq_one, self.dna_seq_two):
            if base_one != base_two:
                self.distance += 1

    # distância
    def hamming_distance(self):
        try:
            path = os.path.realpath("../../output/HAMM.txt")
            output_data = open(path, 'w')
            output_data.write(f"{self.distance}")
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = HAMMSolution()
    solution.hamming_distance()
