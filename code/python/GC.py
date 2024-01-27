import os


class GCSolution:
    def __init__(self):
        self.sequences_of_dna = []
        self.labels = []
        self.quantities = []

        self.read_sequences_dna()

    # lendo as sequências de dna do arquivo
    def read_sequences_dna(self):
        try:
            path = os.path.realpath("../../input/rosalind_gc.txt")
            input_data = open(path, 'r')
            # linhas de texto
            lines = input_data.readlines()
            # lista com todos os rótulos
            self.labels = [label for label in lines if label[0] == '>']

            dna_seq = ""
            for line in lines:
                # verificando se a linha de texto não é um rótulo
                if line not in self.labels:
                    dna_seq += line.strip()
                    # verificando se é a última linha
                    if line == lines[-1]:
                        # adicionando a última seuquência de dna
                        self.sequences_of_dna.append(dna_seq)
                    continue

                if dna_seq:
                    # adicioando as sequências de dna
                    self.sequences_of_dna.append(dna_seq)
                dna_seq = ""
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # pegando a quantidade do conteúdo GC na sequência de DNA
    def get_gc_content(self, dna: str):
        quantity = 0
        for base in dna:
            if base in ['G', 'C']:
                quantity += 1
        return quantity

    # pegando o índice da maior quantidade
    def get_index_largest_quantity(self, quantities: list):
        max = quantities[0]
        index = 0
        for i in range(1, len(quantities)):
            if quantities[i] > max:
                max = quantities[i]
                index = i
        return index

    # pegando a maior quantidade
    def get_highest_gc_content(self):
        for dna in self.sequences_of_dna:
            quantity = self.get_gc_content(dna)
            self.quantities.append(quantity*100/len(dna))
        i = self.get_index_largest_quantity(self.quantities)
        return i

    # maior quantidade
    def highest_gc_content(self):
        i = self.get_highest_gc_content()
        quantity = self.quantities[i]
        label = self.labels[i]

        try:
            path = os.path.realpath("../../output/GC.txt")
            output_data = open(path, 'w')
            output_data.write(f"{label}")
            output_data.write(f"{quantity:.6f}")
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = GCSolution()
    solution.highest_gc_content()
