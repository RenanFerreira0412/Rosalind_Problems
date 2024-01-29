import os


class PRTMSolution:
    def __init__(self):
        # proteína
        self.protein = None
        # massas
        self.monoisotopic_mass = {
            'A':   71.03711,
            'C':   103.00919,
            'D':   115.02694,
            'E':  129.04259,
            'F': 147.06841,
            'G': 57.02146,
            'H':  137.05891,
            'I': 113.08406,
            'K':   128.09496,
            'L':  113.08406,
            'M': 131.04049,
            'N': 114.04293,
            'P':   97.05276,
            'Q':  128.05858,
            'R': 156.10111,
            'S':   87.03203,
            'T':  101.04768,
            'V': 99.06841,
            'W':   186.07931,
            'Y':  163.06333
        }

        self.get_protein()

    # lendo a proteína
    def get_protein(self):
        try:
            path = os.path.realpath("../../input/rosalind_prtm.txt")
            input_data = open(path, 'r')
            self.protein = input_data.readline().strip()
            input_data.close()

        except IOError:
            print("Erro na leitura do arquivo!")

    # calcular o peso
    def calculate_weight(self):
        weight = 0
        for aminoacid in self.protein:
            weight += self.monoisotopic_mass[aminoacid]
        return weight

    # escrevendo o peso
    def get_weight(self):
        weight = self.calculate_weight()

        try:
            path = os.path.realpath("../../output/PRTM.txt")
            output_data = open(path, 'w')
            output_data.write(f"{weight:.3f}")
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = PRTMSolution()
    solution.get_weight()
