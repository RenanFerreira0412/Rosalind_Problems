import os


class IEVSolution:
    """ 
        1 - AA-AA
        2 - AA-Aa
        3 - AA-aa
        4 - Aa-Aa
        5 - Aa-aa
        6 - aa-aa 
    """

    def __init__(self):
        self.offspring = [2, 2, 2, 1.5, 1, 0]
        self.couples = []

        self.read_number_of_couples()

    # lendo o número de casais em uma população
    def read_number_of_couples(self):
        try:
            path = os.path.realpath("../../input/rosalind_iev.txt")
            input_data = open(path, 'r')
            # linha de texto
            line = input_data.readline()
            self.couples = [int(number) for number in line.split()]
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # número esperado de descendentes
    def number_of_offspring(self):
        number = 0
        for offspring, couples in zip(self.offspring, self.couples):
            number += offspring * couples
        return number

    def get_offspring(self):
        offspring = self.number_of_offspring()

        try:
            path = os.path.realpath("../../output/IEV.txt")
            output_data = open(path, 'w')
            output_data.write(f"{offspring}")
            output_data.close()

        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = IEVSolution()
    solution.get_offspring()
