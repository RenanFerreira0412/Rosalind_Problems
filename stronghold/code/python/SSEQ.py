import os


class SSEQSolution:
    def __init__(self):
        self.dna_one = None
        self.dna_two = None
        self.positions = []

        self.get_dna_sequences()
        self.get_locations()

    # lendo as sequências de dna
    def get_dna_sequences(self):
        try:
            path = os.path.realpath("../../input/rosalind_sseq.txt")
            input_data = open(path, 'r')
            lines = input_data.readlines()
            labels = [line for line in lines if line[0] == '>']
            sequences = []
            dna = ""
            for line in lines:
                if line not in labels:
                    dna += line.strip()
                    if line == lines[-1]:
                        sequences.append(dna)
                    continue

                if dna:
                    sequences.append(dna)
                dna = ""

            self.dna_one = sequences[0]
            self.dna_two = sequences[1]
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # verificando a posição da base no dna
    def check_position_of_base_in_dna(self, base: str, start: int):
        pos = 0
        i = start + 1
        while i < len(self.dna_one):
            if self.dna_one[i] == base:
                pos = i
                break
            i += 1
        return pos

    # 'pegando' todas as posições
    def get_locations(self):
        pos = 1
        for base in self.dna_two:
            # verificando a posição
            pos = self.check_position_of_base_in_dna(base, pos)
            # adicionando a posição
            self.positions.append(pos+1)

    def locations(self):
        try:
            path = os.path.realpath("../../output/SSEQ.txt")
            output_data = open(path, 'w')
            locations = ' '.join(map(str, self.positions))
            output_data.write(locations)
            output_data.close()
        except IOError:
            print("Erro na escrita no arquivo!")


if __name__ == "__main__":
    solution = SSEQSolution()
    solution.locations()
