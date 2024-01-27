import os


class IPRBSolution:
    def __init__(self):
        self.k = 0
        self.m = 0
        self.n = 0
        self.pop = 0

        self.get_individuals()

    # número de indivíduos
    def get_number_of_individuals(self, individuals: list):
        self.k = individuals[0]  # número de homozigotos dominantes
        self.m = individuals[1]  # número de heterozigotos
        self.n = individuals[2]  # número de homozigotos recessivos

        self.pop = self.k + self.m + self.n  # população

    # pegar os indivíduos
    def get_individuals(self):
        try:
            path = os.path.realpath("../../input/rosalind_iprb.txt")
            input_data = open(path, 'r')
            line = input_data.readline().strip()
            # número de cada indivíduo
            number_each_individual = [int(quantity)
                                      for quantity in line.split()]
            self.get_number_of_individuals(number_each_individual)
            input_data.close()
            
        except IOError:
            print("Erro na leitura do arquivo!")

    # calcular probabilidade
    def cal_probability(self):
        k = self.k
        m = self.m
        n = self.n
        pop = self.pop

        # formulação feita através da análise de todas as possibilidades do caso em questão
        numerator = (k * (k - 1) + m * (m - 1) * 0.75 + 2 *
                     (k * m + k * n + m * n * 0.5))

        denominator = pop * (pop - 1)

        probability = numerator / denominator

        return probability

    # probabilidade

    def probability(self):
        probability = self.cal_probability()

        try:
            path = os.path.realpath("../../output/IPRB.txt")
            output_data = open(path, 'w')
            output_data.write(f"{probability:.5f}")
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = IPRBSolution()
    solution.probability()
