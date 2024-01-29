import os
import requests


class GBKSolution:
    def __init__(self):
        self.number_nucleotide = 0
        self.gene = None
        self.mindate = None
        self.maxdate = None

        self.__get_search_parameters()
        self.__fetch_number_nucleotide()

    # receber parâmetros de busca
    def __get_search_parameters(self):
        try:
            path = os.path.realpath("../../input/rosalind_gbk.txt")
            input_data = open(path, 'r')
            lines = input_data.readlines()
            # lendo os parâmetros
            self.gene = lines[0].strip()
            self.mindate = lines[1].strip()
            self.maxdate = lines[2].strip()
            input_data.close()
        except IOError:
            print("Erro na leitura do arquivo!")

    # carregando os dados
    def __fetch_number_nucleotide(self):
        base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
        search_term = f'db=nucleotide&term=({self.gene}[Organism]) AND ("{self.mindate}"[Publication Date]: "{self.maxdate}"[Publication Date])&retmode=json'

        url = f"{base_url}{search_term}"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                # dados
                data = response.json()
                # quantidade
                number = data["esearchresult"]["count"]
                self.number_nucleotide = number
        except requests.HTTPError as e:
            print(f"Erro ao carregar os dados: {e}")

    # retornando número de entradas do Nucleotide GenBank para um determinado gênero
    def get_number_nucleotide_genbank(self):
        try:
            path = os.path.realpath("../../output/GBK.txt")
            output_data = open(path, 'w')
            output_data.write(f"{self.number_nucleotide}")
            output_data.close()
        except IOError:
            print("Erro na escrita do arquivo!")


if __name__ == "__main__":
    solution = GBKSolution()
    solution.get_number_nucleotide_genbank()
