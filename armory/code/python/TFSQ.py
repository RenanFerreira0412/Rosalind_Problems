import os


class TFSQSolution:
    def __init__(self):
        self.labels = []
        self.sequences = []

        self.read_fastq_file()

    def read_fastq_file(self):
        try:
            path = os.path.realpath("../../input/rosalind_tfsq.txt")
            input_data = open(path, 'r')
            lines = input_data.readlines()
            # 1/2 5/6 9/10
            # identificador da sequência

            for i in range(0, len(lines), 4):
                label = lines[i].replace('@', '>')
                sequence = lines[i+1]
                self.labels.append(label)
                self.sequences.append(sequence)

            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    def write_data_in_fasta_file(self):
        try:
            path = os.path.realpath("../../output/TFSQ.txt")
            output_data = open(path, 'w')
            for label, sequence in zip(self.labels, self.sequences):
                output_data.write(label)
                output_data.write(sequence)
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = TFSQSolution()
    solution.write_data_in_fasta_file()
